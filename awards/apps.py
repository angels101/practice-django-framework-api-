from django.apps import AppConfig


class AwardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awards'
    verbose_name='awwards'

    def ready(self):
        import awards.signals

# foo/apps.py

from django.apps import AppConfig

class FooConfig(AppConfig):
    name = 'full.python.path.to.your.app.foo'
    label = 'my.foo'  # <-- this is the important line - change it to anything other than the default, which is the module name ('foo' in this case)