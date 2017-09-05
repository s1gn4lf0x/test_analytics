import json
import logging
import requests

from django.conf import settings

from util.dates import create_report_date
from shsql.models import FacebookRawReport

from .util import report_config

logger = logging.getLogger('django')

def get_auth_token(domain):
    """Get the OAuth2 company token"""
    data = 'grant_type=client_credentials&username=fb_api_admin'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    url = domain + '/o/token/'
    logger.debug(url)
    auth = (
        settings.INTERNAL_USER['INTERNAL_API_USER_ID'],
        settings.INTERNAL_USER['INTERNAL_API_USER_SECRET']
    )
    r = requests.post(
        url,
        data=data,
        auth=auth,
        headers=headers
    )
    logger.debug('Auth response:')
    logger.debug('{}_{}_{}'.format(r.status_code, r.reason, r.text))

    result = json.loads(r.text)
    logger.debug(result)

    return result['access_token']

def get_safe_auth_token(domain):
    """Auth token wrapper"""
    token = get_auth_token(domain)
    logger.debug('Got token: {}'.format(token))
    return token

def send_to_endpoint(accounts, level, platform, breakdown, period, url, day=1):
    """ Task to test fetch of daily raw facebook ad reports.
    Fetch raw facebook reports for the test client accounts.
    Store the raw report data in DynamoDB for later processing.
    """
    report_date = create_report_date(day)
    logger.info('endpoint report: {}'.format(report_date))

    post_url = '{}{}'.format(settings.REDSHIFT_API_HOST_URL, url)
    token = get_safe_auth_token(settings.REDSHIFT_API_HOST_URL)
    headers = {'Authorization': 'Bearer '+ token}
    logger.info('Token {}'.format(token))

    result = []
    for acc in accounts:
        # Debug logging
        logger.debug(
            'Company {}, Account {}'.format(
                acc.app.company.id,
                acc.account_id
            )
        )

        # Get the unique report config from the DB
        setup = report_config(
            level,
            platform,
            breakdown,
            acc.app.company,
            period
        )

        # Get the reports for this report_date
        reports = FacebookRawReport.objects.filter(
            account=acc,
            company=acc.app.company,
            config=setup,
            report_date=report_date,
        )

        for r in reports:
            logger.debug(r.data)
            data = {
                'company_id' : str(acc.app.company.id),
                'report_date' : str(report_date),
                'description' : '{}_{}'.format(
                    acc.app.company.id,
                    acc.account_id
                ),
                'report_type' : '{}_{}_{}_{}'.format(
                    platform,
                    level,
                    breakdown,
                    period
                ),
                'payload' : json.dumps(r.data)
            }

            r = requests.post(
                post_url,
                json=data,
                headers=headers
            )
            logger.info('Signalfox Data API POST response:')
            logger.info(r.text)
            result.append({acc.account_id: r.status_code})

    return result
