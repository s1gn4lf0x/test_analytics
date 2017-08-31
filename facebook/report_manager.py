import time
from datetime import timedelta

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adreportrun import AdReportRun

class AdDataFormatter:
    """Helper class to correctly format ad data from json string input"""
    def convert_to_float(self, val):
        return float(val)

    def convert_to_int(self, val):
        return int(val)

    def no_convert(self, val):
        return val

    def __init__(self):
        self.field_types = {
            'impressions': self.convert_to_int,
            'spend': self.convert_to_float,
            'frequency': self.convert_to_float,
            'reach': self.convert_to_int,
            'cpm': self.convert_to_float,
            'ctr': self.convert_to_float,
            'unique_ctr': self.convert_to_float,
            'link_click': self.convert_to_int,
            'link_click_ctr': self.convert_to_float,
            'inline_link_clicks': self.convert_to_int,
            'unique_link_clicks': self.convert_to_int,
            'clicks': self.convert_to_int,
            'clicks_unique': self.convert_to_int,
            'cpc': self.convert_to_float,
            'cpp': self.convert_to_float,
            'app_installs': self.convert_to_int,
            'purchase_value': self.convert_to_float,
            'revenue': self.convert_to_float,
            'purchases': self.convert_to_int,
            'purchasers': self.convert_to_int,
            'cost_per_purchase': self.convert_to_float,
            'cost_per_conversion': self.convert_to_float,
            'opens': self.convert_to_int,
            'cost_per_open': self.convert_to_float,
            'cost_per_link_click': self.convert_to_float,
            'add_payment_info': self.convert_to_int,
            'conversion': self.convert_to_int,
            'unique_conversions': self.convert_to_int
        }

    def convert(self, col, val):
        """Convert a column's value to the correct format"""
        if col in self.field_types:
            return self.field_types[col](val)
        else:
            return val

    def convert_values(self, data):
        """Covert the values in the report data to the correct data types"""

        return [{col: self.convert(col, d[col]) for col in d} for d in data]

class ReportManager:
    """Class to handle facebook ad report generation"""

    def __init__(self, setup_map):
        """Initialize the column formatter and the setup map.
        The setup map contains:
            fields: a list of fields to fetch for the report
            params: a map of report query parameters
            (see https://developers.facebook.com/docs/marketing-api/insights/parameters/v2.9)
            basic_columns: a map of insight column names to db column names for
            columns common across app types (non-action columns)
            action_map: a map of maps for various action types to pull for the
            report e.g., actions, cost_per_action_type, action_values, etc
            (see https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats/)
        """
        self.formatter = AdDataFormatter()
        self.setup = setup_map

    def label_field(self):
        if 'label_field' in self.setup:
            return self.setup['label_field']
        else:
            return 'report_date'

    def raw_ad_insights(
        self,
        ad_account,
        report_date = None,
        do_async = False
    ):
        """
        Pull insights from the Insight edge and return the raw insights report
        Params:
        * `ad_account` is your Facebook AdAccount object
        * `report_date` is the date for the insight report
        * `do_async` whether or not to fetch the report asynchronously
        For more information see the [Ads Insights doc](
        https://developers.facebook.com/docs/marketing-api/insights-api)
        """
        if report_date:
            self.setup['params']['time_range'] = {
                'since': report_date,
                'until': report_date
            }

        insights = None
        if not do_async:
            insights = ad_account.get_insights(
                self.setup['fields'],
                self.setup['params']
            )
        else:
            safe_count = 0
            job = ad_account.get_insights(
                self.setup['fields'],
                self.setup['params'],
                async=do_async
            )
            job.remote_read()
            while job[AdReportRun.Field.async_status] != 'Job Completed' and safe_count < 120:
                time.sleep(1)
                rr = job.remote_read()
                safe_count += 1
            insights = job.get_result()

        return insights

    def formatted_ad_insights_from_raw(
        self,
        raw_insights
    ):
        """Take raw facebook insights and return a column formatted result."""

        insight_values = self.insights_value(raw_insights)
        return self.formatter.convert_values(insight_values)

    def insights_value(
        self,
        insights,
        limit=-1
    ):
        """
        Construct an array of insight report from insights object
        Params:
        * `insights` is the object from insights edge
        * `limit` is the limit of records to be returned
        """
        data = [self.values(insight) for insight in insights]
        return data if limit < 0 else data[:limit+1]

    def values(
        self,
        insight
    ):
        """
        Get the values from an insight object
        Params:
        * `insight` is a single insights object
        For more information see the [Insights doc](
        https://developers.facebook.com/docs/marketing-api/insights)
        """
        # action types that we want to get from insight
        # format is action_type_returned_from_api: db_column_name
        actions_map = self.setup['actions_map']

        # general columns that we want to get from insight
        key_value = dict.fromkeys(self.setup['basic_columns'].values())
        for column_key in actions_map:
            key_value.update(dict.fromkeys(actions_map[column_key].values()))

        # get values for general columns
        for k in self.setup['basic_columns']:
            if k in insight:
                if k == 'account_name':
                    key_value[self.setup['basic_columns'][k]] = str(insight[k]).replace(' ', '')
                else:
                    key_value[self.setup['basic_columns'][k]] = insight[k]

        # get values for actions
        for column_key in actions_map:
            if column_key in insight:
                for key in actions_map[column_key]:
                    key_value[actions_map[column_key][key]] = 0
                actions = insight[column_key]
                if not actions:
                    continue
                for action in actions:
                    action_val = self.value_from_action(action, actions_map, column_key)
                    if action_val:
                        col_name = actions_map[column_key][action['action_type']]
                        key_value[col_name] = action_val
            else:
                for t in actions_map[column_key]:
                    key_value[actions_map[column_key][t]] = 0

        return key_value

    def value_from_action(self, action, actions_map, column_key):
        """Get the value for this action.
        If we are using an attribution window, add the total value.
        """
        val = None
        t = action['action_type']
        if t in actions_map[column_key]:
            if 'value' in action:
                val = action['value']
            if 'action_attribution_windows' in self.setup['params']:
                for param in self.setup['params']['action_attribution_windows']:
                    if param in action:
                        fval = float(action[param])
                        val = fval if not val else val+fval

        return val
