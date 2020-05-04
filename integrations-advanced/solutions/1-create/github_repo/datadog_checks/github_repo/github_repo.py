from github import Github

from datadog_checks.base import AgentCheck


class GithubRepoCheck(AgentCheck):
    def check(self, instance):
        g = Github()

        repo = g.get_repo("Datadog/integrations-extras")
        self.log.debug('Getting stats for: {}'.format(repo.full_name))
