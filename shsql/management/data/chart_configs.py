chart_configs = [
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "675",
            "825",
            "811",
            "775",
            "864",
            "820",
            "865",
            "911",
            "952",
            "452",
            "750",
            "815",
            "875",
            "1044",
            "912",
            "850",
            "950",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "915"
          ]
        }
      ],
      "field": "spend",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#ffff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "Daily Spend",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 0.1,
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 0.1,
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            300,
            1100
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickprefix": "$",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 1,
      "section": "time_series",
      "section_height": 1050,
      "section_name": "Upper Funnel - Time Series",
      "section_open": True,
      "width": "100%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "Impressions",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "675",
            "825",
            "811",
            "775",
            "864",
            "820",
            "865",
            "911",
            "952",
            "452",
            "750",
            "815",
            "875",
            "1044",
            "912",
            "850",
            "950",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "915"
          ]
        }
      ],
      "field": "impressions",
      "layout": {
        "autosize": True,
        "bargap": 0.1,
        "bargroupgap": 0.1,
        "barmode": "overlay",
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "separators": ".'",
        "title": "Impressions",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "domain": [
            0,
            1
          ],
          "exponentformat": "none",
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            300,
            1100
          ],
          "showline": False,
          "tickformat": ",",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 2,
      "section": "time_series",
      "section_height": 1050,
      "section_name": "Upper Funnel - Time Series",
      "section_open": True,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "impressions",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "17.591917",
            "16.5906",
            "18.101652",
            "17.538845",
            "14.824664",
            "14.118215",
            "13.624473",
            "17.591917",
            "16.5906",
            "18.101652",
            "17.538845",
            "14.824664",
            "14.118215",
            "13.624473",
            "17.591917",
            "16.5906",
            "18.101652",
            "17.538845",
            "14.824664",
            "13.624473",
            "17.591917",
            "16.5906",
            "14.118215",
            "13.624473"
          ]
        }
      ],
      "field": "cpm",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPM<sup>*</sup>",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False,
          "zerolinecolor": "red",
          "zerolinewidth": 2
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            12,
            19
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$,",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False,
          "zerolinecolor": "#f1f0f0",
          "zerolinewidth": 1
        }
      },
      "row": 2,
      "section": "time_series",
      "section_height": 1050,
      "section_name": "Upper Funnel - Time Series",
      "section_open": True,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cpm",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "Frequency",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "1",
            "1.13",
            "1.14",
            "1.19",
            "1.11",
            "1.23",
            "1.38",
            "1.45",
            "1.53",
            "1.54",
            "1.66",
            "1.62",
            "1.68",
            "1.62",
            "1.57",
            "1.65",
            "1.7",
            "1.8",
            "1.77",
            "1.8",
            "1.89",
            "1.81",
            "1.86",
            "1.87"
          ]
        }
      ],
      "field": "frequency",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "Frequency<sup>*</sup>",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showgrid": True,
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1,
          "hoverformat": ".2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.8,
            2.0
          ],
          "showline": False,
          "tickformat": ".1f",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 2,
      "section": "time_series",
      "section_height": 1050,
      "section_name": "Upper Funnel - Time Series",
      "section_open": True,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "frequency",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "Clicks",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "62",
            "80",
            "71",
            "72",
            "83",
            "80",
            "81",
            "81",
            "91",
            "44",
            "71",
            "77",
            "84",
            "100",
            "81",
            "81",
            "92",
            "94",
            "100",
            "93",
            "100",
            "91",
            "93",
            "90"
          ]
        }
      ],
      "field": "clicks",
      "layout": {
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "title": "Clicks",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(122, 60, 160, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            30,
            110
          ],
          "showline": False,
          "tickformat": ",",
          "ticks": "",
          "ticksuffix": " ",
          "zeroline": False
        }
      },
      "row": 3,
      "section": "time_series",
      "section_height": 1050,
      "section_name": "Upper Funnel - Time Series",
      "section_open": True,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "clicks",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "1.644",
            "1.31",
            "1.232",
            "1.24",
            "1.665",
            "1.78",
            "1.391",
            "1.667",
            "1.305",
            "1.739",
            "1.474",
            "1.786",
            "1.272",
            "1.57",
            "1.306",
            "1.23",
            "1.328",
            "1.299",
            "1.562",
            "1.506",
            "1.446",
            "1.394",
            "1.381",
            "1.676"
          ]
        }
      ],
      "field": "cpc",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPC",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            1.1,
            1.9
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$,.1f",
          "tickmode": "auto",
          "tickprefix": " ",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 3,
      "section": "time_series",
      "section_height": 1050,
      "section_name": "Upper Funnel - Time Series",
      "section_open": True,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cpc",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "2.309959",
            "1.731346",
            "1.831723",
            "1.797838",
            "1.565591",
            "1.366954",
            "1.38205",
            "1.831723",
            "1.797838",
            "1.565591",
            "1.366954",
            "1.38205",
            "2.309959",
            "1.731346",
            "1.831723",
            "1.797838",
            "2.309959",
            "1.731346",
            "1.831723",
            "1.366954",
            "1.38205",
            "1.831723",
            "1.797838",
            "1.565591"
          ]
        }
      ],
      "field": "ctr",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CTR",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showgrid": True,
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1,
          "hoverformat": ".2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            1.2,
            2.4
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".1f",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 3,
      "section": "time_series",
      "section_height": 1050,
      "section_name": "Upper Funnel - Time Series",
      "section_open": True,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "ctr",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "New Users",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "62",
            "80",
            "71",
            "72",
            "83",
            "80",
            "81",
            "81",
            "91",
            "44",
            "71",
            "77",
            "84",
            "100",
            "81",
            "81",
            "92",
            "94",
            "100",
            "93",
            "100",
            "91",
            "93",
            "90"
          ]
        }
      ],
      "field": "unique_conversions",
      "layout": {
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "title": "New Users",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(122, 60, 160, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            30,
            110
          ],
          "showline": False,
          "tickformat": ",",
          "ticks": "",
          "ticksuffix": " ",
          "zeroline": False
        }
      },
      "row": 4,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "unique_conversions",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "3.434",
            "4.883",
            "3.471",
            "4.123",
            "4.883",
            "5.091",
            "4.969",
            "4.12",
            "4.711",
            "5.091",
            "3.706",
            "4.046",
            "4.494",
            "4.483",
            "3.583",
            "4.146",
            "3.609",
            "4.726",
            "4.414",
            "3.637",
            "5.014",
            "5.066",
            "4.2",
            "3.52"
          ]
        }
      ],
      "field": "cost_per_unique_conversion",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPU (CAC)",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            3.0,
            5.2
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$.1f",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 4,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cost_per_unique_conversion",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "34.8",
            "27",
            "34",
            "27.7",
            "30.6",
            "27.1",
            "26.4",
            "27.4",
            "27.2",
            "31.9",
            "26.6",
            "27.6",
            "31.8",
            "25",
            "34.6",
            "28",
            "34.6",
            "25.2",
            "28.7",
            "28.6",
            "28.1",
            "33.7",
            "27.9",
            "25.6"
          ]
        }
      ],
      "field": "cvr",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CVR<sup>*</sup>",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showgrid": True,
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1,
          "hoverformat": ".1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            23,
            36
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".1f",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 4,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cvr",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "Payers",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "62",
            "68",
            "68",
            "66",
            "80",
            "73",
            "69",
            "77",
            "82",
            "39",
            "69",
            "64",
            "79",
            "87",
            "68",
            "80",
            "85",
            "93",
            "95",
            "86",
            "81",
            "82",
            "84",
            "90"
          ]
        }
      ],
      "field": "purchasers",
      "layout": {
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "title": "Payers<sup>*</sup>",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(122, 60, 160, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            30,
            100
          ],
          "showline": False,
          "tickformat": ",",
          "ticks": "",
          "ticksuffix": " ",
          "zeroline": False
        }
      },
      "row": 5,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "purchasers",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "221.94",
            "234.21",
            "198.15",
            "264.17",
            "237.59",
            "181.44",
            "178.42",
            "202.62",
            "243.45",
            "215.78",
            "213.83",
            "260.07",
            "187.32",
            "269.3",
            "274.63",
            "245.12",
            "243.42",
            "193.63",
            "275.76",
            "222.74",
            "279.91",
            "293.13",
            "250.98",
            "290.63"
          ]
        }
      ],
      "field": "cppu",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPP<sup>*</sup>",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            160.0,
            300.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickmode": "auto",
          "tickprefix": " $",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 5,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cppu",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "0.05",
            "0.045",
            "0.043",
            "0.04",
            "0.043",
            "0.044",
            "0.043",
            "0.04",
            "0.039",
            "0.039",
            "0.035",
            "0.033",
            "0.033",
            "0.03",
            "0.029",
            "0.032",
            "0.03",
            "0.033",
            "0.033",
            "0.033",
            "0.034",
            "0.037",
            "0.038",
            "0.036"
          ]
        }
      ],
      "field": "payer_cvr",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "Payer-CVR",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showgrid": True,
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1,
          "hoverformat": ".2%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.02,
            0.05
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".1%",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 5,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "payer_cvr",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "Revenues",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "3216.64",
            "3546.34",
            "5099.07",
            "5424.17",
            "3902.11",
            "4865.24",
            "4631.8",
            "5075.44",
            "6552.7",
            "2076.31",
            "3653.05",
            "6333.49",
            "6986.02",
            "5839.35",
            "3651.66",
            "4244.11",
            "6347.38",
            "7816.56",
            "7631.32",
            "4818.81",
            "6287.6",
            "4457.58",
            "6114.94",
            "3504.15"
          ]
        }
      ],
      "field": "purchase_value",
      "layout": {
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "title": "Revenues<sup>*</sup>",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(122, 60, 160, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            1000,
            9000
          ],
          "showline": False,
          "tickformat": "$,",
          "ticks": "",
          "ticksuffix": " ",
          "zeroline": False
        }
      },
      "row": 6,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "purchase_value",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "fill": "none",
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "0.178",
            "0.211",
            "0.103",
            "0.119",
            "0.134",
            "0.204",
            "0.212",
            "0.309",
            "0.357",
            "0.197",
            "0.143",
            "0.165",
            "0.338",
            "0.233",
            "0.257",
            "0.161",
            "0.327",
            "0.171",
            "0.297",
            "0.29",
            "0.399",
            "0.259",
            "0.277",
            "0.253"
          ]
        }
      ],
      "field": "roas",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "ROAS<sup>*</sup>",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".1%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.04,
            0.42
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".0%",
          "tickmode": "auto",
          "tickprefix": " ",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 6,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "roas",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "ARPU",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "9.38",
            "7.98",
            "6.1",
            "11.09",
            "10.06",
            "10.25",
            "10.62",
            "9.47",
            "13.39",
            "4.64",
            "9.85",
            "9.19",
            "8.49",
            "13.04",
            "13.6",
            "7.68",
            "13.92",
            "11.95",
            "15.54",
            "14.12",
            "12.44",
            "12.38",
            "9.29",
            "14.88"
          ]
        },
        {
          "line": {
            "color": "#41A074",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#41A074",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "ARPPU",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "43.58",
            "43.75",
            "42.88",
            "32.88",
            "53.28",
            "40.15",
            "32.6",
            "43.46",
            "70.89",
            "31.22",
            "36.53",
            "48.9",
            "46",
            "58.45",
            "49.57",
            "38.51",
            "66.26",
            "44.52",
            "48.51",
            "52.9",
            "46.76",
            "50.73",
            "44.42",
            "48.01"
          ],
          "yaxis": "y2"
        }
      ],
      "field": "arpu|arppu",
      "layout": {
        "autosize": True,
        "height": 350,
        "legend": {
          "bgcolor": "rgba(240,240,240,1)",
          "font": {
            "color": "black"
          },
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.02,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showgrid": True,
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 0.1,
          "hoverformat": "$.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            2.0,
            26.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$.1f",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": " ",
          "title": "ARPU",
          "zeroline": False
        },
        "yaxis2": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 0.1,
          "hoverformat": "$.1",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "overlaying": "y",
          "range": [
            0,
            80
          ],
          "rangemode": "tozero",
          "showgrid": False,
          "showline": False,
          "side": "right",
          "tickformat": "$.0f",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": " ",
          "title": "ARPPU",
          "zeroline": False
        }
      },
      "row": 6,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "arpu|arppu",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "Results",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "62",
            "80",
            "71",
            "72",
            "83",
            "80",
            "81",
            "81",
            "91",
            "44",
            "71",
            "77",
            "84",
            "100",
            "81",
            "81",
            "92",
            "94",
            "100",
            "93",
            "100",
            "91",
            "93",
            "90"
          ]
        }
      ],
      "field": "link_click",
      "layout": {
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "title": "Results count",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(122, 60, 160, 1)",
          "linewidth": 2,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            30,
            110
          ],
          "showline": False,
          "tickformat": ",",
          "ticks": "",
          "ticksuffix": " ",
          "zeroline": False
        }
      },
      "row": 7,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "link_click",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "2.79",
            "2.74",
            "2.88",
            "2.79",
            "2.76",
            "2.86",
            "2.69",
            "2.72",
            "2.53",
            "2.6",
            "2.51",
            "2.52",
            "2.56",
            "2.73",
            "2.66",
            "2.82",
            "2.75",
            "2.54",
            "2.59",
            "2.65",
            "2.83",
            "2.52",
            "2.79",
            "2.75"
          ]
        }
      ],
      "field": "cost_per_link_click",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "Cost per Result",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "range": [
            2.4,
            2.9
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$.1f",
          "tickmode": "auto",
          "tickprefix": " ",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 7,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cost_per_link_click",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "Result rate",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "9.38",
            "7.98",
            "6.1",
            "11.09",
            "10.06",
            "10.25",
            "10.62",
            "9.47",
            "13.39",
            "4.64",
            "9.85",
            "9.19",
            "8.49",
            "13.04",
            "13.6",
            "7.68",
            "13.92",
            "11.95",
            "15.54",
            "14.12",
            "12.44",
            "12.38",
            "9.29",
            "14.88"
          ]
        }
      ],
      "field": "link_click_ctr",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "Result rate per User",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showgrid": True,
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "autotick": False,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 0.1,
          "hoverformat": ".2%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "range": [
            2.0,
            18.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ",.1%",
          "tickmode": "auto",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 7,
      "section": "time_series",
      "section_height": 1399,
      "section_name": "Lower Funnel - Time Series",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "link_click_ctr",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "name": "Clicks",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "62",
            "80",
            "71",
            "72",
            "83",
            "80",
            "81",
            "81",
            "91",
            "44",
            "71",
            "77",
            "84",
            "100",
            "81",
            "81",
            "92",
            "94",
            "100",
            "93",
            "100",
            "91",
            "93",
            "90"
          ],
          "yaxis": "y"
        },
        {
          "line": {
            "color": "#41A074",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#41A074",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "CTR",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "2.309959",
            "1.731346",
            "1.831723",
            "1.797838",
            "1.565591",
            "1.366954",
            "1.38205",
            "1.831723",
            "1.797838",
            "1.565591",
            "1.366954",
            "1.38205",
            "2.309959",
            "1.731346",
            "1.831723",
            "1.797838",
            "2.309959",
            "1.731346",
            "1.831723",
            "1.366954",
            "1.38205",
            "1.831723",
            "1.797838",
            "1.565591"
          ],
          "yaxis": "y2"
        }
      ],
      "field": "clicks|ctr",
      "layout": {
        "height": 350,
        "legend": {
          "bgcolor": "rgba(240,240,240,1)",
          "font": {
            "color": "black"
          },
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.02,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ",.0f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "range": [
            30,
            150
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ",",
          "tickprefix": " ",
          "ticks": "",
          "title": "",
          "zeroline": False
        },
        "yaxis2": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "overlaying": "y",
          "range": [
            0.4,
            2.5
          ],
          "showgrid": False,
          "showline": False,
          "side": "right",
          "tickformat": ",.1f",
          "ticks": "",
          "ticksuffix": "%",
          "title": " ",
          "zeroline": False
        }
      },
      "row": 8,
      "section": "time_series",
      "section_height": 350,
      "section_name": "2-Metric comparisons",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "clicks|ctr",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "name": "Spend",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "1898.59",
            "1964.41",
            "2005.12",
            "2076.95",
            "1985.66",
            "2253.62",
            "1618.71",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "1985.66",
            "2253.62",
            "1618.71",
            "1040",
            "1010",
            "1898.59",
            "1964.41",
            "2005.12",
            "2076.95",
            "1985.66",
            "2253.62"
          ],
          "yaxis": "y"
        },
        {
          "line": {
            "color": "#41A074",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#41A074",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "CPU",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "3.434",
            "4.883",
            "3.471",
            "4.123",
            "4.883",
            "5.091",
            "4.969",
            "4.12",
            "4.711",
            "5.091",
            "3.706",
            "4.046",
            "4.494",
            "4.483",
            "3.583",
            "4.146",
            "3.609",
            "4.726",
            "4.414",
            "3.637",
            "5.014",
            "5.066",
            "4.2",
            "3.52"
          ],
          "yaxis": "y2"
        }
      ],
      "field": "spend|cost_per_conversion",
      "layout": {
        "height": 350,
        "legend": {
          "bgcolor": "rgba(240,240,240,1)",
          "font": {
            "color": "black"
          },
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.02,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.0f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "range": [
            800.0,
            3400.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$,",
          "tickprefix": " ",
          "ticks": "",
          "title": "",
          "zeroline": False
        },
        "yaxis2": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "overlaying": "y",
          "range": [
            1.6,
            5.4
          ],
          "showgrid": False,
          "showline": False,
          "side": "right",
          "tickformat": "$,.1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": " ",
          "zeroline": False
        }
      },
      "row": 8,
      "section": "time_series",
      "section_height": 350,
      "section_name": "2-Metric comparisons",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend|cost_per_conversion",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "name": "Spend",
          "type": "bar",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "1898.59",
            "1964.41",
            "2005.12",
            "2076.95",
            "1985.66",
            "2253.62",
            "1618.71",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "1985.66",
            "2253.62",
            "1618.71",
            "1040",
            "1010",
            "1898.59",
            "1964.41",
            "2005.12",
            "2076.95",
            "1985.66",
            "2253.62"
          ],
          "yaxis": "y"
        },
        {
          "line": {
            "color": "#41A074",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#41A074",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "ROAS",
          "type": "scatter",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ],
          "y": [
            "0.178",
            "0.211",
            "0.103",
            "0.119",
            "0.134",
            "0.204",
            "0.212",
            "0.309",
            "0.357",
            "0.197",
            "0.143",
            "0.165",
            "0.338",
            "0.233",
            "0.257",
            "0.161",
            "0.327",
            "0.171",
            "0.297",
            "0.29",
            "0.399",
            "0.259",
            "0.277",
            "0.253"
          ],
          "yaxis": "y2"
        }
      ],
      "field": "spend|roas",
      "layout": {
        "height": 350,
        "legend": {
          "bgcolor": "rgba(240,240,240,1)",
          "font": {
            "color": "black"
          },
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.02,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "rangeselector": {
            "buttons": [
              {
                "count": 8.5,
                "label": "7d",
                "step": "day"
              },
              {
                "count": 15.5,
                "label": "14d",
                "step": "day"
              },
              {
                "count": 31.5,
                "label": "30d",
                "step": "day"
              },
              {
                "count": 1,
                "label": "MTD",
                "step": "month",
                "stepmode": "todate"
              },
              {
                "count": 1,
                "label": "YTD",
                "step": "year",
                "stepmode": "todate"
              }
            ],
            "visible": True,
            "x": 0.5,
            "xanchor": "center",
            "y": -0.25
          },
          "showline": False,
          "tickformat": "%m.%d",
          "ticks": "",
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.0f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "range": [
            800.0,
            3400.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$,",
          "tickprefix": " ",
          "ticks": "",
          "title": "",
          "zeroline": False
        },
        "yaxis2": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".1%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 2,
          "mirror": "",
          "nticks": 7,
          "overlaying": "y",
          "range": [
            0.0,
            0.44
          ],
          "showgrid": False,
          "showline": False,
          "side": "right",
          "tickformat": ".0%",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 8,
      "section": "time_series",
      "section_height": 350,
      "section_name": "2-Metric comparisons",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend|roas",
  },
  {
    "config": {
      "col": 2,
      "data": [
        {
          "close": [
            "675",
            "825",
            "811",
            "775",
            "864",
            "820",
            "865",
            "911",
            "952",
            "452",
            "750",
            "815",
            "875",
            "1044",
            "912",
            "850",
            "950",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "915"
          ],
          "decreasing": {
            "fillcolor": "#55D399",
            "line": {
              "color": "#29664A"
            }
          },
          "high": [
            "675",
            "825",
            "811",
            "775",
            "864",
            "820",
            "865",
            "911",
            "952",
            "452",
            "750",
            "815",
            "875",
            "1044",
            "912",
            "850",
            "950",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "915"
          ],
          "increasing": {
            "line": {
              "color": "rgba(255,0,0,1)"
            }
          },
          "line": {
            "color": "rgba(255,255,255,1)"
          },
          "low": [
            "675",
            "825",
            "811",
            "775",
            "864",
            "820",
            "865",
            "911",
            "952",
            "452",
            "750",
            "815",
            "875",
            "1044",
            "912",
            "850",
            "950",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "915"
          ],
          "open": [
            "675",
            "825",
            "811",
            "775",
            "864",
            "820",
            "865",
            "911",
            "952",
            "452",
            "750",
            "815",
            "875",
            "1044",
            "912",
            "850",
            "950",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "915"
          ],
          "type": "candlestick",
          "x": [
            "2017-05-01",
            "2017-05-02",
            "2017-05-03",
            "2017-05-04",
            "2017-05-05",
            "2017-05-06",
            "2017-05-07",
            "2017-05-08",
            "2017-05-09",
            "2017-05-10",
            "2017-05-11",
            "2017-05-12",
            "2017-05-13",
            "2017-05-14",
            "2017-05-15",
            "2017-05-16",
            "2017-05-17",
            "2017-05-18",
            "2017-05-19",
            "2017-05-20",
            "2017-05-21",
            "2017-05-22",
            "2017-05-23",
            "2017-05-24"
          ]
        }
      ],
      "field": "cost_per_conversion.candlestick",
      "layout": {
        "dragmode": "zoom",
        "height": 350,
        "legend": {
          "orientation": "h",
          "y": 1.1
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "plot_bgcolor": "rgba(220, 220, 220, 1)",
        "showlegend": False,
        "title": "CPUs across campaigns",
        "xaxis": {
          "gridcolor": "rgba(255, 255, 255, 1)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangeslider": [
            "2017-05-01",
            "2017-05-15"
          ],
          "showline": False,
          "tickformat": "%b-%d",
          "ticks": "",
          "tickvals": [
            "2017-05-01",
            "2017-05-08",
            "2017-05-15",
            "2017-05-22"
          ],
          "title": "report date",
          "type": "date",
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(255, 255, 255, 1)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "showline": False,
          "tickformat": ".1f",
          "tickprefix": " $",
          "ticks": "",
          "ticksuffix": " ",
          "title": "CPU",
          "zeroline": False
        }
      },
      "row": 8,
      "section": "candlestick",
      "section_height": 350,
      "section_name": "CPI distribution and trends",
      "section_open": False,
      "width": "100%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cost_per_conversion.candlestick",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "direction": "clockwise",
          "hole": 0.7,
          "hoverinfo": "label+percent+text",
          "insidetextfont": {
            "color": "white"
          },
          "labels": [
            "US",
            "GB",
            "CA",
            "AU",
            "BR",
            "DE",
            "FR",
            "IT"
          ],
          "marker": {
            "colors": [
              "rgba(68.086020000000005, 1.2428699999999999, 84.000825000000006, 255.0)",
              "rgba(45.242865000000002, 111.569385, 142.17907499999998, 255.0)",
              "rgba(71.291370000000001, 43.502744999999997, 122.399235, 255.0)",
              "rgba(59.568764999999999, 80.026139999999998, 138.69807, 255.0)",
              "rgba(35.753549999999997, 169.79404499999998, 130.92388499999998, 255.0)",
              "rgba(154.54147499999999, 216.936915, 60.361560000000004, 255.0)",
              "rgba(81.551294999999996, 196.58306999999999, 104.84376, 255.0)",
              "rgba(33.773220000000002, 140.81508000000002, 141.01958999999999, 255.0)"
            ],
            "colorscale": "Greens"
          },
          "name": "Spend by Country",
          "pull": 0,
          "rotation": -90,
          "showlegend": False,
          "sort": True,
          "textinfo": "label",
          "type": "pie",
          "values": [
            "3044",
            "912",
            "1850",
            "950",
            "440",
            "210",
            "275",
            "540"
          ],
          "hovertext": [
            "$3044",
            "$912",
            "$1850",
            "$950",
            "$440",
            "$210",
            "$275",
            "$540"
          ]
        }
      ],
      "field": "spend.pie:geo",
      "layout": {
        "height": 500,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(250, 250, 250, 1)",
        "title": "Spend by Country"
      },
      "row": 10,
      "section": "breakdown_pie",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend.pie:geo",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "direction": "clockwise",
          "hole": 0.7,
          "hoverformat": "$,.0f",
          "hoverinfo": "label+percent+value",
          "insidetextfont": {
            "color": "white"
          },
          "labels": [
            "US",
            "GB",
            "CA",
            "AU",
            "BR",
            "DE",
            "FR",
            "IT"
          ],
          "marker": {
            "colors": [
              "rgba(68.086020000000005, 1.2428699999999999, 84.000825000000006, 255.0)",
              "rgba(45.242865000000002, 111.569385, 142.17907499999998, 255.0)",
              "rgba(71.291370000000001, 43.502744999999997, 122.399235, 255.0)",
              "rgba(59.568764999999999, 80.026139999999998, 138.69807, 255.0)",
              "rgba(33.773220000000002, 140.81508000000002, 141.01958999999999, 255.0)",
              "rgba(81.551294999999996, 196.58306999999999, 104.84376, 255.0)",
              "rgba(154.54147499999999, 216.936915, 60.361560000000004, 255.0)",
              "rgba(35.753549999999997, 169.79404499999998, 130.92388499999998, 255.0)"
            ],
            "colorscale": "Greens"
          },
          "name": "New Users by Country",
          "pull": 0,
          "rotation": -90,
          "showlegend": False,
          "sort": True,
          "textinfo": "label",
          "type": "pie",
          "values": [
            "1024",
            "352",
            "650",
            "550",
            "240",
            "110",
            "75",
            "120"
          ]
        }
      ],
      "field": "unique_conversions.pie:geo",
      "layout": {
        "height": 500,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(250, 250, 250, 1)",
        "title": "New Users by Country"
      },
      "row": 10,
      "section": "breakdown_pie",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "unique_conversions.pie:geo",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "direction": "clockwise",
          "hole": 0.7,
          "hoverinfo": "label+percent+value",
          "insidetextfont": {
            "color": "white"
          },
          "labels": [
            "US",
            "GB",
            "CA",
            "AU",
            "BR",
            "DE",
            "FR",
            "IT"
          ],
          "marker": {
            "colors": [
              "rgba(68.086020000000005, 1.2428699999999999, 84.000825000000006, 255.0)",
              "rgba(35.753549999999997, 169.79404499999998, 130.92388499999998, 255.0)",
              "rgba(71.291370000000001, 43.502744999999997, 122.399235, 255.0)",
              "rgba(59.568764999999999, 80.026139999999998, 138.69807, 255.0)",
              "rgba(33.773220000000002, 140.81508000000002, 141.01958999999999, 255.0)",
              "rgba(45.242865000000002, 111.569385, 142.17907499999998, 255.0)",
              "rgba(81.551294999999996, 196.58306999999999, 104.84376, 255.0)",
              "rgba(154.54147499999999, 216.936915, 60.361560000000004, 255.0)"
            ],
            "colorscale": "Greens"
          },
          "name": "Revenues by Country",
          "pull": 0,
          "rotation": -90,
          "showlegend": False,
          "sort": True,
          "textinfo": "label",
          "type": "pie",
          "values": [
            "12024",
            "752",
            "6150",
            "3450",
            "2140",
            "2310",
            "750",
            "520"
          ]
        }
      ],
      "field": "purchase_value.pie:geo",
      "layout": {
        "height": 500,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(250, 250, 250, 1)",
        "title": "Revenues by Country"
      },
      "row": 10,
      "section": "breakdown_pie",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "purchase_value.pie:geo",
  },
  {
    "config": {
      "col": 4,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "direction": "clockwise",
          "hole": 0.7,
          "hoverinfo": "label+percent+text",
          "insidetextfont": {
            "color": "white"
          },
          "labels": [
            "CA",
            "FL",
            "TX",
            "NY",
            "PA",
            "OH",
            "MI",
            "IL",
            "WA",
            "NC",
            "GA",
            "WI",
            "VA",
            "MO",
            "MA",
            "AZ",
            "IN",
            "OR",
            "NJ",
            "TN",
            "CO",
            "MN",
            "MD",
            "KY",
            "SC",
            "OK",
            "UT",
            "IA",
            "AL",
            "KS",
            "CT",
            "LA",
            "ME",
            "AR",
            "NV",
            "NH",
            "NE",
            "ID",
            "NM",
            "WV",
            "MS",
            "MT",
            "RI",
            "VT",
            "HI",
            "SD",
            "DE",
            "WY",
            "AK",
            "ND",
            "DC"
          ],
          "marker": {
            "colors": []
          },
          "name": "Spend by US State",
          "pull": 0,
          "rotation": -90,
          "showlegend": False,
          "sort": True,
          "textinfo": "label",
          "type": "pie",
          "values": [
            "5011.46",
            "4127.69",
            "3744.88",
            "2947.4",
            "2833.95",
            "2562.14",
            "2404.15",
            "2111.15",
            "2082.93",
            "2005.56",
            "1657.09",
            "1626.15",
            "1616.09",
            "1537.65",
            "1508.11",
            "1435.31",
            "1422.72",
            "1376.21",
            "1246.39",
            "1201.56",
            "1193.33",
            "1098.62",
            "1011.24",
            "950.03",
            "809.94",
            "782.17",
            "777.9",
            "734.69",
            "726.04",
            "678.41",
            "648.55",
            "644.11",
            "596.35",
            "590.33",
            "567.4",
            "456.77",
            "453.44",
            "390.57",
            "383.37",
            "369.48",
            "282.98",
            "282.05",
            "276.83",
            "246.99",
            "225.43",
            "188.94",
            "177.87",
            "169.72",
            "156.71",
            "156.43",
            "96.79"
          ]
        }
      ],
      "field": "spend.pie:region",
      "layout": {
        "height": 500,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(250, 250, 250, 1)",
        "title": "Spend by US State"
      },
      "row": 10,
      "section": "breakdown_pie",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend.pie:region",
  },
  {
    "config": {
      "col": 5,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "direction": "clockwise",
          "hole": 0.7,
          "hoverinfo": "label+percent+value",
          "insidetextfont": {
            "color": "white"
          },
          "labels": [
            "CA",
            "TX",
            "FL",
            "NY",
            "PA",
            "IL",
            "MI",
            "OH",
            "NC",
            "GA",
            "MA",
            "VA",
            "WA",
            "NJ",
            "AZ",
            "MO",
            "CO",
            "WI",
            "MN",
            "TN",
            "OR",
            "IN",
            "MD",
            "SC",
            "KY",
            "CT",
            "OK",
            "AL",
            "LA",
            "UT",
            "KS",
            "IA",
            "AR",
            "NV",
            "HI",
            "NE",
            "ME",
            "NH",
            "WV",
            "ID",
            "MS",
            "NM",
            "RI",
            "DE",
            "DC",
            "VT",
            "MT",
            "AK",
            "ND",
            "SD",
            "WY"
          ],
          "marker": {
            "colors": []
          },
          "name": "New Users by US State",
          "pull": 0,
          "rotation": -90,
          "showlegend": False,
          "sort": True,
          "textinfo": "label",
          "type": "pie",
          "values": [
            "2102",
            "1788",
            "1658",
            "1410",
            "857",
            "736",
            "688",
            "686",
            "624",
            "573",
            "542",
            "537",
            "523",
            "501",
            "452",
            "439",
            "409",
            "401",
            "381",
            "370",
            "365",
            "351",
            "339",
            "290",
            "260",
            "210",
            "201",
            "199",
            "193",
            "192",
            "180",
            "176",
            "148",
            "137",
            "131",
            "126",
            "113",
            "103",
            "100",
            "98",
            "90",
            "89",
            "87",
            "67",
            "60",
            "58",
            "54",
            "41",
            "41",
            "40",
            "36"
          ]
        }
      ],
      "field": "unique_conversions.pie:region",
      "layout": {
        "height": 500,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(250, 250, 250, 1)",
        "title": "New Users by US State"
      },
      "row": 10,
      "section": "breakdown_pie",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "unique_conversions.pie:region",
  },
  {
    "config": {
      "col": 6,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "direction": "clockwise",
          "hole": 0.7,
          "hoverinfo": "label+percent+value",
          "insidetextfont": {
            "color": "white"
          },
          "labels": [
            "NY",
            "VA",
            "NC",
            "OH",
            "CA",
            "MO",
            "TN",
            "NJ",
            "MI",
            "IL",
            "MD",
            "FL",
            "MA",
            "PA",
            "OR",
            "RI",
            "UT",
            "WA",
            "DE",
            "MN",
            "HI",
            "IN",
            "CO",
            "TX",
            "WI",
            "OK",
            "NV",
            "AZ",
            "KY",
            "ID",
            "WY"
          ],
          "marker": {
            "colors": []
          },
          "name": "Revenues by US State",
          "pull": 0,
          "rotation": -90,
          "showlegend": False,
          "sort": True,
          "textinfo": "label",
          "type": "pie",
          "values": [
            "346",
            "297.5",
            "287.25",
            "145",
            "132",
            "120",
            "90",
            "90",
            "80",
            "80",
            "72",
            "68",
            "60",
            "56",
            "56",
            "50",
            "50",
            "50",
            "40",
            "40",
            "40",
            "36",
            "30",
            "26",
            "20",
            "20",
            "20",
            "20",
            "10",
            "10",
            "10"
          ]
        }
      ],
      "field": "purchase_value.pie:region",
      "layout": {
        "height": 500,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(250, 250, 250, 1)",
        "title": "Revenues by US State"
      },
      "row": 10,
      "section": "breakdown_pie",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "purchase_value.pie:region",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "orientation": "v",
          "type": "bar",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "14.12",
            "11.12",
            "11.969",
            "14.091",
            "12.883",
            "15.823",
            "13.883",
            "14.471",
            "17.434"
          ]
        }
      ],
      "field": "cpm:geo",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPM by Country",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "showline": False,
          "tickformat": "$.",
          "ticks": "",
          "tickwidth": 1,
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            10,
            18
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$,",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 11,
      "section": "breakdown_nonadd_bar",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cpm:geo",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "orientation": "v",
          "type": "bar",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "1.42",
            "1.22",
            "1.269",
            "1.391",
            "0.883",
            "1.823",
            "1.483",
            "1.571",
            "1.744"
          ]
        }
      ],
      "field": "cpc:geo",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPC by Country",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "showline": False,
          "tickformat": "$.1f",
          "ticks": "",
          "tickwidth": 1,
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.7,
            1.9
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$,.1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 11,
      "section": "breakdown_nonadd_bar",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cpc:geo",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "orientation": "v",
          "type": "bar",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "4.012",
            "3.012",
            "3.969",
            "4.091",
            "2.883",
            "5.823",
            "3.883",
            "4.471",
            "5.434"
          ]
        }
      ],
      "field": "cost_per_conversion:geo",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPU by Country",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "dtick": 1,
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "showline": False,
          "tickformat": "$.",
          "ticks": "",
          "tickwidth": 1,
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "anchor": "x",
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            2.4,
            6.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$,",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 11,
      "section": "breakdown_nonadd_bar",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cost_per_conversion:geo",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "hoverinfo": "x+y",
          "hovertext": [
            "California",
            "Florida",
            "Texas",
            "New York",
            "Pennsylvania",
            "Ohio",
            "Michigan",
            "Illinois",
            "Washington",
            "North Carolina",
            "Georgia",
            "Wisconsin",
            "Virginia",
            "Missouri",
            "Massachusetts",
            "Arizona",
            "Indiana",
            "Oregon",
            "New Jersey",
            "Tennessee",
            "Colorado",
            "Minnesota",
            "Maryland",
            "Kentucky",
            "South Carolina",
            "Oklahoma",
            "Utah",
            "Iowa",
            "Alabama",
            "Kansas",
            "Connecticut",
            "Louisiana",
            "Maine",
            "Arkansas",
            "Nevada",
            "New Hampshire",
            "Nebraska",
            "Idaho",
            "New Mexico",
            "West Virginia",
            "Mississippi",
            "Montana",
            "Rhode Island",
            "Vermont",
            "Hawaii",
            "South Dakota",
            "Delaware",
            "Wyoming",
            "Alaska",
            "North Dakota",
            "District of Columbia"
          ],
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "orientation": "v",
          "type": "bar",
          "x": [
            "CA",
            "FL",
            "TX",
            "NY",
            "PA",
            "OH",
            "MI",
            "IL",
            "WA",
            "NC",
            "GA",
            "WI",
            "VA",
            "MO",
            "MA",
            "AZ",
            "IN",
            "OR",
            "NJ",
            "TN",
            "CO",
            "MN",
            "MD",
            "KY",
            "SC",
            "OK",
            "UT",
            "IA",
            "AL",
            "KS",
            "CT",
            "LA",
            "ME",
            "AR",
            "NV",
            "NH",
            "NE",
            "ID",
            "NM",
            "WV",
            "MS",
            "MT",
            "RI",
            "VT",
            "HI",
            "SD",
            "DE",
            "WY",
            "AK",
            "ND",
            "DC"
          ],
          "y": [
            2.683053125,
            2.6562298232129,
            2.6542377919321,
            2.6820641827577,
            2.6513788221971,
            2.6253104993598,
            2.6338241239892,
            2.6342724097788,
            2.6245688646118,
            2.6562550443906,
            2.706878198567,
            2.635206527282,
            2.6638523274478,
            2.6531758957655,
            2.6614254385965,
            2.6367439231204,
            2.6312542759407,
            2.6588066825776,
            2.6857208387942,
            2.6384910655195,
            2.6047181208054,
            2.6495775623269,
            2.7040349344978,
            2.6272881355932,
            2.6849794238683,
            2.6753426124197,
            2.6377187153931,
            2.6355542725173,
            2.6377546296296,
            2.625041322314,
            2.6682208588957,
            2.6339240506329,
            2.5933134328358,
            2.608895612708,
            2.6340797546012,
            2.6505263157895,
            2.5938475836431,
            2.587519379845,
            2.6704782608696,
            2.6153995680346,
            2.6773055555556,
            2.5700828729282,
            2.725875,
            2.6184713375796,
            2.6886363636364,
            2.6971369294606,
            2.6067592592593,
            2.6288571428571,
            2.5581395348837,
            2.6577840909091,
            2.6538655462185
          ]
        }
      ],
      "field": "cpm_us_region",
      "layout": {
        "autosize": True,
        "bargap": 0.2,
        "bargroupgap": 0.2,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPM by US State",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "showline": False,
          "ticks": "",
          "tickwidth": 1,
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            2.52,
            2.74
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$,.1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 12,
      "section": "breakdown_nonadd_bar",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cpm:region",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "hoverinfo": "x+y",
          "hovertext": [
            "California",
            "Florida",
            "Texas",
            "New York",
            "Pennsylvania",
            "Ohio",
            "Michigan",
            "Illinois",
            "Washington",
            "North Carolina",
            "Georgia",
            "Wisconsin",
            "Virginia",
            "Missouri",
            "Massachusetts",
            "Arizona",
            "Indiana",
            "Oregon",
            "New Jersey",
            "Tennessee",
            "Colorado",
            "Minnesota",
            "Maryland",
            "Kentucky",
            "South Carolina",
            "Oklahoma",
            "Utah",
            "Iowa",
            "Alabama",
            "Kansas",
            "Connecticut",
            "Louisiana",
            "Maine",
            "Arkansas",
            "Nevada",
            "New Hampshire",
            "Nebraska",
            "Idaho",
            "New Mexico",
            "West Virginia",
            "Mississippi",
            "Montana",
            "Rhode Island",
            "Vermont",
            "Hawaii",
            "South Dakota",
            "Delaware",
            "Wyoming",
            "Alaska",
            "North Dakota",
            "District of Columbia"
          ],
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "orientation": "v",
          "type": "bar",
          "x": [
            "CA",
            "FL",
            "TX",
            "NY",
            "PA",
            "OH",
            "MI",
            "IL",
            "WA",
            "NC",
            "GA",
            "WI",
            "VA",
            "MO",
            "MA",
            "AZ",
            "IN",
            "OR",
            "NJ",
            "TN",
            "CO",
            "MN",
            "MD",
            "KY",
            "SC",
            "OK",
            "UT",
            "IA",
            "AL",
            "KS",
            "CT",
            "LA",
            "ME",
            "AR",
            "NV",
            "NH",
            "NE",
            "ID",
            "NM",
            "WV",
            "MS",
            "MT",
            "RI",
            "VT",
            "HI",
            "SD",
            "DE",
            "WY",
            "AK",
            "ND",
            "DC"
          ],
          "y": [
            "1.42",
            "1.22",
            "1.269",
            "1.391",
            "0.883",
            "1.823",
            "1.483",
            "1.571",
            "1.744",
            "1.42",
            "1.22",
            "1.269",
            "1.391",
            "0.883",
            "1.823",
            "1.483",
            "1.571",
            "1.744",
            "1.42",
            "1.22",
            "1.269",
            "1.391",
            "0.883",
            "1.823",
            "1.483",
            "1.571",
            "1.744",
            "1.42",
            "1.22",
            "1.269",
            "1.391",
            "0.883",
            "1.823",
            "1.483",
            "1.571",
            "1.744",
            "1.42",
            "1.22",
            "1.269",
            "1.391",
            "0.883",
            "1.823",
            "1.483",
            "1.571",
            "1.744",
            "1.42",
            "1.22",
            "1.269",
            "1.391",
            "0.883",
            "1.823"
          ]
        }
      ],
      "field": "cpc_us_region",
      "layout": {
        "autosize": True,
        "bargap": 0.2,
        "bargroupgap": 0.2,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPC by US State",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "showline": False,
          "ticks": "",
          "tickwidth": 1,
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.7,
            1.9
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$,.1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 12,
      "section": "breakdown_nonadd_bar",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cpc:region",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "hoverinfo": "x+y",
          "hovertext": [
            "California",
            "Florida",
            "Texas",
            "New York",
            "Pennsylvania",
            "Ohio",
            "Michigan",
            "Illinois",
            "Washington",
            "North Carolina",
            "Georgia",
            "Wisconsin",
            "Virginia",
            "Missouri",
            "Massachusetts",
            "Arizona",
            "Indiana",
            "Oregon",
            "New Jersey",
            "Tennessee",
            "Colorado",
            "Minnesota",
            "Maryland",
            "Kentucky",
            "South Carolina",
            "Oklahoma",
            "Utah",
            "Iowa",
            "Alabama",
            "Kansas",
            "Connecticut",
            "Louisiana",
            "Maine",
            "Arkansas",
            "Nevada",
            "New Hampshire",
            "Nebraska",
            "Idaho",
            "New Mexico",
            "West Virginia",
            "Mississippi",
            "Montana",
            "Rhode Island",
            "Vermont",
            "Hawaii",
            "South Dakota",
            "Delaware",
            "Wyoming",
            "Alaska",
            "North Dakota",
            "District of Columbia"
          ],
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "orientation": "v",
          "type": "bar",
          "x": [
            "CA",
            "FL",
            "TX",
            "NY",
            "PA",
            "OH",
            "MI",
            "IL",
            "WA",
            "NC",
            "GA",
            "WI",
            "VA",
            "MO",
            "MA",
            "AZ",
            "IN",
            "OR",
            "NJ",
            "TN",
            "CO",
            "MN",
            "MD",
            "KY",
            "SC",
            "OK",
            "UT",
            "IA",
            "AL",
            "KS",
            "CT",
            "LA",
            "ME",
            "AR",
            "NV",
            "NH",
            "NE",
            "ID",
            "NM",
            "WV",
            "MS",
            "MT",
            "RI",
            "VT",
            "HI",
            "SD",
            "DE",
            "WY",
            "AK",
            "ND",
            "DC"
          ],
          "y": [
            2.683053125,
            2.6562298232129,
            2.6542377919321,
            2.6820641827577,
            2.6513788221971,
            2.6253104993598,
            2.6338241239892,
            2.6342724097788,
            2.6245688646118,
            2.6562550443906,
            2.706878198567,
            2.635206527282,
            2.6638523274478,
            2.6531758957655,
            2.6614254385965,
            2.6367439231204,
            2.6312542759407,
            2.6588066825776,
            2.6857208387942,
            2.6384910655195,
            2.6047181208054,
            2.6495775623269,
            2.7040349344978,
            2.6272881355932,
            2.6849794238683,
            2.6753426124197,
            2.6377187153931,
            2.6355542725173,
            2.6377546296296,
            2.625041322314,
            2.6682208588957,
            2.6339240506329,
            2.5933134328358,
            2.608895612708,
            2.6340797546012,
            2.6505263157895,
            2.5938475836431,
            2.587519379845,
            2.6704782608696,
            2.6153995680346,
            2.6773055555556,
            2.5700828729282,
            2.725875,
            2.6184713375796,
            2.6886363636364,
            2.6971369294606,
            2.6067592592593,
            2.6288571428571,
            2.5581395348837,
            2.6577840909091,
            2.6538655462185
          ]
        }
      ],
      "field": "cpu_us_region",
      "layout": {
        "autosize": True,
        "bargap": 0.2,
        "bargroupgap": 0.2,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPU by US State",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "showline": False,
          "ticks": "",
          "tickwidth": 1,
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            2.52,
            2.74
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$,.1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 12,
      "section": "breakdown_nonadd_bar",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cost_per_conversion:region",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "fill": "none",
          "fillcolor": "rgba(248, 76, 141, 0.8)",
          "hoverinfo": "y+x",
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "CTR",
          "orientation": "y",
          "type": "scatter",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "1.01",
            "1.12",
            "1.269",
            "1.091",
            "1.883",
            "1.023",
            "1.183",
            "0.971",
            "0.934"
          ]
        },
        {
          "fill": "none",
          "fillcolor": "rgba(188, 91, 248, 0.8)",
          "hoverinfo": "y+x",
          "line": {
            "color": "#41A074",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#41A074",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "CVR",
          "type": "scatter",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "46.62",
            "45.12",
            "41.269",
            "38.091",
            "51.883",
            "40.023",
            "45.183",
            "48.971",
            "47.934"
          ],
          "yaxis": "y2"
        }
      ],
      "field": "ctr_cvr_country",
      "layout": {
        "autosize": True,
        "barmode": "group",
        "height": 350,
        "legend": {
          "bgcolor": "rgba(240,240,240,1)",
          "font": {
            "color": "black"
          },
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.02,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "",
        "xaxis": {
          "anchor": "y",
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        },
        "yaxis": {
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.8,
            2.7
          ],
          "rangemode": "tozero",
          "showline": False,
          "side": "bottom",
          "tick0": 0.5,
          "tickformat": ".1f",
          "ticks": "",
          "ticksuffix": "% ",
          "tickwidth": 1,
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis2": {
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "overlaying": "y",
          "range": [
            24.0,
            54.0
          ],
          "rangemode": "tozero",
          "showgrid": False,
          "showline": False,
          "showticklabels ": False,
          "side": "right",
          "tick0": 0.5,
          "tickformat": ".1f",
          "ticks": "",
          "ticksuffix": "% ",
          "tickwidth": 1,
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 13,
      "section": "breakdown_nonadd_line",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "ctr|cvr:geo",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "fill": "none",
          "fillcolor": "rgba(255, 0, 0, 1)",
          "hoverinfo": "y+x",
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "payer-CVR",
          "type": "scatter",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "3.62",
            "3.12",
            "3.269",
            "3.091",
            "2.883",
            "5.023",
            "4.183",
            "4.371",
            "5.234"
          ]
        },
        {
          "fill": "none",
          "fillcolor": "rgba(65,135,48,1)",
          "hoverinfo": "y+x",
          "line": {
            "color": "#41A074",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#41A074",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "ROAS",
          "type": "scatter",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "14.62",
            "7.12",
            "13.269",
            "14.091",
            "19.883",
            "25.023",
            "8.183",
            "11.371",
            "18.234"
          ],
          "yaxis": "y2"
        }
      ],
      "field": "payer_cvr_roas_country",
      "layout": {
        "autosize": True,
        "barmode": "group",
        "height": 350,
        "legend": {
          "bgcolor": "rgba(240,240,240,1)",
          "font": {
            "color": "black"
          },
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.02,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "",
        "xaxis": {
          "anchor": "y",
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        },
        "yaxis": {
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".2%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            2.6,
            7.2
          ],
          "rangemode": "tozero",
          "showline": False,
          "side": "bottom",
          "tick0": 0.5,
          "tickfont": {
            "color": "black"
          },
          "tickformat": ".1%",
          "ticks": "",
          "ticksuffix": " ",
          "tickwidth": 1,
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis2": {
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".2%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "overlaying": "y",
          "range": [
            0.0,
            28.0
          ],
          "rangemode": "tozero",
          "showgrid": False,
          "showline": False,
          "side": "right",
          "tick0": 0.5,
          "tickformat": ".1%",
          "ticks": "",
          "ticksuffix": " ",
          "tickwidth": 1,
          "title": "",
          "zeroline": False
        }
      },
      "row": 13,
      "section": "breakdown_nonadd_line",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "payer_cvr|roas:geo",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "fill": "none",
          "fillcolor": "rgba(84,122,251,1)",
          "hoverformat": "$.2f",
          "hoverinfo": "y+x",
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "ARPU",
          "type": "scatter",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "11.62",
            "7.12",
            "8.269",
            "9.091",
            "7.883",
            "15.023",
            "11.183",
            "12.371",
            "13.234"
          ]
        },
        {
          "fill": "none",
          "fillcolor": "rgba(68,225,138,1)",
          "hoverinfo": "y+x",
          "line": {
            "color": "#41A074",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#41A074",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "lines+markers",
          "name": "ARPPU",
          "type": "scatter",
          "x": [
            "WW",
            "IT",
            "FR",
            "DE",
            "BR",
            "AU",
            "GB",
            "CA",
            "US"
          ],
          "y": [
            "24.62",
            "16.12",
            "18.269",
            "20.091",
            "25.883",
            "35.023",
            "24.183",
            "23.371",
            "27.234"
          ],
          "yaxis": "y2"
        }
      ],
      "field": "arpu_arppu_country",
      "layout": {
        "annotations": [],
        "autosize": True,
        "barmode": "group",
        "height": 350,
        "legend": {
          "bgcolor": "rgba(240,240,240,1)",
          "font": {
            "color": "black"
          },
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.02,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "",
        "xaxis": {
          "anchor": "y",
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "ticks": "",
          "ticksuffix": " ",
          "title": "",
          "zeroline": False
        },
        "yaxis": {
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            6,
            22
          ],
          "rangemode": "tozero",
          "showline": False,
          "side": "bottom",
          "tick0": 0.5,
          "tickformat": "$,.2f",
          "ticks": "",
          "ticksuffix": "",
          "tickwidth": 1,
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis2": {
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "overlaying": "y",
          "range": [
            0.0,
            38.0
          ],
          "rangemode": "tozero",
          "showgrid": False,
          "showline": False,
          "side": "right",
          "tick0": 0.5,
          "tickformat": "$,",
          "ticks": "",
          "ticksuffix": "",
          "tickwidth": 1,
          "title": "",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 13,
      "section": "breakdown_nonadd_line",
      "section_height": 2048,
      "section_name": "Breakdowns",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "arpu|arppu:geo",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "white",
            "line": {
              "color": "#327BD1",
              "width": 1.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "markers",
          "name": "data",
          "showlegend": False,
          "type": "scatter",
          "x": [
            "675",
            "825",
            "811",
            "775",
            "864",
            "820",
            "865",
            "911",
            "952",
            "452",
            "750",
            "815",
            "875",
            "1044",
            "912",
            "850",
            "950",
            "1040",
            "1010",
            "975",
            "1040",
            "1010",
            "975",
            "915"
          ],
          "y": [
            "3.434",
            "4.883",
            "3.471",
            "4.123",
            "4.883",
            "5.091",
            "4.969",
            "4.12",
            "4.711",
            "5.091",
            "3.706",
            "4.046",
            "4.494",
            "4.483",
            "3.583",
            "4.146",
            "3.609",
            "4.726",
            "4.414",
            "3.637",
            "5.014",
            "5.066",
            "4.2",
            "3.52"
          ]
        }
      ],
      "field": "spend_cpu_scatter",
      "layout": {
        "autosize": True,
        "height": 350,
        "legend": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.0,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "[Spend / CPU] correlation",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 0,
          "mirror": "",
          "nticks": 7,
          "range": [
            300,
            1100
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$,0.f",
          "ticks": "",
          "title": "daily spend",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 0,
          "mirror": "",
          "nticks": 7,
          "range": [
            3.0,
            5.2
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$.1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": "CPU",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 15,
      "section": "correlations",
      "section_height": 700,
      "section_name": "Correlation analysis",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend|cost_per_conversion.scatter",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "white",
            "line": {
              "color": "#327BD1",
              "width": 1.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "markers",
          "name": "data",
          "showlegend": False,
          "type": "scatter",
          "x": [
            "0.05",
            "0.045",
            "0.043",
            "0.04",
            "0.043",
            "0.044",
            "0.043",
            "0.04",
            "0.039",
            "0.039",
            "0.035",
            "0.033",
            "0.033",
            "0.03",
            "0.029",
            "0.032",
            "0.03",
            "0.033",
            "0.033",
            "0.033",
            "0.034",
            "0.037",
            "0.038",
            "0.036"
          ],
          "y": [
            "3.434",
            "4.883",
            "3.471",
            "4.123",
            "4.883",
            "5.091",
            "4.969",
            "4.12",
            "4.711",
            "5.091",
            "3.706",
            "4.046",
            "4.494",
            "4.483",
            "3.583",
            "4.146",
            "3.609",
            "4.726",
            "4.414",
            "3.637",
            "5.014",
            "5.066",
            "4.2",
            "3.52"
          ]
        }
      ],
      "field": "payer_cvr_cpu_scatter",
      "layout": {
        "autosize": True,
        "height": 350,
        "legend": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.0,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "[Payer-CVR / CPU] correlation",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".2%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.02,
            0.05
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".1%",
          "ticks": "",
          "title": "payer-CVR",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$.2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            3.0,
            5.2
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$.1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": "CPU",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 15,
      "section": "correlations",
      "section_height": 700,
      "section_name": "Correlation analysis",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "payer_cvr|cost_per_conversion.scatter",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "white",
            "line": {
              "color": "#327BD1",
              "width": 1.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "markers",
          "name": "data",
          "showlegend": False,
          "type": "scatter",
          "x": [
            "221.94",
            "234.21",
            "198.15",
            "264.17",
            "237.59",
            "181.44",
            "178.42",
            "202.62",
            "243.45",
            "215.78",
            "213.83",
            "260.07",
            "187.32",
            "269.3",
            "274.63",
            "245.12",
            "243.42",
            "193.63",
            "275.76",
            "222.74",
            "279.91",
            "293.13",
            "250.98",
            "290.63"
          ],
          "y": [
            "43.58",
            "43.75",
            "42.88",
            "32.88",
            "53.28",
            "40.15",
            "32.6",
            "43.46",
            "70.89",
            "31.22",
            "36.53",
            "48.9",
            "46",
            "58.45",
            "49.57",
            "38.51",
            "66.26",
            "44.52",
            "48.51",
            "52.9",
            "46.76",
            "50.73",
            "44.42",
            "48.01"
          ]
        }
      ],
      "field": "cppu|arppu.scatter",
      "layout": {
        "autosize": True,
        "height": 350,
        "legend": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.0,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "[CPP / ARPPU] correlation",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            160.0,
            300.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$.1 ",
          "ticks": "",
          "title": "CPP",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$.1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            20,
            80
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": "$ ",
          "ticks": "",
          "ticksuffix": " ",
          "title": "ARPPU",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 15,
      "section": "correlations",
      "section_height": 700,
      "section_name": "Correlation analysis",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cppu|arppu.scatter",
  },
  {
    "config": {
      "col": 4,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "white",
            "line": {
              "color": "#327BD1",
              "width": 1.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "markers",
          "name": "Frequency",
          "showlegend": False,
          "type": "scatter",
          "x": [
            "1",
            "1.13",
            "1.14",
            "1.19",
            "1.11",
            "1.23",
            "1.38",
            "1.45",
            "1.53",
            "1.54",
            "1.66",
            "1.62",
            "1.68",
            "1.62",
            "1.57",
            "1.65",
            "1.7",
            "1.8",
            "1.77",
            "1.8",
            "1.89",
            "1.81",
            "1.86",
            "1.87"
          ],
          "y": [
            "0.05",
            "0.045",
            "0.043",
            "0.04",
            "0.043",
            "0.044",
            "0.043",
            "0.04",
            "0.039",
            "0.039",
            "0.035",
            "0.033",
            "0.033",
            "0.03",
            "0.029",
            "0.032",
            "0.03",
            "0.033",
            "0.033",
            "0.033",
            "0.034",
            "0.037",
            "0.038",
            "0.036"
          ]
        }
      ],
      "field": "frequency|payer_cvr.scatter",
      "layout": {
        "autosize": True,
        "height": 350,
        "hoverinfo": "x+y",
        "legend": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.0,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "[Frequency / Payer-CVR] correlation",
        "xaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".2f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.8,
            2.0
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": ".1f",
          "ticks": "",
          "ticksuffix": " ",
          "title": "frequency",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "'Droid Sans',Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ",.1%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.02,
            0.05
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".0%",
          "ticks": "",
          "title": "payer-CVR",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 15,
      "section": "correlations",
      "section_height": 700,
      "section_name": "Correlation analysis",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "frequency|payer_cvr.scatter",
  },
  {
    "config": {
      "col": 5,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "white",
            "line": {
              "color": "#327BD1",
              "width": 1.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "markers",
          "name": "data",
          "showlegend": False,
          "type": "scatter",
          "x": [
            "3.434",
            "4.883",
            "3.471",
            "4.123",
            "4.883",
            "5.091",
            "4.969",
            "4.12",
            "4.711",
            "5.091",
            "3.706",
            "4.046",
            "4.494",
            "4.483",
            "3.583",
            "4.146",
            "3.609",
            "4.726",
            "4.414",
            "3.637",
            "5.014",
            "5.066",
            "4.2",
            "3.52"
          ],
          "y": [
            "0.178",
            "0.211",
            "0.103",
            "0.119",
            "0.134",
            "0.204",
            "0.212",
            "0.309",
            "0.357",
            "0.197",
            "0.143",
            "0.165",
            "0.338",
            "0.233",
            "0.257",
            "0.161",
            "0.327",
            "0.171",
            "0.297",
            "0.29",
            "0.399",
            "0.259",
            "0.277",
            "0.253"
          ]
        }
      ],
      "field": "cpu|roas.scatter",
      "layout": {
        "autosize": True,
        "height": 350,
        "legend": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.0,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "[CPU / ROAS] correlation",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": "$,.1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            3.0,
            5.2
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": "$.1 ",
          "ticks": "",
          "title": "CPU",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".1%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.04,
            0.42
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": ".0% ",
          "ticks": "",
          "ticksuffix": " ",
          "title": "ROAS",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 15,
      "section": "correlations",
      "section_height": 700,
      "section_name": "Correlation analysis",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cost_per_conversion|roas.scatter",
  },
  {
    "config": {
      "col": 6,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "white",
            "line": {
              "color": "#327BD1",
              "width": 1.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "mode": "markers",
          "name": "data",
          "showlegend": False,
          "type": "scatter",
          "x": [
            "0.05",
            "0.045",
            "0.043",
            "0.04",
            "0.043",
            "0.044",
            "0.043",
            "0.04",
            "0.039",
            "0.039",
            "0.035",
            "0.033",
            "0.033",
            "0.03",
            "0.029",
            "0.032",
            "0.03",
            "0.033",
            "0.033",
            "0.033",
            "0.034",
            "0.037",
            "0.038",
            "0.036"
          ],
          "y": [
            "0.178",
            "0.211",
            "0.103",
            "0.119",
            "0.134",
            "0.204",
            "0.212",
            "0.309",
            "0.357",
            "0.197",
            "0.143",
            "0.165",
            "0.338",
            "0.233",
            "0.257",
            "0.161",
            "0.327",
            "0.171",
            "0.297",
            "0.29",
            "0.399",
            "0.259",
            "0.277",
            "0.253"
          ]
        }
      ],
      "field": "payer_cvr|roas.scatter",
      "layout": {
        "autosize": True,
        "height": 350,
        "legend": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "orientation": "h",
          "x": 0.5,
          "xanchor": "center",
          "y": 1.0,
          "yanchor": "bottom"
        },
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": True,
        "title": "[Payer-CVR / ROAS] correlation",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".1%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.02,
            0.05
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".0% ",
          "ticks": "",
          "title": "payer-CVR",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "hoverformat": ".1%",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "nticks": 7,
          "range": [
            0.04,
            0.42
          ],
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": ".0% ",
          "ticks": "",
          "ticksuffix": " ",
          "title": "ROAS",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        }
      },
      "row": 15,
      "section": "correlations",
      "section_height": 700,
      "section_name": "Correlation analysis",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "payer_cvr|roas.scatter",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "autobinx": False,
          "histfunc": "count",
          "histnorm": "percent",
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "type": "histogram",
          "x": [
            "2.309959",
            "1.731346",
            "1.831723",
            "1.797838",
            "1.565591",
            "1.366954",
            "1.38205",
            "1.831723",
            "1.797838",
            "1.565591",
            "1.366954",
            "1.38205",
            "2.309959",
            "1.731346",
            "1.831723",
            "1.797838",
            "2.309959",
            "1.731346",
            "1.831723",
            "1.366954",
            "1.38205",
            "1.831723",
            "1.797838",
            "1.565591"
          ],
          "xbins": {
            "end": 2.5,
            "size": 0.2,
            "start": 0.5
          },
          "y": []
        }
      ],
      "field": "ctr.histogram",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CTR distribution",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1.0,
          "hoverformat": ".1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "range": [
            0,
            3
          ],
          "rangemode": "normal",
          "showline": False,
          "tickformat": ".0f",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "CTR",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1.0,
          "hoverformat": ".1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": ".0f",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 16,
      "section": "distributions",
      "section_height": 350,
      "section_name": "Metric distributions",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "ctr.histogram",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "autobinx": False,
          "histfunc": "count",
          "histnorm": "percent",
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "type": "histogram",
          "x": [
            "3.434",
            "4.883",
            "3.471",
            "4.123",
            "4.883",
            "5.091",
            "4.969",
            "4.12",
            "4.711",
            "5.091",
            "3.706",
            "4.046",
            "4.494",
            "4.483",
            "3.583",
            "4.146",
            "3.609",
            "4.726",
            "4.414",
            "3.637",
            "5.014",
            "5.066",
            "4.2",
            "3.52"
          ],
          "xbins": {
            "end": 8,
            "size": 0.25,
            "start": 2
          },
          "y": []
        }
      ],
      "field": "cost_per_conversion.histogram",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "CPU distribution",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1.0,
          "hoverformat": "$.1 ",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "range": [
            0,
            8
          ],
          "rangemode": "normal",
          "showline": False,
          "tickformat": "$.0 ",
          "ticks": "",
          "title": "CPU",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1.0,
          "hoverformat": ".1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".0f",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 16,
      "section": "distributions",
      "section_height": 350,
      "section_name": "Metric distributions",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "cost_per_conversion.histogram",
  },
  {
    "config": {
      "col": 3,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "autobinx": False,
          "histfunc": "count",
          "histnorm": "percent",
          "line": {
            "color": "#327BD1",
            "shape": "spline",
            "smoothing": 1,
            "width": 1.5
          },
          "marker": {
            "color": "#327BD1",
            "line": {
              "color": "black",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "type": "histogram",
          "x": [
            "0.05",
            "0.045",
            "0.043",
            "0.04",
            "0.043",
            "0.044",
            "0.043",
            "0.04",
            "0.039",
            "0.039",
            "0.035",
            "0.033",
            "0.033",
            "0.03",
            "0.029",
            "0.032",
            "0.03",
            "0.033",
            "0.033",
            "0.033",
            "0.034",
            "0.037",
            "0.038",
            "0.036"
          ],
          "xbins": {
            "end": 0.08,
            "size": 0.002,
            "start": 0.02
          },
          "y": [
            "0.5",
            "0.45",
            "0.43",
            "0.4",
            "0.43",
            "0.44",
            "0.43",
            "0.04",
            "0.039",
            "0.039",
            "0.035",
            "0.033",
            "0.033",
            "0.03",
            "0.029",
            "0.032",
            "0.03",
            "0.033",
            "0.033",
            "0.033",
            "0.034",
            "0.037",
            "0.038",
            "0.036"
          ]
        }
      ],
      "field": "payer_cvr.histogram",
      "layout": {
        "autosize": True,
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "rgba(255, 255, 255, 1)",
        "showlegend": False,
        "title": "Payer-CVR distribution",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1.0,
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "range": [
            0,
            0.08
          ],
          "rangemode": "tozero",
          "showline": False,
          "tickformat": ".0% ",
          "ticks": "",
          "title": "Payer-CVR",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(200, 200, 200, 0.5)",
          "gridwidth": 1.0,
          "hoverformat": ".1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": ".0f",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 16,
      "section": "distributions",
      "section_height": 350,
      "section_name": "Metric distributions",
      "section_open": False,
      "width": "33.3%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "payer_cvr.histogram",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "tickformat": "$,",
            "title": "Spend",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(240,240,240)"
            ],
            [
              0.2,
              "rgb(210,210,210)"
            ],
            [
              0.4,
              "rgb(190,190,190)"
            ],
            [
              0.6,
              "rgb(150,150,150)"
            ],
            [
              0.8,
              "rgb(120,120,120)"
            ],
            [
              1,
              "rgb(90,90,90)"
            ]
          ],
          "hoverformat": "$,.1f",
          "hoverinfo": "z+location",
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "ISO-3",
          "locations": [
            "USA",
            "CAN",
            "GBR",
            "BGR",
            "LVA",
            "EGY",
            "GUM",
            "MYS",
            "RUS",
            "FRA",
            "TWN",
            "BRA",
            "COL",
            "DEU",
            "JAM",
            "IRL",
            "MEX"
          ],
          "marker": {
            "color": "",
            "line": {
              "color": "",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "US",
            "CA",
            "GB",
            "BG",
            "LV",
            "EG",
            "GU",
            "MY",
            "RU",
            "FR",
            "TW",
            "BR",
            "CO",
            "DE",
            "JM",
            "IE",
            "MX"
          ],
          "type": "choropleth",
          "z": [
            "4260.07",
            "4024.64",
            "4007.04",
            "3940.29",
            "3647.24",
            "3835.88",
            "3704.38",
            "3219.47",
            "3304.43",
            "3041.06",
            "3157.67",
            "2831.63",
            "2974.77",
            "2756.12",
            "2729.09",
            "2672.56",
            "2798.7"
          ]
        }
      ],
      "field": "spend.map:geo",
      "layout": {
        "autosize": True,
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "lataxis": {
            "range": [
              -55,
              90
            ],
            "showgrid": False,
            "showline": True
          },
          "lonaxis": {},
          "projection": {
            "rotation": {
              "lon": 0
            },
            "type": "miller"
          },
          "scope": "world",
          "showframe": False,
          "showlakes": True,
          "showland": False,
          "showrivers": False,
          "showsubunits": False,
          "subunitcolor": "rgba(0, 0, 255, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "Spend by country",
        "yaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        }
      },
      "row": 17,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend.map:geo",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "tickformat": "$,",
            "title": "Spend",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(240,240,240)"
            ],
            [
              0.2,
              "rgb(210,210,210)"
            ],
            [
              0.4,
              "rgb(190,190,190)"
            ],
            [
              0.6,
              "rgb(150,150,150)"
            ],
            [
              0.8,
              "rgb(120,120,120)"
            ],
            [
              1,
              "rgb(90,90,90)"
            ]
          ],
          "hoverinfo": "z+location",
          "hovertext": [
            "California",
            "Florida",
            "Texas",
            "Pennsylvania",
            "New York",
            "Ohio",
            "Michigan",
            "Washington",
            "North Carolina",
            "Illinois",
            "Wisconsin",
            "Georgia",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
          ],
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "USA-states",
          "locations": [
            "CA",
            "FL",
            "TX",
            "PA",
            "NY",
            "OH",
            "MI",
            "WA",
            "NC",
            "IL",
            "WI",
            "GA",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY"
          ],
          "marker": {
            "line": {
              "color": "rgba(1, 1, 1, 1)",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "California",
            "Florida",
            "Texas",
            "Pennsylvania",
            "New York",
            "Ohio",
            "Michigan",
            "Washington",
            "North Carolina",
            "Illinois",
            "Wisconsin",
            "Georgia",
            "Virginia",
            "Arizona",
            "Massachusetts",
            "Indiana",
            "Oregon",
            "Missouri",
            "Tennessee",
            "Minnesota",
            "New Jersey",
            "Colorado",
            "Maryland",
            "Kentucky",
            "South Carolina",
            "Oklahoma",
            "Iowa",
            "Kansas",
            "Alabama",
            "Utah",
            "Louisiana",
            "Connecticut",
            "Nevada",
            "Maine",
            "Arkansas",
            "Idaho",
            "New Hampshire",
            "Nebraska",
            "West Virginia",
            "New Mexico",
            "Mississippi",
            "Montana",
            "Rhode Island",
            "Vermont",
            "Hawaii",
            "South Dakota",
            "Delaware",
            "Wyoming",
            "North Dakota",
            "Alaska",
            "District of Columbia"
          ],
          "type": "choropleth",
          "z": [
            "5011.46",
            "4127.69",
            "3744.88",
            "2947.4",
            "2833.95",
            "2562.14",
            "2404.15",
            "2111.15",
            "2082.93",
            "2005.56",
            "1657.09",
            "1626.15",
            "1616.09",
            "1537.65",
            "1508.11",
            "1435.31",
            "1422.72",
            "1376.21",
            "1246.39",
            "1201.56",
            "1193.33",
            "1098.62",
            "1011.24",
            "950.03",
            "809.94",
            "782.17",
            "777.9",
            "734.69",
            "726.04",
            "678.41",
            "648.55",
            "644.11",
            "596.35",
            "590.33",
            "567.4",
            "456.77",
            "453.44",
            "390.57",
            "383.37",
            "369.48",
            "282.98",
            "282.05",
            "276.83",
            "246.99",
            "225.43",
            "188.94",
            "177.87",
            "169.72",
            "156.71",
            "156.43",
            "96.79"
          ]
        }
      ],
      "field": "spend.map:region",
      "layout": {
        "autosize": True,
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "coastlinecolor": "rgba(0, 0, 0, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "red",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "landcolor": "rgba(0, 255, 0, 1)",
          "lataxis": {},
          "lonaxis": {},
          "oceancolor": "rgba(137, 203, 255, 1)",
          "scope": "usa",
          "showcoastlines": True,
          "showframe": True,
          "showlakes": True,
          "showland": False,
          "showocean": True,
          "showrivers": True,
          "showsubunits": True,
          "subunitcolor": "rgba(0, 0, 0, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "Spend by US state",
        "xaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        },
        "yaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        }
      },
      "row": 17,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "spend.map:region",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "title": "New Users",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(255,240,240)"
            ],
            [
              0.2,
              "rgb(255,176,230)"
            ],
            [
              0.4,
              "rgb(250,156,210)"
            ],
            [
              0.6,
              "rgb(250,136,190)"
            ],
            [
              0.8,
              "rgb(248,106,165)"
            ],
            [
              1,
              "rgb(248, 76, 141)"
            ]
          ],
          "hoverinfo": "z+location",
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "ISO-3",
          "locations": [
            "USA",
            "CAN",
            "GBR",
            "BGR",
            "LVA",
            "EGY",
            "GUM",
            "MYS",
            "RUS",
            "FRA",
            "TWN",
            "BRA",
            "COL",
            "DEU",
            "JAM",
            "IRL",
            "MEX"
          ],
          "marker": {
            "line": {
              "color": "rgba(1, 1, 1, 1)",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "US",
            "CA",
            "GB",
            "BG",
            "LV",
            "EG",
            "GU",
            "MY",
            "RU",
            "FR",
            "TW",
            "BR",
            "CO",
            "DE",
            "JM",
            "IE",
            "MX"
          ],
          "type": "choropleth",
          "z": [
            "1014901",
            "132",
            "77",
            "91",
            "14",
            "6",
            "6",
            "9",
            "28",
            "4",
            "2",
            "1",
            "2",
            "1",
            "14",
            "1",
            "4"
          ]
        }
      ],
      "field": "unique_conversions.map:geo",
      "layout": {
        "autosize": True,
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "red",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "lataxis": {
            "range": [
              -55,
              90
            ],
            "showgrid": False,
            "showline": True
          },
          "lonaxis": {},
          "projection": {
            "rotation": {
              "lon": 0
            },
            "type": "miller"
          },
          "scope": "world",
          "showframe": False,
          "showlakes": True,
          "showland": False,
          "showrivers": False,
          "showsubunits": False,
          "subunitcolor": "rgba(0, 0, 255, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "New Users by country",
        "yaxis": {
          "gridcolor": "rgba(255, 255, 255, 1)",
          "gridwidth": 1.0,
          "hoverformat": ".1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": ".0f",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 18,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "unique_conversions.map:geo",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "title": "New Users",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(255,240,240)"
            ],
            [
              0.2,
              "rgb(255,176,230)"
            ],
            [
              0.4,
              "rgb(250,156,210)"
            ],
            [
              0.6,
              "rgb(250,136,190)"
            ],
            [
              0.8,
              "rgb(248,106,165)"
            ],
            [
              1,
              "rgb(248, 76, 141)"
            ]
          ],
          "hoverinfo": "z+location",
          "hovertext": [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
          ],
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "USA-states",
          "locations": [
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "DC",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY"
          ],
          "marker": {
            "line": {
              "color": "rgba(1, 1, 1, 1)",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
          ],
          "type": "choropleth",
          "z": [
            "542",
            "636",
            "510",
            "576",
            "676",
            "694",
            "506",
            "530",
            "596",
            "620",
            "632",
            "672",
            "508",
            "534",
            "604",
            "668",
            "532",
            "530",
            "626",
            "520",
            "692",
            "552",
            "502",
            "660",
            "544",
            "688",
            "610",
            "624",
            "636",
            "600",
            "668",
            "696",
            "506",
            "556",
            "520",
            "524",
            "594",
            "554",
            "594",
            "522",
            "610",
            "556",
            "662",
            "590",
            "698",
            "612",
            "534",
            "544",
            "680",
            "658",
            "668"
          ]
        }
      ],
      "field": "unique_conversions.map:region",
      "layout": {
        "autosize": True,
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "coastlinecolor": "rgba(0, 255, 0, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "red",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "landcolor": "rgba(0, 255, 0, 1)",
          "lataxis": {},
          "lonaxis": {},
          "oceancolor": "rgba(137, 203, 255, 1)",
          "scope": "usa",
          "showcoastlines": True,
          "showframe": True,
          "showlakes": True,
          "showland": True,
          "showocean": True,
          "showrivers": True,
          "showsubunits": True,
          "subunitcolor": "rgba(0, 0, 255, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "New Users by US state",
        "xaxis": {
          "anchor": "y",
          "domain": [
            0,
            1
          ],
          "gridcolor": "rgba(255, 255, 255, 1)",
          "gridwidth": 1.0,
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "range": [
            0,
            0.08
          ],
          "rangemode": "normal",
          "showline": False,
          "tickformat": ".0% ",
          "ticks": "",
          "title": "Payer-CVR",
          "titlefont": {
            "color": "#7f7f7f",
            "family": "Geneva, Verdana, Geneva, sans-serif",
            "size": 16
          },
          "zeroline": False
        },
        "yaxis": {
          "gridcolor": "rgba(255, 255, 255, 1)",
          "gridwidth": 1.0,
          "hoverformat": ".1f",
          "linecolor": "rgba(148, 148, 148, 1)",
          "linewidth": 1,
          "mirror": "",
          "rangemode": "tozero",
          "showline": False,
          "tick0": 0,
          "tickformat": ".0f",
          "ticks": "",
          "ticksuffix": "% ",
          "title": "",
          "zeroline": False
        }
      },
      "row": 18,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "unique_conversions.map:region",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "tickformat": "$,",
            "title": "Revenues",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(240,245,240)"
            ],
            [
              0.2,
              "rgb(150,210,130)"
            ],
            [
              0.4,
              "rgb(130,190,110)"
            ],
            [
              0.6,
              "rgb(110,170,90)"
            ],
            [
              0.8,
              "rgb(90,150,70)"
            ],
            [
              1,
              "rgb(65,135,48)"
            ]
          ],
          "hoverinfo": "z+location",
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "ISO-3",
          "locations": [
            "USA",
            "CAN",
            "GBR",
            "BGR",
            "LVA",
            "EGY",
            "GUM",
            "MYS",
            "RUS",
            "FRA",
            "TWN",
            "BRA",
            "COL",
            "DEU",
            "JAM",
            "IRL",
            "MEX"
          ],
          "marker": {
            "line": {
              "color": "rgba(1, 1, 1, 1)",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "US",
            "CA",
            "GB",
            "BG",
            "LV",
            "EG",
            "GU",
            "MY",
            "RU",
            "FR",
            "TW",
            "BR",
            "CO",
            "DE",
            "JM",
            "IE",
            "MX"
          ],
          "type": "choropleth",
          "z": [
            "1415.42",
            "1327.41",
            "1316.51",
            "1270.2",
            "1229.04",
            "1256.66",
            "1256.11",
            "1220.85",
            "1047.14",
            "1009.84",
            "1036.84",
            "996.56",
            "942.51",
            "895.98",
            "909.41",
            "809.03",
            "772.1"
          ]
        }
      ],
      "field": "purchase_value.map:geo",
      "layout": {
        "autosize": True,
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "red",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "lataxis": {
            "range": [
              -55,
              90
            ],
            "showgrid": False,
            "showline": True
          },
          "lonaxis": {},
          "projection": {
            "rotation": {
              "lon": 0
            },
            "type": "miller"
          },
          "scope": "world",
          "showframe": False,
          "showlakes": True,
          "showland": False,
          "showrivers": False,
          "showsubunits": False,
          "subunitcolor": "rgba(0, 0, 255, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "Revenues by country",
        "yaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        }
      },
      "row": 19,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "purchase_value.map:geo",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "tickformat": "$,",
            "title": "Revenues",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(240,245,240)"
            ],
            [
              0.2,
              "rgb(150,210,130)"
            ],
            [
              0.4,
              "rgb(130,190,110)"
            ],
            [
              0.6,
              "rgb(110,170,90)"
            ],
            [
              0.8,
              "rgb(90,150,70)"
            ],
            [
              1,
              "rgb(65,135,48)"
            ]
          ],
          "hoverinfo": "z+location",
          "hovertext": [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
          ],
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "USA-states",
          "locations": [
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "DC",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY"
          ],
          "marker": {
            "line": {
              "color": "rgba(1, 1, 1, 1)",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
          ],
          "type": "choropleth",
          "z": [
            "1252.87",
            "1031.92",
            "936.22",
            "736.85",
            "708.49",
            "640.54",
            "601.04",
            "527.79",
            "520.73",
            "501.39",
            "414.27",
            "406.54",
            "404.02",
            "384.41",
            "377.03",
            "358.83",
            "355.68",
            "344.05",
            "311.6",
            "300.39",
            "298.33",
            "274.65",
            "252.81",
            "237.51",
            "202.49",
            "195.54",
            "194.48",
            "183.67",
            "181.51",
            "169.6",
            "162.14",
            "161.03",
            "149.09",
            "147.58",
            "141.85",
            "114.19",
            "113.36",
            "97.64",
            "95.84",
            "92.37",
            "70.75",
            "70.51",
            "69.21",
            "61.75",
            "56.36",
            "47.24",
            "44.47",
            "42.43",
            "39.18",
            "39.11",
            "24.2"
          ]
        }
      ],
      "field": "purchase_value.map:region",
      "layout": {
        "autosize": True,
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "coastlinecolor": "rgba(0, 255, 0, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "red",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "landcolor": "rgba(0, 255, 0, 1)",
          "lataxis": {},
          "lonaxis": {},
          "oceancolor": "rgba(137, 203, 255, 1)",
          "scope": "usa",
          "showcoastlines": True,
          "showframe": True,
          "showlakes": True,
          "showland": True,
          "showocean": True,
          "showrivers": True,
          "showsubunits": True,
          "subunitcolor": "rgba(0, 0, 255, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "Revenues by US state",
        "xaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        },
        "yaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        }
      },
      "row": 19,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "purchase_value.map:region",
  },
  {
    "config": {
      "col": 1,
      "config": {
        "displaylogo": False,
        "scrollZoom": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "tickformat": ".0%",
            "title": "ROAS",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(255,0,0)"
            ],
            [
              0.2,
              "rgb(230,100,0)"
            ],
            [
              0.4,
              "rgb(205,200,0)"
            ],
            [
              0.6,
              "rgb(180,200,25)"
            ],
            [
              0.8,
              "rgb(75,173,50)"
            ],
            [
              1,
              "rgb(0,153,76)"
            ]
          ],
          "hoverinfo": "z+location",
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "ISO-3",
          "locations": [
            "USA",
            "CAN",
            "GBR",
            "BGR",
            "LVA",
            "EGY",
            "GUM",
            "MYS",
            "RUS",
            "FRA",
            "TWN",
            "BRA",
            "COL",
            "DEU",
            "JAM",
            "IRL",
            "MEX"
          ],
          "marker": {
            "line": {
              "color": "rgba(1, 1, 1, 1)",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "US",
            "CA",
            "GB",
            "BG",
            "LV",
            "EG",
            "GU",
            "MY",
            "RU",
            "FR",
            "TW",
            "BR",
            "CO",
            "DE",
            "JM",
            "IE",
            "MX"
          ],
          "type": "choropleth",
          "z": [
            "0.42",
            "0.37",
            "0.32",
            "0.25",
            "0.25",
            "0.27",
            "0.21",
            "0.19",
            "0.17",
            "0.12",
            "0.15",
            "0.15",
            "0.20",
            "0.12",
            "0.11",
            "0.07",
            "0.25"
          ]
        }
      ],
      "field": "roas.map:geo",
      "layout": {
        "autosize": True,
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "black",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "lataxis": {
            "range": [
              -55,
              90
            ],
            "showgrid": False,
            "showline": True
          },
          "lonaxis": {},
          "projection": {
            "rotation": {
              "lon": 0
            },
            "type": "miller"
          },
          "scope": "world",
          "showframe": False,
          "showlakes": True,
          "showland": False,
          "showrivers": False,
          "showsubunits": False,
          "subunitcolor": "rgba(0, 0, 255, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "ROAS by country",
        "yaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        }
      },
      "row": 20,
      "scrollZoom": False,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "roas.map:geo",
  },
  {
    "config": {
      "col": 2,
      "config": {
        "displaylogo": False
      },
      "data": [
        {
          "colorbar": {
            "thickness": 8,
            "tickfont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            },
            "tickformat": ".0%",
            "title": "ROAS",
            "titlefont": {
              "family": "Geneva, Verdana, Geneva, sans-serif"
            }
          },
          "colorscale": [
            [
              0,
              "rgb(255,0,0)"
            ],
            [
              0.2,
              "rgb(230,100,0)"
            ],
            [
              0.4,
              "rgb(205,200,0)"
            ],
            [
              0.6,
              "rgb(180,200,25)"
            ],
            [
              0.8,
              "rgb(75,173,50)"
            ],
            [
              1,
              "rgb(0,153,76)"
            ]
          ],
          "hoverinfo": "z+location",
          "hovertext": [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
          ],
          "line": {
            "color": "rgba(0,0,0,1)",
            "shape": "spline",
            "smoothing": 1,
            "width": 1
          },
          "locationmode": "USA-states",
          "locations": [
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "DC",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY"
          ],
          "marker": {
            "line": {
              "color": "rgba(1, 1, 1, 1)",
              "width": 0.5
            },
            "size": 6,
            "symbol": "circle"
          },
          "reversescale": False,
          "text": [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
          ],
          "type": "choropleth",
          "z": [
            "0.42",
            "0.37",
            "0.32",
            "0.25",
            "0.25",
            "0.27",
            "0.21",
            "0.19",
            "0.17",
            "0.12",
            "0.15",
            "0.15",
            "0.20",
            "0.12",
            "0.11",
            "0.07",
            "0.25",
            "0.42",
            "0.37",
            "0.32",
            "0.25",
            "0.25",
            "0.27",
            "0.21",
            "0.19",
            "0.17",
            "0.12",
            "0.15",
            "0.15",
            "0.20",
            "0.12",
            "0.11",
            "0.07",
            "0.25",
            "0.42",
            "0.37",
            "0.32",
            "0.25",
            "0.25",
            "0.27",
            "0.21",
            "0.19",
            "0.17",
            "0.12",
            "0.15",
            "0.15",
            "0.20",
            "0.12",
            "0.11",
            "0.07",
            "0.25",
            "0.42",
            "0.37",
            "0.32",
            "0.25",
            "0.25",
            "0.27",
            "0.21",
            "0.19",
            "0.17",
            "0.12",
            "0.15",
            "0.15",
            "0.20",
            "0.12",
            "0.11",
            "0.07",
            "0.25"
          ]
        }
      ],
      "field": "roas.map:region",
      "layout": {
        "autosize": True,
        "dragmode": "zoom",
        "geo": {
          "bgcolor": "rgba(255, 255, 255, 1)",
          "coastlinecolor": "rgba(0, 255, 0, 1)",
          "countrycolor": "rgba(1, 1, 1, 1)",
          "countrywidth": 3,
          "framecolor": "red",
          "lakecolor": "rgba(137, 203, 255, 1)",
          "landcolor": "rgba(0, 255, 0, 1)",
          "lataxis": {},
          "lonaxis": {},
          "oceancolor": "rgba(137, 203, 255, 1)",
          "scope": "usa",
          "showcoastlines": True,
          "showframe": True,
          "showlakes": True,
          "showland": True,
          "showocean": True,
          "showrivers": True,
          "showsubunits": True,
          "subunitcolor": "rgba(0, 0, 255, 1)"
        },
        "height": 350,
        "margin": {
          "autoexpand": True,
          "b": 45,
          "l": 60,
          "r": 50,
          "t": 80
        },
        "paper_bgcolor": "#fff",
        "showlegend": False,
        "title": "ROAS by US state",
        "xaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        },
        "yaxis": {
          "mirror": "",
          "showline": False,
          "ticks": "",
          "zeroline": False
        }
      },
      "row": 20,
      "section": "choropleth",
      "section_height": 1400,
      "section_name": "Maps",
      "section_open": False,
      "width": "50%"
    },
    "company": None,
    "dashboard": "marketing",
    "field": "roas.map:region",
  }
]
