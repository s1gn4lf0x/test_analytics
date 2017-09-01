import json
import os
import uuid
from django.core.management.base import BaseCommand

from facebook.tasks import facebook_backdate_raw_reports

class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--level', nargs=1, required=False,
            help='Report level e.g. account, campaign, adset'
        )
        parser.add_argument('--breakdown', nargs=1, required=False,
            help='Breakdown e.g. geo, region'
        )
        parser.add_argument('--days', nargs=1, required=True,
            help='No of days to backdate.'
        )
        parser.add_argument('--offset', nargs=1, required=True,
            help='No of days to offset before starting backdate'
        )

    def handle(self, *args, **options):
        # run the raw reports for the last day manually
        days = int(options['days'][0])
        offset = int(options['offset'][0])
        level = options['level'][0] if options['level'] else 'account'
        breakdown = options['breakdown'][0] if options['breakdown'] else ''
        facebook_backdate_raw_reports(
            level,
            'web',
            breakdown,
            1,
            days=days,
            offset=offset
        )
