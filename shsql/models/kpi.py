from django.db import models
from django.contrib.postgres.fields import JSONField
from facebookads.adobjects.campaign import Campaign
from fernet_fields import EncryptedCharField

from .user import Company
from .configs import KPIReportConfig

class KPIBinnedDashboardReport(models.Model):
    """The bucket reports table"""

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='kpibinreports'
    )
    config = models.ForeignKey(
        KPIReportConfig,
        on_delete=models.PROTECT,
        related_name='kpibinreports'
    )
    report_date = models.DateTimeField()
    data = JSONField()

    class Meta:
        unique_together = ('company', 'config', 'report_date')

class KPIDashboardReport(models.Model):
    """The bucket reports table"""

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='kpidashreports'
    )
    report_date = models.DateTimeField()
    period = models.PositiveSmallIntegerField(default=1)
    data = JSONField()

    class Meta:
        unique_together = ('company', 'report_date', 'period')
