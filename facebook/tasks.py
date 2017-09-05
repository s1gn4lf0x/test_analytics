from celery import shared_task

from .util import fetch_active_accounts
from .util import construct_to_redshift_url

from .raw_reports import facebook_raw_reports_batch
from .raw_reports import facebook_backdate_raw_reports_batch

from .dashboard_reports import facebook_dashboard_reports_batch
from .dashboard_reports import facebook_backdate_dashboard_reports_batch

from .redshift_reports import send_to_endpoint

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
    result = facebook_raw_reports_batch(
        active_accounts,
        level,
        platform,
        breakdown,
        period
    )
    return {
        'fb_raw_report_{}_{}_{}_d{}'.format(
            level,
            platform,
            breakdown,
            period
        ): result
    }

@shared_task
def facebook_backdate_raw_reports(
    level,
    platform,
    breakdown,
    period,
    days,
    offset
):
    """ Task to fetch daily raw facebook ad reports.
    Pull all active ad accounts from the web DB and fetch raw facebook
    reports for them. Store the raw report data in DynamoDB for later
    processing.
    """
    active_accounts = fetch_active_accounts()
    # For each active ad account generate the appropriate fb reports and store
    # TODO: batch this job
    result = facebook_backdate_raw_reports_batch(
        active_accounts,
        level,
        platform,
        breakdown,
        period,
        days,
        offset
    )
    return {
        'fb_backdate_raw_report_{}_{}_{}_d{}'.format(
            level,
            platform,
            breakdown,
            period
        ): result
    }

@shared_task
def facebook_dashboard_reports(level, platform, breakdown, period):
    """ Task to test creation of daily UA dashboard reports.
    Create dashboard facebook reports for the test client accounts.
    Store the result in DynamoDB for web access.
    """
    accounts = fetch_active_accounts()
    # For each test ad account generate the appropriate fb reports and store
    result = facebook_dashboard_reports_batch(
        accounts,
        level,
        platform,
        breakdown,
        period
    )
    return {
        'fb_dash_report_{}_{}_{}_d{}'.format(
            level,
            platform,
            breakdown,
            period
        ): result
    }

@shared_task
def facebook_backdate_dashboard_reports(
    level,
    platform,
    breakdown,
    period,
    days,
    offset
):
    """ Task to test creation of daily UA dashboard reports.
    Create dashboard facebook reports for the test client accounts.
    Store the result in DynamoDB for web access.
    """
    accounts = fetch_active_accounts()
    # For each test ad account generate the appropriate fb reports and store
    result = facebook_backdate_dashboard_reports_batch(
        accounts,
        level,
        platform,
        breakdown,
        period,
        days,
        offset
    )
    return {
        'fb_backdate_dash_report_{}_{}_{}_d{}'.format(
            level,
            platform,
            breakdown,
            period):
        result
    }

@shared_task
def facebook_reports_to_redshift(level, platform, breakdown, period):
    accounts = fetch_active_accounts()
    url = construct_to_redshift_url(level, breakdown, period)
    result = send_to_endpoint(
        accounts,
        level,
        platform,
        breakdown,
        period,
        url,
        day=1
    )
    return {
        'to_redshift_{}_{}_{}_{}'.format(
            level,
            platform,
            breakdown,
            period
        ): result
    }
