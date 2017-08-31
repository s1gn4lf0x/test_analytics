import os
import json
import uuid

from django.test import TestCase

from shsql.models import Company
from shsql.models import ReportConfig
from shsql.models import FacebookApp
from shsql.models import FacebookAdAccount
from shsql.models import FacebookRawReport

from shsql.management.data.report_configs import facebook_report_configs

from .raw_reports import facebook_daily_raw_reports

class RawReportsTest(TestCase):
    def setUp(self):
        # Create the report configs to use
        for config in facebook_report_configs:
            kwargs = {
                'platform': config['platform'],
                'level': config['level'],
                'period': config['period'],
                'breakdown': config['breakdown']
            }
            if config['company']:
                kwargs['company'] = Company.get(id=config['company'])

            (report, created) = ReportConfig.objects.update_or_create(
                defaults = config,
                **kwargs
            )

        # Create the app and accounts to test
        test_api_id = uuid.uuid4()
        accs_file = '/tmp/test_ad_accounts.json'
        if os.path.isfile(accs_file):
            with open(accs_file) as f:
                accs = json.load(f)
                for acc in accs:
                    (self.company, created) = Company.objects.get_or_create(
                        id=acc['company_id'],
                        name='TestClient',
                        url='http://test.com',
                        api_id=test_api_id
                    )
                    (fb_app, created) = FacebookApp.objects.update_or_create(
                        company = self.company,
                        app_id = acc['app_id'],
                        defaults = {
                            'app_secret': acc['app_secret'],
                            'access_token': acc['access_token'],
                            'name': 'Test App'
                        }
                    )
                    fb_ad_acc = FacebookAdAccount.objects.create(
                        app = fb_app,
                        account_id = acc['account_id'],
                        name = 'Test Account',
                        platform = acc['platform'],
                        daily_budget = 10000,
                        objective = 'LINK_CLICKS',
                        is_active = True
                    )


    def test_facebook_daily_raw_reports(self):
        """We can pull and store facebook daily raw reports"""
        facebook_daily_raw_reports('account', 'web', '', 1)
        # There should now be reports in the DB
        reports = FacebookRawReport.objects.all()
        self.assertTrue(len(reports) > 0)
        # The reports config should match the input
        for r in reports:
            self.assertEqual(r.config.platform, 'web')
            self.assertEqual(r.config.level, 'account')
            self.assertEqual(r.company.id, self.company.id)

    def test_facebook_daily_geo_raw_reports(self):
        """We can pull and store facebook daily raw reports"""
        facebook_daily_raw_reports('account', 'web', 'geo', 1)
        # There should now be reports in the DB
        reports = FacebookRawReport.objects.all()
        self.assertTrue(len(reports) > 0)
        # The reports config should match the input
        for r in reports:
            self.assertEqual(r.config.platform, 'web')
            self.assertEqual(r.config.level, 'account')
            self.assertEqual(r.config.breakdown, 'geo')
            self.assertEqual(r.company.id, self.company.id)
            self.assertTrue(len(r.data) > 0)
            self.assertTrue('country' in r.data[0])

    def test_facebook_daily_region_raw_reports(self):
        """We can pull and store facebook daily raw reports"""
        facebook_daily_raw_reports('account', 'web', 'region', 1)
        # There should now be reports in the DB
        reports = FacebookRawReport.objects.all()
        self.assertTrue(len(reports) > 0)
        # The reports config should match the input
        for r in reports:
            self.assertEqual(r.config.platform, 'web')
            self.assertEqual(r.config.level, 'account')
            self.assertEqual(r.config.breakdown, 'region')
            self.assertEqual(r.company.id, self.company.id)
            self.assertTrue(len(r.data) > 0)
            self.assertTrue('region' in r.data[0])
