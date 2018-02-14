from __future__ import absolute_import

from django.conf import settings

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

pytest_plugins = ['sentry.utils.pytest']
def pytest_configure(config):
    from sentry.plugins import plugins
    from sentry_redmine.plugin import RedminePlugin
    settings.INSTALLED_APPS += ('sentry_redmine', )
    plugins.register(RedminePlugin)
     
    settings.SECRET_KEY = 'redmine-plugin'
    settings.SENTRY_USE_BIG_INTS = True
