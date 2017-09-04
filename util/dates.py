from datetime import datetime, timedelta
from delorean import Delorean
from django.utils import timezone

def create_report_date(offset):
    local_date = timezone.localtime() - timedelta(days=offset)
    return Delorean(local_date).truncate('day').datetime
