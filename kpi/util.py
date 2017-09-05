import json
import logging

from decimal import Decimal
from django.conf import settings

from util.dates import create_report_date
from shsql.models import KPIReportConfig

KPI_COHORT_BUCKET_REPORTS_KEY = 'kpi_cohort_bucket_reports'
DEFAULT = 'default'

logger = logging.getLogger('django')

def fetch_active_companies(rs):
    """ Gets active companies from Redshift by doing
    a distinct select
    """
    query = """
        select distinct(company_id) from {}.init
    """.format(settings.REDSHIFT_SCHEMA)
    rs.run_query(query)
    return rs.cursor.fetchall()

def report_config(company, name):
    """Get the KPI report config for this company and name.
    If there is no company specific config, use the generic one.
    """
    report_config = KPIReportConfig.objects.filter(
        company=company,
        name=name
    )
    if report_config.exists():
        return report_config.get()
    else:
        return KPIReportConfig.objects.filter(
            company=None,
            name=name
        ).get()

def safe_divide(a, b):
    return a/b if b != 0 else 0

def to_float_local(d, key):
    if d and key in d:
        if d[key]:
            return float(d[key])
    return 0

def json_from_record(record):
    return json.loads(json.dumps(dict(record), default=default_converter))

def default_converter(obj):
    """ Decimal converter for JSON serializer"""
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError

def generate_kpi_bucket_query(params, company_id, report_date):
    """ Generates custom sql based on client-specific configuration.
    Each section of the resulting UNION corresponds to a cohort bin defined
    by the client
    """

    query = """
        select company_id, bin, sum(amount) as revenue,
        count(*) as transactions, max(spend) as spend,
        (sum(amount)-max(spend))/max(spend) as pct_pnl
        from (
    """

    for p, param in enumerate(params):
        if p > 0:
            query += " union all "

        query += """
            select i.company_id, '{bucket}' as bin,
            datediff('day', i.install_ts, p.create_ts) as days_active,
            i.install_ts, p.amount, fb.spend
            from {schema}.purchase p
            inner join {schema}.init i on p.user_id = i.user_id and p.company_id = i.company_id
            inner join {schema}.fb_raw_reports fb on i.install_ts::date = fb.report_date::date
            where p.company_id = '{company_id}'
            and date(i.install_ts) = '{report_date}'
            and datediff('day', i.install_ts, p.create_ts) between {lo} and {hi}
        """.format(
            bucket=param["name"],
            company_id=company_id,
            lo=param["lo"],
            hi=param["hi"],
            schema=settings.REDSHIFT_SCHEMA,
            report_date=report_date)

    query += """) as a
    group by company_id, bin
    order by company_id, bin asc"""
    return query

def get_roas_buckets(rs, prefix, dd, company_id):
    query = """
        select '{prefix}{dd}' as title, sum(p.amount) amount,
        sum(fb.spend) spend, (sum(p.amount)-sum(fb.spend))/sum(fb.spend) pct_pnl
        from {schema}.purchase p
        inner join {schema}.init i on p.user_id = i.user_id
        and p.create_ts::date < dateadd(day, {dd}, i.install_ts)::date
        and i.company_id = p.company_id
        inner join {schema}.fb_raw_reports fb on i.install_ts::date = fb.report_date::date
        where i.company_id='{company_id}'
    """.format(
        company_id=company_id,
        dd=dd,
        schema=settings.REDSHIFT_SCHEMA,
        prefix=prefix
    )
    logger.debug(query)

    rs.run_query(query)
    one = rs.cursor.fetchone()
    return dict(one) if one else None

def get_cohorted_counts(rs, company_id, output_name):
    """ Utility function to simplify computing count aggregates by
    company and date from Redshift tables
    """
    query = """
        select create_ts::date as cohort,
        count(distinct user_id) from {schema}.init
        where user_id in (
            select distinct user_id from {schema}.purchase
            where company_id='{company_id}'
        )
        and company_id='{company_id}'
        group by cohort
    """.format(
        company_id=company_id,
        schema=settings.REDSHIFT_SCHEMA
    )
    logger.debug(query)

    rs.run_query(query)
    one = rs.cursor.fetchone()
    return dict(one) if one else None

def get_retention_counts(
    rs,
    d_dt,
    offset,
    company_id,
    output_name,
    is_payer_retention=False
):
    """ Utility function to simplify computing count aggregates by
    company and date from Redshift tables
    """
    init_dt = create_report_date(offset)
    query = """
        select count(distinct user_id) as {output_name} from {schema}.eng_freq_2
        where date(create_ts) = '{d_dt}'
        and company_id = '{company_id}'
	    and user_id in (
           select distinct user_id from {schema}.init
           where date(create_ts) = '{init_dt}'
           and company_id = '{company_id}')
    """.format(
        d_dt=d_dt,
        init_dt=init_dt,
        company_id=company_id,
        schema=settings.REDSHIFT_SCHEMA,
        output_name=output_name
    )

    if is_payer_retention:
        query += """
            and user_id in (
                select distinct user_id from {schema}.purchase
                where company_id = '{company_id}'
            )
        """.format(
            company_id=company_id,
            schema=settings.REDSHIFT_SCHEMA
        )
    logger.debug(query)

    rs.run_query(query)
    one = rs.cursor.fetchone()
    return dict(one) if one else None

def get_table_counts(
    rs,
    offset_from,
    offset_to,
    company_id,
    field,
    table,
    agg1,
    agg2,
    target_field,
):
    """ Utility function to simplify computing count aggregates by
    company and date from Redshift tables
    """
    dt_from = create_report_date(offset_from)
    dt_to = create_report_date(offset_to)
    query = """
        select {agg1}({agg2}({target_field})) {field}
        from {schema}.{table}
        where create_ts between '{dt_from}' and '{dt_to}'
	    and company_id = '{company_id}'
        group by company_id
    """.format(
        dt_from=dt_from,
        dt_to=dt_to,
        company_id=company_id,
        field = field,
        schema=settings.REDSHIFT_SCHEMA,
        table=table,
        agg1=agg1,
        agg2=agg2,
        target_field=target_field
    )
    logger.debug(query)

    rs.run_query(query)
    one = rs.cursor.fetchone()
    return dict(one) if one else {field: 0}
