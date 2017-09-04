import json
import psycopg2

from django.conf import settings
from django.core.exceptions import ValidationError

from rest_framework.serializers import CharField

class RedshiftHelper:
    """A class to handle Redshift queries and interactions"""

    def __init__(self, cursor_factory=None):
        self.schema = settings.REDSHIFT_SCHEMA
        credentials = {}
        credentials['dbname'] = settings.REDSHIFT_DB_NAME
        credentials['user'] = settings.REDSHIFT_USERNAME
        credentials['password'] = settings.REDSHIFT_PASSWORD
        credentials['host'] = settings.REDSHIFT_HOSTNAME
        credentials['port'] = settings.REDSHIFT_PORT
        self.conn = psycopg2.connect(**credentials)
        self.cursor = self.conn.cursor(cursor_factory=cursor_factory)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def run_query(self, query, params=None, commit=False):
        """Run the query string"""
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        if commit:
            self.conn.commit()
