from __future__ import absolute_import

import responses

from exam import fixture
from sentry.testutils import PluginTestCase

from sentry_redmine.plugin import RedminePlugin

class RedminePluginTest(PluginTestCase):
    @fixture
    def plugin(self):
        return RedminePlugin()

    def test_conf_key(self):
        assert self.plugin.test_conf_key == 'redmine'

    def test_entry_point(self):
        self.assertAppInstalled('redmine', 'sentry_plugins.victorops')
        self.assertPluginInstalled('redmine', self.plugin)

    def test_is_configured(self):
        assert self.plugin.is_configured(self.project) is False
        self.plugin.set_option('api_key', 'abcdef', self.project)
        assert self.plugin.is_configured(self.project) is True

    def test_render_config(self):
        user = self.create_user()
        project = self.create_project()
        self.plugin.get_config(project=project,)
        