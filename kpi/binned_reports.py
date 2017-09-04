import logging

from shsql.models import Company
from shsql.models import KPIBinnedDashboardReport
from shsql.models import KPIReportConfig

from .util import report_config
from .util import generate_kpi_bucket_sql
from .util import json_from_record
from .util import KPI_COHORT_BUCKET_REPORTS_KEY

logger = logging.getLogger('django')

def kpi_bin_reports_batch(company_id, rs, report_date, period):
    """ Fetches client configuration, generates sql, executes generated sql
    against Redshift, converts results to JSON and stores in DynamoDB
    """
    company = Company.get(id=company_id)
    kpi_config = report_config(company, KPI_COHORT_BUCKET_REPORTS_KEY)
    logger.info("Final configs: {}".format(str(config.config['params'])))

    params = kpi_config.config['params']
    query = generate_kpi_bucket_query(params, company_id, report_date)
    logger.debug(query)

    rs.run_query(query)
    payload = [json_from_record(record) for record in rs.cursor]
    logger.debug(data)

    data = {
        'labels': [report_date.strftime("%Y-%m-%d")],
        'payload': payload
    }

    (report, created) = KPIBinnedDashboardReport.objects.update_or_create(
        company=company,
        report_date=report_date,
        config=kpi_config,
        defaults={'data': data}
    )

    return {company_id: created}
