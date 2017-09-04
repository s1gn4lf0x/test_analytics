import os
import boto3
import json

from datetime import datetime, timedelta
from delorean import Delorean
from django.utils import timezone

from util.fernet import FernetHelper
from util.row import Row
from shsql.models import FacebookAdAccount
from shsql.models import FacebookReportConfig
from shsql.models import DashboardConfig


# ------- Shared helper functions (non-task functions) ------- #
def fetch_active_accounts():
    return FacebookAdAccount.objects.filter(is_active__exact=True)

def fetch_test_accounts():
    test_accs_file = '/tmp/test_ad_accounts.json'
    s3 = boto3.client('s3')
    s3.download_file('eb-settings', 'test_ad_accounts.json', test_accs_file)
    if os.path.isfile(test_accs_file):
        with open(test_accs_file) as f:
            accs = json.load(f)
            cols = list(accs[0].keys())
            raw_rows = [[acc[col] for col in cols] for acc in accs]
            rows = [Row(cols, row) for row in raw_rows]
            return rows

def result_key(acc):
    """Key to save the report result under."""
    return '{}_{}'.format(acc.company_id,acc.account_id)

def report_config(level, platform, breakdown, company, period):
    """Get the report config for this compandy and specification.
    If there is no company specific config, use the generic one.
    """

    report_config = FacebookReportConfig.objects.filter(
        level=level,
        platform=platform.lower(),
        breakdown=breakdown,
        company=company,
        period=period
    )
    if report_config.exists():
        return report_config.get()
    else:
        return FacebookReportConfig.objects.filter(
            level=level,
            platform=platform.lower(),
            breakdown=breakdown,
            company=None,
            period=period
        ).get()

def dashboard_config(company, platform, dashboard):
    dash_config = DashboardConfig.objects.filter(
        company=company,
        platform=platform.lower(),
        dashboard=dashboard
    )
    if dash_config.exists():
        return dash_config.get()
    else:
        return DashboardConfig.objects.filter(
            company=None,
            platform=platform.lower(),
            dashboard=dashboard
        ).get()
