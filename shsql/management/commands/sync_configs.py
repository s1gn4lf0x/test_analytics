import json
import os
import uuid
from django.core.management.base import BaseCommand

from shsql.models import Company
from shsql.models import ReportConfig
from shsql.management.data.report_configs import facebook_report_configs

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Loop through the report configs and insert them into
        # the DB ... create OR update
        for config in facebook_report_configs:
            kwargs = {
                'platform': config['platform'],
                'level': config['level'],
                'period': config['period'],
                'breakdown': config['breakdown']
            }
            if config['company']:
                kwargs['company'] = Company.get(id=config['company'])

            ReportConfig.objects.update_or_create(
                defaults = config,
                **kwargs
            )
