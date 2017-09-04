from django.db import models
from django.contrib.postgres.fields import JSONField
from facebookads.adobjects.campaign import Campaign
from fernet_fields import EncryptedCharField

from .user import Company
from .configs import FacebookReportConfig

class FacebookApp(models.Model):
    """The Facebook app auth information
    needed for running ads through the marketing API.
    Each client would typically only need one 'app'
    to run ads with.
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    app_id = models.CharField(max_length=100, unique=True)
    app_secret = EncryptedCharField(max_length=100)
    access_token = EncryptedCharField(max_length=256)
    name = models.CharField(max_length=100, blank=True)
    business_id = models.CharField(max_length=100, blank=True)

class FacebookAdAccount(models.Model):
    """The information for a specific ad account i.e.,
    a particular app and platform (and even then there may
    be multiple accounts)
    """
    PLATFORM_CHOICES = (
        ('ios', 'iOS'),
        ('android', 'Android'),
        ('web', 'Web Site'),
        ('canvas', 'Canvas App')
    )
    app = models.ForeignKey(
        FacebookApp,
        on_delete=models.CASCADE,
        related_name='accounts'
    )
    account_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    platform = models.CharField(max_length=32, choices=PLATFORM_CHOICES)
    daily_budget = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=False)
    validation = models.CharField(max_length=500, blank=True)
    objective = models.CharField(max_length=100, default=Campaign.Objective.link_clicks)
    is_reporting_only = models.BooleanField(default=True)
    is_auto = models.BooleanField(default=False)

    class Meta:
        unique_together = ('account_id', 'app')

class FacebookRawReport(models.Model):
    """The Facebook raw report data
    """
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='fbrawreports'
    )
    account = models.ForeignKey(
        FacebookAdAccount,
        on_delete=models.CASCADE,
        related_name='fbrawreports'
    )
    config = models.ForeignKey(
        FacebookReportConfig,
        on_delete=models.PROTECT,
        related_name='fbrawreports'
    )
    report_date = models.DateTimeField()
    data = JSONField()

    class Meta:
        unique_together = ('company', 'account', 'report_date', 'config')

class FacebookDashboardReport(models.Model):
    """The Facebook dashboard report data.
    Data taken from the raw report and configured for use
    on the dashboard including the addition of derived fields etc.
    """
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='fbreports'
    )
    account = models.ForeignKey(
        FacebookAdAccount,
        on_delete=models.CASCADE,
        related_name='fbreports'
    )
    raw_report = models.ForeignKey(
        FacebookRawReport,
        on_delete=models.PROTECT,
        related_name='fbreports'
    )
    report_date = models.DateTimeField()
    data = JSONField()

    class Meta:
        unique_together = ('company', 'account', 'report_date', 'raw_report')

class FacebookAdSetConfig(models.Model):
    """The AdSet definition table"""

    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.CASCADE
    )
    platform = models.CharField(max_length=128)
    objective = models.CharField(max_length=128)
    optimization_goal = models.CharField(max_length=128)
    billing_event = models.CharField(max_length=128)
    geo = models.CharField(max_length=128)
    bid_amount = models.DecimalField(max_digits=7, decimal_places=2)
    optional_config = JSONField()

    class Meta:
        unique_together = ('company', 'platform', 'objective', 'geo')

class FacebookImageCreative(models.Model):
    """Image creative storage by Company"""
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    image_hash = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=512)
    url = models.URLField(max_length=256)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('company', 'date_created', 'name')

class FacebookImage(models.Model):
    """Image storage by Company"""

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    image_hash = models.CharField(max_length=256)
    permalink_url = models.URLField(max_length=256)
    created_time = models.DateTimeField()
    accounts = models.ManyToManyField(
        FacebookAdAccount,
        related_name='fb_images'
    )

    class Meta:
        unique_together = ('company', 'image_hash')
