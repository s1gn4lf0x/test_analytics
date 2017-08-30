from django.db import models
from django.contrib.postgres.fields import JSONField
from facebookads.adobjects.campaign import Campaign
from fernet_fields import EncryptedCharField

from .user import Company

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

class FacebookAccountDailyRawReport(models.Model):
    """The Facebook app auth information
    needed for running ads through the marketing API.
    Each client would typically only need one 'app'
    to run ads with.
    """
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='fbdailyrawreports'
    )
    account = models.ForeignKey(
        FacebookAdAccount,
        on_delete=models.CASCADE,
        related_name='fbdailyrawreports'
    )
    report_date = models.DateTimeField()
    data = JSONField()

    class Meta:
        unique_together = ('company', 'account', 'report_date')