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
        'minute': 38,
        'extra_args': []
    },
    'fb-dashboard-reports': {
        'task': 'facebook.tasks.facebook_dashboard_reports',
        'hour': 19,
        'minute': 41,
        'extra_args': []
    }
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
    return celery_tasks
