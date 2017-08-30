import uuid

from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField

class Company(models.Model):
    """The Company class

    A company is the basic user of the system having one or more
    apps and one or more users.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    url = models.URLField(blank=True)
    admin = models.ForeignKey(User, null=True, blank=True)
    api_id = models.UUIDField(default=uuid.uuid4)
    api_urls = ArrayField(models.URLField(), null=True, blank=True)

    def __unicode__(self):
        print('here in company unicode!!')
        return '{}'.format(self.name)

class UserProfile(models.Model):
    """The user profile class

    Extends the user information to add the company they belong to.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        print('here in str!!')
        return '{}'.format(self.company.name)
