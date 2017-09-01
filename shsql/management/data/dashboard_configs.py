# The various dashboard default configs
dashboard_configs = [{
    'company': None,
    'platform': 'web',
    'dashboard': 'marketing',
    'config': {
        'fields': [
          'cpm',
          'ctr',
          'clicks',
          'unique_link_clicks',
          'spend',
          'reach',
          'impressions',
          'frequency',
          'cpc',
          'cpp',
          'cost_per_conversion',
          'purchase',
          'init_checkout',
          'add_payment_info',
          'link_click',
          'cost_per_link_click',
          'conversion',
          'add_to_cart',
          'purchase_value',
          'purchasers',
          'unique_conversions',
          'unique_link_clicks_ctr'
        ],
        'hidden_fields': [
          'campaign_id',
          'campaign_name',
          'adset_id',
          'adset_name'
        ],
        'derived_fields': [{
          'field': 'cvr',
          'op': 'truediv',
          'f1': 'unique_conversions',
          'f2': 'unique_link_clicks'
        },{
          'field': 'cppu',
          'op': 'truediv',
          'f1': 'spend',
          'f2': 'purchasers'
        },{
          'field': 'payer_cvr',
          'op': 'truediv',
          'f1': 'purchasers',
          'f2': 'unique_conversions'
        },{
          'field': 'roas',
          'op': 'truediv',
          'f1': 'purchase_value',
          'f2': 'spend'
        },{
          'field': 'arpu',
          'op': 'truediv',
          'f1': 'purchase_value',
          'f2': 'unique_conversions'
        },{
          'field': 'arppu',
          'op': 'truediv',
          'f1': 'purchase_value',
          'f2': 'purchasers'
        },{
          'field': 'link_click_ctr',
          'op': 'truediv',
          'f1': 'link_click',
          'f2': 'impressions'
        },{
          'field': 'cost_per_unique_conversion',
          'op': 'truediv',
          'f1': 'spend',
          'f2': 'unique_conversions'
        }],
        'aggregate_fields': [{
          'field': 'cpc',
          'type': 'weighted',
          'weight': 'clicks'
        },{
          'field': 'cpm',
          'type': 'weighted',
          'weight': 'impressions'
        },{
          'field': 'cost_per_unique_conversion',
          'type': 'weighted',
          'weight': 'unique_conversions'
        },{
          'field': 'cvr',
          'type': 'weighted',
          'weight': 'clicks'
        },{
          'field': 'ctr',
          'type': 'weighted',
          'weight': 'impressions'
        },{
          'field': 'roas',
          'type': 'weighted',
          'weight': 'spend'
        },{
          'field': 'payer_cvr',
          'type': 'weighted',
          'weight': 'unique_conversions'
        },{
          'field': 'arpu',
          'type': 'weighted',
          'weight': 'unique_conversions'
        },{
          'field': 'arppu',
          'type': 'weighted',
          'weight': 'purchasers'
        }],
        'charts': [
          'spend',
          'impressions',
          'cpm',
          'frequency',
          'clicks',
          'cpc',
          'ctr',
          'unique_conversions',
          'cost_per_conversion',
          'cvr',
          'purchasers',
          'cppu',
          'payer_cvr',
          'purchase_value',
          'roas',
          'cost_per_unique_conversion',
          'arpu|arppu',
          'link_click',
          'link_click_ctr',
          'cost_per_link_click',
          'clicks|ctr',
          'spend|cost_per_conversion',
          'spend|roas',
          'spend.pie:geo',
          'impressions.pie:geo',
          'clicks.pie:geo',
          'spend.pie:region',
          'unique_conversions.pie:region',
          'purchase_value.pie:region',
          'unique_conversions.pie:geo',
          'purchase_value.pie:geo',
          'link_click.pie:geo',
          'cpm:geo',
          'cpc:geo',
          'cost_per_conversion:geo',
          'cpm:region',
          'cpc:region',
          'cost_per_conversion:region',
          'ctr|cvr:geo',
          'payer_cvr|roas:geo',
          'arpu|arppu:geo',
          'spend|cost_per_conversion.scatter',
          'payer_cvr|cost_per_conversion.scatter',
          'cppu|arppu.scatter',
          'frequency|payer_cvr.scatter',
          'cost_per_conversion|roas.scatter',
          'payer_cvr|roas.scatter',
          'ctr.histogram',
          'cost_per_conversion.histogram',
          'payer_cvr.histogram',
          'spend.map:geo',
          'spend.map:region',
          'unique_conversions.map:geo',
          'unique_conversions.map:region',
          'purchase_value.map:geo',
          'purchase_value.map:region',
          'roas.map:geo',
          'roas.map:region',
          'empty_2'
        ],
        'tables': [
          'yesterday'
        ]

    }
  },{
    'company': None,
    'platform': 'web',
    'dashboard': 'kpi',
    'config': {
        'fields': [
            'revenue',
            'dau',
            'arpu'
        ],
        'hidden_fields': [],
        'derived_fields': [],
        'aggregate_fields': [],
        'charts': [
            'revenue',
            'dau',
            'arpu'
        ],
        'tables': [
        ]
    }
}]
