import os
import json
import uuid

from django.test import TestCase
from django.core import management

from shsql.models import Company
from shsql.models import KPIDashboardReport
from shsql.models import KPIBinnedDashboardReport

from .tasks import kpi_binned_reports
from .tasks import kpi_reports

class KPIReportsTest(TestCase):
    def setUp(self):
        # Create the report configs to use
        management.call_command('sync_configs')

        # Create a company to test
        (self.company, created) = Company.objects.get_or_create(
            id=uuid.UUID('2c308727-678d-4b9a-b716-3b0cf1559e31'),
            name='Test Client',
            url='http://test.com',
            api_id=uuid.uuid4()
        )

    def test_kpi_binned_reports(self):
        """We can run the kpi binned reports"""
        # There should now be reports in the DB
        result = kpi_binned_reports(1, 1)
        print(result)

        reports = KPIBinnedDashboardReport.objects.all()
        # There should now be some reports available
        self.assertTrue(len(reports) > 0)
        for r in reports:
            self.assertEqual(r.company.id, self.company.id)
            self.assertTrue('labels' in r.data)
            self.assertTrue('payload' in r.data)

    def test_kpi_reports(self):
        """We can run the kpi reports"""
        # There should now be reports in the DB
        result = kpi_reports(1, 1)
        print(result)

        reports = KPIDashboardReport.objects.all()
        # There should now be some reports available
        self.assertTrue(len(reports) > 0)
        for r in reports:
            self.assertEqual(r.company.id, self.company.id)
            self.assertTrue('labels' in r.data)
            self.assertTrue('revenue' in r.data)
