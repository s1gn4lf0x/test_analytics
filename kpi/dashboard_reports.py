from shsql.models import KPIDashboardReport
from shsql.models import Company

# Table counts query fields:
# field, table, agg1, agg2, target_field
query_fields = {
    'dau': ['dau','eng_freq_2','count','distinct','user_id'],
    'dpu': ['dpu','purchase','count','distinct','user_id'],
    'wau': ['wau','eng_freq_2','count','distinct','user_id'],
    'mau': ['mau','eng_freq_2','count','distinct','user_id'],
    'dnu': ['dnu','init','count','distinct','user_id'],
    'rev': ['revenue','purchase','sum','','amount'],
    'nts': ['num_trans','purchase','count','','id'],
    'seg': ['secondary_eng','eng_freq_2','count','distinct','id'],
    'fse': ['freq_secondary_eng','eng_freq_2','count(*)/count','distinct','id'],
    'ite': ['intensity_eng','eng_freq_2','avg','','intensity'],
    'fqt': ['freq_tertiary','eng_freq_3','count','distinct','id']
}

def count_dict(offset1, offset2, fields):
    table_args = [rs, offset1, offset2, *fields]
    return get_table_counts(*table_args)

def retention_dict(offset, is_payer=False):
    name = 'retention_d{}'.format(offset)
    if is_payer:
        name = 'payer_'+name
    retention_args = [rs, report_date, offset, company_id, name, is_payer]
    return get_retention_counts(*retention_args)

def safe_divide(a, b):
    return a/b if b != 0 else 0

def to_float_local(d, key):
    if d and key in d:
        if d[key]:
            return float(d[key])
    return 0

def kpi_daily_reports_batch(company_id, rs, report_date, period):
    """ Executes numerous queries to compute KPIs per active account.
    KPIs include daily total revenue, dau, dpu and arpu
    Store the raw report data in DynamoDB for later processing.
    """

    rev_dict = count_dict(1, 0, query_fields['rev'])
    dau_dict = count_dict(1, 0, query_fields['dau'])
    dpu_dict = count_dict(1, 0, query_fields['dpu'])
    wau_dict = count_dict(7, 1, query_fields['wau'])
    mau_dict = count_dict(7, 1, query_fields['mau'])
    dnu_dict = count_dict(1, 0, query_fields['dnu'])
    nts_dict = count_dict(1, 0, query_fields['nts'])
    seg_dict = count_dict(1, 0, query_fields['seg'])
    fse_dict = count_dict(1, 0, query_fields['fse'])
    ite_dict = count_dict(1, 0, query_fields['ite'])
    fqt_dict = count_dict(1, 0, query_fields['fqt'])

    rd1_dict = retention_dict(2)
    rd2_dict = retention_dict(3)
    rd7_dict = retention_dict(7)
    rd30_dict = retention_dict(30)
    rd60_dict = retention_dict(60)
    pd1_dict = retention_dict(2, is_payer=True)
    pd2_dict = retention_dict(3, is_payer=True)
    pd7_dict = retention_dict(7, is_payer=True)
    pd30_dict = retention_dict(30, is_payer=True)
    pd60_dict = retention_dict(60, is_payer=True)

    roas_bin_d1_dict = get_roas_buckets(rs, 'roas_d', 1, company_id)
    roas_bin_d2_dict = get_roas_buckets(rs, 'roas_d', 2, company_id)
    roas_bin_d7_dict = get_roas_buckets(rs, 'roas_d', 7, company_id)
    roas_bin_d30_dict = get_roas_buckets(rs, 'roas_d', 30, company_id)
    roas_bin_d60_dict = get_roas_buckets(rs, 'roas_d', 60, company_id)

    data = {
        'labels' : [dt.strftime("%Y-%m-%d")],
        'revenue' : [to_float_local(rev_dict,'revenue')],
        'dau' : [to_float_local(dau_dict,'dau')],
        'dpu' : [to_float_local(dpu_dict,'dpu')],
        'arpu' : [safe_divide(
            to_float_local(revenue_dict,'revenue'),
            to_float_local(dau_dict,'dau')
        )],
        'wau' : [to_float_local(wau_dict,'wau')],
        'mau' : [to_float_local(mau_dict,'mau')],
        'dnu' : [to_float_local(dnu_dict,'dnu')],
        'num_trans' : [to_float_local(nts_dict,'num_trans')],
        'secondary_eng' : [to_float_local(seg_dict,'secondary_eng')],
        'freq_secondary_eng' : [to_float_local(fse_dict,'freq_secondary_eng')],
        'intensity_eng' : [to_float_local(ite_dict,'intensity_eng')],
        'freq_tertiary_eng' : [to_float_local(fqt_dict,'freq_tertiary')],
        'retention_d1' : [to_float_local(rd1_dict,'retention_d1')],
        'retention_d2' : [to_float_local(rd2_dict,'retention_d2')],
        'retention_d7' : [to_float_local(rd7_dict,'retention_d7')],
        'retention_d30' : [to_float_local(rd30_dict,'retention_d30')],
        'retention_d60' : [to_float_local(rd60_dict,'retention_d60')],
        'payer_retention_d1' : [to_float_local(pd1_dict,'payer_retention_d1')],
        'payer_retention_d2' : [to_float_local(pd2_dict,'payer_retention_d2')],
        'payer_retention_d7' : [to_float_local(pd7_dict,'payer_retention_d7')],
        'payer_retention_d30' : [to_float_local(pd30_dict,'payer_retention_d30')],
        'payer_retention_d60' : [to_float_local(pd60_dict,'payer_retention_d60')],
        'payer_retention_d60' : [to_float_local(pd60_dict,'payer_retention_d60')],
        'roas_d1' : [to_float_local(roas_bin_d1_dict, 'spend')],
        'roas_d7' : [to_float_local(roas_bin_d1_dict, 'spend')],
        'roas_d30' : [to_float_local(roas_bin_d1_dict, 'spend')],
        'roas_d60' : [to_float_local(roas_bin_d1_dict, 'spend')]
    }

    (report, created) = KPIDailyDashboardReport.objects.update_or_create(
        company=Company.get(id=company_id),
        report_date=report_date,
        period=period,
        defaults={'data': data}
    )

    return {company_id: created}
