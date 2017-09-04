
# Define common objects (used by all configs for a certain platform)
web_fields = [
    'impressions',
    'frequency',
    'spend',
    'reach',
    'cpm',
    'ctr',
    'cpc',
    'cpp',
    'unique_ctr',
    'inline_link_clicks',
    'clicks',
    'unique_clicks',
    'actions',
    'action_values',
    'unique_actions',
    'cost_per_action_type',
    'unique_link_clicks_ctr'
]

web_basic_columns = {
    'impressions': 'impressions',
    'frequency': 'frequency',
    'reach': 'reach',
    'clicks': 'clicks',
    'date_stop': 'report_date',
    'unique_clicks': 'clicks_unique',
    'ctr': 'ctr',
    'unique_ctr': 'ctr_unique',
    'spend': 'spend',
    'cpm': 'cpm',
    'cpc': 'cpc',
    'cpp': 'cpp',
    'unique_link_clicks_ctr': 'unique_link_clicks_ctr'
}

geo_web_basic_columns = {
    'country': 'country'
}
geo_web_basic_columns.update(web_basic_columns)

region_web_basic_columns = {
    'region': 'region'
}
region_web_basic_columns.update(web_basic_columns)

campaign_web_basic_columns = {
    'campaign_id': 'campaign_id',
    'campaign_name': 'campaign_name'
}
campaign_web_basic_columns.update(web_basic_columns)

adset_web_basic_columns = {
    'campaign_id': 'campaign_id',
    'campaign_name': 'campaign_name',
    'adset_id': 'adset_id',
    'adset_name': 'adset_name'
}
adset_web_basic_columns.update(web_basic_columns)

web_actions_map = {
    'actions': {
    'offsite_conversion.fb_pixel_purchase': 'purchase',
    'offsite_conversion.fb_pixel_initiate_checkout': 'init_checkout',
    'offsite_conversion.fb_pixel_add_payment_info': 'add_payment_info',
    'link_click': 'link_click',
    'offsite_conversion': 'conversion',
    'offsite_conversion.fb_pixel_add_to_cart': 'add_to_cart'
    },
    'cost_per_action_type': {
    'offsite_conversion.fb_pixel_purchase': 'cost_per_purchase',
    'link_click': 'cost_per_link_click',
    'offsite_conversion': 'cost_per_conversion'
    },
    'action_values': {
    'offsite_conversion.fb_pixel_purchase': 'purchase_value'
    },
    'unique_actions': {
    'offsite_conversion.fb_pixel_purchase': 'purchasers',
    'offsite_conversion': 'unique_conversions',
    'link_click': 'unique_link_clicks'
    },
    'cost_per_unique_action_type': {
    'link_click': 'cost_per_unique_link_click'
    }
}

facebook_report_configs = [{
    'platform': 'web',
    'level': 'account',
    'breakdown': '',
    'company': None,
    'period': 1,
    'config': {
        'fields': web_fields,
        'basic_columns': web_basic_columns,
        'params': {
          'breakdowns': [],
          'limit': 10,
          'time_range': {
            'until': '2017-05-01',
            'since': '2017-04-30'
          },
          'level': 'account',
          'filtering': []
        },
        'actions_map': web_actions_map
    }
},{
    'platform': 'web',
    'level': 'account',
    'breakdown': 'geo',
    'company': None,
    'period': 1,
    'config': {
        'label_field': 'country',
        'fields': web_fields,
        'basic_columns': geo_web_basic_columns,
        'params': {
          'breakdowns': ['country'],
          'limit': 100,
          'time_range': {
            'until': '2017-05-01',
            'since': '2017-04-30'
          },
          'level': 'account',
          'filtering': [{'field': 'impressions', 'operator': 'GREATER_THAN', 'value': 9}]
        },
        'actions_map': web_actions_map
    }
},{
    'platform': 'web',
    'level': 'account',
    'breakdown': 'region',
    'company': None,
    'period': 1,
    'config': {
        'label_field': 'region',
        'fields': web_fields,
        'basic_columns': region_web_basic_columns,
        'params': {
          'breakdowns': ['region'],
          'limit': 100,
          'time_range': {
            'until': '2017-05-01',
            'since': '2017-04-30'
          },
          'level': 'account',
          'filtering': [{'field': 'impressions', 'operator': 'GREATER_THAN', 'value': 9}]
        },
        'actions_map': web_actions_map
    }
},{
    'platform': 'web',
    'level': 'campaign',
    'breakdown': '',
    'company': None,
    'period': 1,
    'config': {
        'fields': [
            'campaign_name',
            'campaign_id'
        ] + web_fields,
        'basic_columns': campaign_web_basic_columns,
        'params': {
            'breakdowns': [],
            'limit': 100,
            'time_range': {
            'until': '2017-05-01',
            'since': '2017-04-30'
            },
            'level': 'campaign',
            'filtering': []
        },
        'actions_map': web_actions_map
    }
},{
    'platform': 'web',
    'level': 'adset',
    'breakdown': '',
    'company': None,
    'period': 1,
    'config': {
        'fields': [
            'campaign_name',
            'campaign_id',
            'adset_name',
            'adset_id',
        ] + web_fields,
        'basic_columns': adset_web_basic_columns,
        'params': {
          'breakdowns': [],
          'limit': 100,
          'time_range': {
            'until': '2017-05-01',
            'since': '2017-04-30'
          },
          'level': 'adset',
          'filtering': []
        },
        'actions_map': web_actions_map
    }
}]

kpi_report_configs = [{
    "company": None,
    "name": "kpi_cohort_bucket_reports",
    "config": {
        "params": [
            {"name":"D0-7", "lo" : 0, "hi" : 7},
            {"name":"D8-15", "lo" : 8, "hi" : 15},
            {"name":"D16-30", "lo" : 16, "hi" : 30},
            {"name":"D30+", "lo" : 30, "hi" : 30000}
        ]
    }
}]
