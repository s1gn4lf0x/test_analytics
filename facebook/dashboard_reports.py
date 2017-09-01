import os
import boto3
import json
import operator

from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adaccount import AdAccount

from shsql.models import DashboardConfig
from shsql.models import FacebookRawReport
from shsql.models import FacebookDashboardReport

from .util import result_key
from .util import dashboard_config
from .util import report_config
from .util import create_report_date
from .report_manager import ReportManager

def facebook_dashboard_reports_batch(
    accounts,
    level,
    platform,
    breakdown,
    period,
    day=1
):
    """Create a batch of daily dashboard reports"""
    result = []
    for acc in accounts:
        # Get the last daily reports from dynamoDB
        raw_report_date = create_report_date(day)
        setup = report_config(
            level,
            platform,
            breakdown,
            acc.app.company,
            period
        )
        reports = FacebookRawReport.objects.filter(
            company=acc.app.company,
            account=acc,
            config=setup,
            report_date=raw_report_date
        )
        if len(reports) == 0:
            continue

        # Get the dashboard config for this company if there is one
        # otherwise use the default marketing dashboard config
        dash_config = dashboard_config(
            acc.app.company,
            setup.platform,
            'marketing'
        )

        # Run the dashboard report analysis
        manager = ReportManager(setup.config)
        report_data = {field: [] for field in dash_config.config['fields']}
        report_data.update({f['field']: [] for f in dash_config.config['derived_fields']})
        report_data['labels'] = []
        label_field = manager.label_field()
        for r in reports:
            for formatted in manager.formatted_ad_insights_from_raw(r.data):
                if not label_field in formatted:
                    continue
                report_data['labels'].append(formatted[label_field])
                for f in dash_config.config['fields']:
                    if f in formatted:
                        report_data[f].append(formatted[f])
                for f in dash_config.config['hidden_fields']:
                    if f in formatted:
                        if not f in report_data:
                            report_data[f] = []
                        report_data[f].append(formatted[f])
                for f in dash_config.config['derived_fields']:
                    if f['f1'] in formatted and f['f2'] in formatted:
                        try:
                            op_func = getattr(operator, f['op'])
                            val = op_func(formatted[f['f1']],formatted[f['f2']])
                        except ZeroDivisionError as e:
                            val = 0
                        report_data[f['field']].append(val)
        if len(report_data['labels']) > 0:
            (report, created) = FacebookDashboardReport.objects.update_or_create(
                account=acc,
                company=acc.app.company,
                raw_report=r,
                report_date=raw_report_date,
                defaults={'data': report_data}
            )
            result.append({acc.account_id: created})
        else:
            result.append({acc.account_id: -1})
    return result

def facebook_backdate_dashboard_reports_batch(
    accounts,
    level,
    platform,
    breakdown,
    period,
    days,
    offset=1
):
    """Create a batch of backdated daily dashboard reports"""
    result = []
    for d in range(offset,days+offset):
        result.append(facebook_dashboard_reports_batch(
            accounts,
            level,
            platform,
            breakdown,
            period,
            d
        ))
    return result
