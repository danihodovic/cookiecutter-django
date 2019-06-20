from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            # pylint: disable=unused-import,import-outside-toplevel
            import {{ cookiecutter.project_slug }}.users.signals  # noqa F401
        except ImportError:
            pass
