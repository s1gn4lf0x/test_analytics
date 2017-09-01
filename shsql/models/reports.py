from django.db import models
from django.contrib.postgres.fields import JSONField

from .user import Company

class ReportConfig(models.Model):
    """Table to store report mapping configs.
    These configs are used for pulling reports (which fields etc)
    and for analysis of raw report data, column name mapping etc.
    """

    platform = models.CharField(max_length=128)
    level = models.CharField(max_length=128)
    breakdown = models.CharField(max_length=128, blank=True)
    period = models.PositiveSmallIntegerField(default=1)
    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.CASCADE
    )
    config = JSONField()

    class Meta:
        unique_together = ('platform', 'level', 'breakdown', 'period', 'company')

class DashboardConfig(models.Model):
    """The dashboard configs table"""
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='dashconfigs',
        null=True
    )
    platform = models.CharField(max_length=128)
    dashboard = models.CharField(max_length=128)
    config = JSONField()

    class Meta:
        unique_together = ('company', 'platform', 'dashboard')

class ChartConfig(models.Model):
    """The chart configs table"""
    field = models.CharField(max_length=128)
    dashboard = models.CharField(max_length=128)
    config = JSONField()

    class Meta:
        unique_together = ('field', 'dashboard')

class TableConfig(models.Model):
    """The table configs table"""
    table = models.CharField(max_length=128)
    dashboard = models.CharField(max_length=128)
    config = JSONField()

    class Meta:
        unique_together = ('table', 'dashboard')