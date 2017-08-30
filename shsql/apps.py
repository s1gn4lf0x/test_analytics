from django.apps import AppConfig

class ShSQLConfig(AppConfig):
    name = 'shsql'

    def ready(self):
        import shsql.signals
