import json
import os
import uuid
from django.core.management.base import BaseCommand

from shsql.models import Company
from shsql.models import FacebookReportConfig
from shsql.models import KPIReportConfig
from shsql.models import DashboardConfig
from shsql.models import ChartConfig
from shsql.models import TableConfig
from shsql.models import FacebookAdSetConfig
from shsql.management.data.report_configs import kpi_report_configs
from shsql.management.data.report_configs import facebook_report_configs
from shsql.management.data.dashboard_configs import dashboard_configs
from shsql.management.data.chart_configs import chart_configs
from shsql.management.data.table_configs import table_configs
from shsql.management.data.adset_configs import adset_configs

def kwargs_from_fields(config, fields):
    return {f: config[f] for f in fields}

def update_configs(configs, fields, m):
    for config in configs:
        all_fields = fields if not config['company'] else fields + ['company']
        kwargs = kwargs_from_fields(config, all_fields)
        m.objects.update_or_create(
            defaults = config,
            **kwargs
        )

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Loop through the report configs and insert them into
        # the DB ... create OR update
        update_configs(
            facebook_report_configs,
            ['platform', 'level', 'period', 'breakdown'],
            FacebookReportConfig
        )

        update_configs(
            kpi_report_configs,
            ['name'],
            KPIReportConfig
        )

        update_configs(
            dashboard_configs,
            ['platform', 'dashboard'],
            DashboardConfig
        )

        update_configs(
            chart_configs,
            ['field', 'dashboard'],
            ChartConfig
        )

        update_configs(
            table_configs,
            ['name', 'dashboard'],
            TableConfig
        )

        update_configs(
            adset_configs,
            ['platform', 'objective', 'geo'],
            FacebookAdSetConfig
        )
