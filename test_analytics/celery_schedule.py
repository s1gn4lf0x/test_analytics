from celery.schedules import crontab
from collections import OrderedDict

fb_reports = [
    ['account', 'web', '', 1],
    ['account', 'web', 'geo', 1],
    ['account', 'web', 'region', 1],
    ['campaign', 'web', '', 1],
    ['adset', 'web', '', 1],
]

# Task run times are in UTC
fb_task_map = {
    'fb-raw-reports': {
        'task': 'facebook.tasks.facebook_raw_reports',
        'hour': 19,
        'minute': 10,
        'extra_args': []
    },
    'fb-dashboard-reports': {
        'task': 'facebook.tasks.facebook_dashboard_reports',
        'hour': 19,
        'minute': 12,
        'extra_args': []
    },
    'fb-to-redshift-reports': {
        'task': 'facebook.tasks.facebook_reports_to_redshift',
        'hour': 19,
        'minute': 37,
        'extra_args': []
    }
}

# Period and offset
kpi_reports = [
    [1, 1,]
]

kpi_task_map = {
    'kpi-binned-reports': {
        'task': 'kpi.tasks.kpi_binned_reports',
        'hour': 20,
        'minute': 35,
        'extra_args': []
    },
    'kpi-binned-reports': {
        'task': 'kpi.tasks.kpi_reports',
        'hour': 20,
        'minute': 39,
        'extra_args': []
    },
}

def configure_celery_tasks():
    celery_tasks = {}
    for task in fb_task_map:
        for i, r in enumerate(fb_reports):
            hr = fb_task_map[task]['hour']
            mn = fb_task_map[task]['minute']
            next_time = divmod(fb_task_map[task]['minute']+i*3, 60)
            celery_tasks[task+'-'+'-'.join([str(a) for a in r if a != ''])] = {
                'task': fb_task_map[task]['task'],
                'schedule': crontab(
                    hour=fb_task_map[task]['hour']+next_time[0],
                    minute=next_time[1]
                ),
                'args': r + fb_task_map[task]['extra_args']
            }
    for task in kpi_task_map:
        for i, r in enumerate(kpi_reports):
            hr = kpi_task_map[task]['hour']
            mn = kpi_task_map[task]['minute']
            next_time = divmod(kpi_task_map[task]['minute']+i*2, 60)
            celery_tasks[task+'-'+'-'.join([str(a) for a in r if a != ''])] = {
                'task': kpi_task_map[task]['task'],
                'schedule': crontab(
                    hour=kpi_task_map[task]['hour']+next_time[0],
                    minute=next_time[1]
                ),
                'args': r + kpi_task_map[task]['extra_args']
            }
    return celery_tasks
