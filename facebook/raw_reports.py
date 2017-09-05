import os
import boto3
import json
import logging

from django.db import IntegrityError, transaction
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adaccount import AdAccount

from shsql.models import FacebookRawReport
from util.dates import create_report_date

from .util import result_key
from .util import report_config
from .report_manager import ReportManager

logger = logging.getLogger('django')

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
                report_date = create_report_date(day)
                logger.info('raw report {} {} {} {}'.format(
                    platform,
                    level,
                    breakdown,
                    report_date)
                )
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

def facebook_backdate_raw_reports_batch(
    accounts,
    level,
    platform,
    breakdown,
    period,
    days=14,
    offset=1
):
    """Create a batch of backdated daily raw reports"""
    result = []
    for d in range(offset,days+offset):
        result.append(facebook_raw_reports_batch(
            accounts,
            level,
            platform,
            breakdown,
            period,
            d
        ))
    return result
