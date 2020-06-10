(You can find our completed solution in the `integrations-extras` repo)

# Check 

Edit the `check.py` file in the `github_repo/datadog_checks/github_repo/` directory and submit the collected metrics:

The following should be added the `check()` function.

<pre class="file" data-target="clipboard">
try:
    stargazers = repo.get_stargazers().totalCount
    self.gauge('github_repo.stargazers', stargazers, tags=tags)
    watchers = repo.get_watchers().totalCount
    self.gauge('github_repo.watchers', watchers, tags=tags)
    contributors = repo.get_contributors().totalCount
    self.gauge('github_repo.contributors', contributors, tags=tags)
    subscribers = repo.get_subscribers().totalCount
    self.gauge('github_repo.subscribers', subscribers, tags=tags)

except RateLimitExceededException as e:
    self.handle_exception(
        "Rate limit exceeded. Make sure you provided an access_token", AgentCheck.WARNING, tags, e
    )
</pre>

# Test

Create a new Python file called `test_e2e.py` in `github_repo/tests/` in order to separate the tests.

Below is a example of how we mocked `PyGithub` methods to test the integration. There are _many_ different ways to do this—this is just one possibility.


<pre class="file" data-target="clipboard">
import mock

from datadog_checks.github_repo import GithubRepoCheck


class TotalCountMock:
    def __init__(self, total_count):
        self.totalCount = total_count


def get_stargazers_mock():
    return TotalCountMock(1)


def get_watchers_mock():
    return TotalCountMock(2)


def get_contributors_mock():
    return TotalCountMock(3)


def get_subscribers_mock():
    return TotalCountMock(4)


@mock.patch('github.Repository.Repository.get_stargazers', side_effect=get_stargazers_mock)
@mock.patch('github.Repository.Repository.get_watchers', side_effect=get_watchers_mock)
@mock.patch('github.Repository.Repository.get_contributors', side_effect=get_contributors_mock)
@mock.patch('github.Repository.Repository.get_subscribers', side_effect=get_subscribers_mock)
def test_check_using_mocks(stargazers_mock, watchers_mock, contributors_mock, subscribers_mock, instance, aggregator):
    check = GithubRepoCheck('github_repo', {"access_token": "<YOUR_ACCESS_TOKEN>"}, {})
    check.check(instance)

    aggregator.assert_metric('github_repo.stargazers', value=1.0, tags=['repository_name:Datadog/integrations-extras'])
    aggregator.assert_metric('github_repo.watchers', value=2.0, tags=['repository_name:Datadog/integrations-extras'])
    aggregator.assert_metric(
        'github_repo.contributors', value=3.0, tags=['repository_name:Datadog/integrations-extras']
    )
    aggregator.assert_metric('github_repo.subscribers', value=4.0, tags=['repository_name:Datadog/integrations-extras'])

    aggregator.assert_all_metrics_covered()
</pre>

__NOTES:__
- Replace `<YOUR_ACCESS_TOKEN>` with your Github Access Token.
- The `aggregator` stub is created by default and can be used to assert what is being submitted by the check method.
- We use the `mock.patch` annotation to mock `PyGithub` methods.
- We call the `assert_all_metrics_covered()` method to make sure we asserted all the submitted metrics.
