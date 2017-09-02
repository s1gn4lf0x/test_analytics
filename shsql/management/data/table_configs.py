table_configs = [{
  'name': 'yesterday',
  'company': None,
  'dashboard': 'marketing',
  'config': {
    'nrow': 3,
    'ncol': 3,
    'days': 1,
    'offset': 1,
    'data': [{
      'field': 'spend',
      'variable': 'Spend',
      'row': 1,
      'col': 1,
      'value': 2000,
      'format': '$,.2f',
      'change': 0.12,
      'changeformat': '.1%',
      'font': {
        'family': 'Geneva',
        'size': 12,
        'color': 'black',
        'changesize': 10,
        'changecolor': 'black'
      }
    },{
      'field': 'unique_conversions',
      'variable': 'New Customers',
      'row': 1,
      'col': 2,
      'value': 355,
      'format': ',',
      'change': 0.09,
      'changeformat': '.1%',
      'font': {
        'family': 'Geneva',
        'size': 12,
        'color': 'black',
        'changesize': 10,
        'changecolor': 'black'
      }
    },{
      'field': 'cost_per_unique_conversion',
      'variable': 'CAC',
      'row': 1,
      'col': 3,
      'value': 10.34,
      'format': '$,.2f',
      'change': 0.03,
      'changeformat': '.1%',
      'font': {
        'family': 'Geneva',
        'size': 12,
        'color': 'black',
        'changesize': 10,
        'changecolor': 'black'
      }
    },{
      'field': 'ctr',
      'variable': 'CTR',
      'row': 2,
      'col': 1,
      'value': 1.4,
      'format': ',.1f',
      'change': -0.03,
      'changeformat': '.1%',
      'font': {
        'family': 'Geneva',
        'size': 12,
        'color': 'black',
        'changesize': 10,
        'changecolor': 'black'
      }
    },{
      'field': 'reach',
      'variable': 'Reach',
      'row': 2,
      'col': 2,
      'value': 3420,
      'format': ',',
      'change': -0.07,
      'changeformat': '.1%',
      'font': {
        'family': 'Geneva',
        'size': 12,
        'color': 'black',
        'changesize': 10,
        'changecolor': 'black'
      }
    },{
      'field': 'cvr',
      'variable': 'CVR',
      'row': 2,
      'col': 3,
      'value': 20.4,
      'format': ',.1f',
      'change': 0.03,
      'changeformat': '.1%',
      'font': {
        'family': 'Geneva',
        'size': 12,
        'color': 'black',
        'changesize': 10,
        'changecolor': 'black'
      }
    }]
  }
}]
