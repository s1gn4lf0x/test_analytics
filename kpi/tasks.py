import logging

from celery import shared_task
from psycopg2.extras import DictCursor

from util.dates import create_report_date

from .util import fetch_active_accounts
from .util import RedshiftHelper
from .binned_reports import kpi_bin_reports_batch

logger = logging.getLogger('django')

@shared_task
def kpi_binned_reports(period, offset):
    """ Task to fetch cohort bins KPI numbers for active clients.
    Fetch client-specific configurations for cohort bin and compute KPIs for each bin.
    Store the raw report data in DynamoDB for later processing.
    """

    rs = RedshiftHelper(cursor_factory=DictCursor)
    accounts = fetch_active_companies(rs)
    logger.info("Accounts: {}".format(str(accounts)))

    results = []
    for account in accounts:
        company_id = account[0]
        logger.info("CompanyId: {}".format(company_id))
        results.append(kpi_bin_reports_batch(
            company_id,
            rs,
            create_report_date(offset),
            period
        ))
    return results

@shared_task
def kpi_reports(period, offset):
    """ Task to fetch KPI numbers for active clients.
    KPIs include daily total revenue, dau, dpu and arpu
    Store the raw report data in DynamoDB for later processing.
    """

    rs = RedshiftHelper(cursor_factory=DictCursor)
    accounts = fetch_active_companies(rs)
    logger.info("Accounts: {}".format(str(accounts)))

    results = []
    for account in accounts:
        company_id = account[0]
        logger.info("CompanyId: {}".format(company_id))
        results.append(kpi_daily_reports_batch(
            company_id,
            rs,
            create_report_date(offset),
            period
        ))
    return results
