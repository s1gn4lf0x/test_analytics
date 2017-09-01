import os
import boto3
import json

from datetime import datetime, timedelta
from delorean import Delorean
from django.db import IntegrityError, transaction
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adaccount import AdAccount

from celery import shared_task

from shsql.models import FacebookRawReport

from .util import fetch_active_accounts
from .util import result_key
from .util import report_config
from .report_manager import ReportManager

@shared_task
def facebook_raw_reports(level, platform, breakdown, period):
    """ Task to fetch daily raw facebook ad reports.
    Pull all active ad accounts from the web DB and fetch raw facebook
    reports for them. Store the raw report data in DynamoDB for later
    processing.
    """
    active_accounts = fetch_active_accounts()
    # For each active ad account generate the appropriate fb reports and store
    # TODO: batch this job
    result = facebook_raw_reports_batch(active_accounts, level, platform, breakdown, period)
    return { 'fb_raw_report_{}_{}_d{}'.format(level, breakdown, period): result }

def facebook_raw_reports_batch(accounts, level, platform, breakdown, period, day=1):
    """Create a batch of daily raw reports"""
    result = []
    try:
        with transaction.atomic():
            for acc in accounts:
                # Initialize the api for this app
                FacebookAdsApi.init(
                    acc.app.app_id,
                    acc.app.app_secret,
                    acc.app.access_token
                )
                # Get the ad account
                ad_account = AdAccount('act_{}'.format(acc.account_id))
                # Get the report config from the DB
                setup = report_config(
                    level,
                    platform,
                    breakdown,
                    acc.app.company,
                    period
                )
                report_date = (Delorean() - timedelta(days=day)).truncate('day').datetime
                report_date_str = report_date.strftime('%Y-%m-%d')
                setup.config['params']['time_range'] = {
                    'since': report_date_str,
                    'until': report_date_str
                }

                # Setup the report manager and pull the insights
                manager = ReportManager(setup.config)
                raw_insights = manager.raw_ad_insights(ad_account)
                # Insert the raw insights into the DB
                (report, created) = FacebookRawReport.objects.update_or_create(
                    account=acc,
                    company=acc.app.company,
                    config=setup,
                    report_date=report_date,
                    defaults={'data': [dict(insight) for insight in raw_insights]}
                )
                result.append({acc.account_id: created})
    except IntegrityError as e:
        logger.error('DB error! Transactions will be rolled back' + str(e))
        result.append({'error': str(e)})
    return result

def facebook_backdate_raw_reports_batch(accounts, level, platform, breakdown, period, days=14, offset=1):
    """Create a batch of backdated daily raw reports"""
    result = []
    for d in range(offset,days+offset):
        result.append(facebook_raw_reports_batch(accounts, level, platform, breakdown, period, d))
    return result
