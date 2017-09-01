import json
import os
import uuid
from django.core.management.base import BaseCommand

from facebook.tasks import facebook_raw_reports

class Command(BaseCommand):

    def handle(self, *args, **options):
        # run the raw reports for the last day manually
        facebook_raw_reports('account', 'web', '', 1)
