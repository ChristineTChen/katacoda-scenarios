import pytest

from datadog_checks.base import ConfigurationError
from datadog_checks.github_repo import GithubRepoCheck


def test_check_invalid_configs(instance):
    # Test missing access_token
    with pytest.raises(ConfigurationError):
        GithubRepoCheck('github_repo', {}, {})

    # Test missing repository_name
    check = GithubRepoCheck('github_repo', {'access_token': "foo"}, {})
    with pytest.raises(ConfigurationError):
        check.check({})

    # Test invalid access_token
    check = GithubRepoCheck('github_repo', {'access_token': "invalid"}, {})
    with pytest.raises(ConfigurationError):
        check.check({"repository_name": "bar"})

    check = GithubRepoCheck('github_repo', {'access_token': "<YOUR_ACCESS_TOKEN>"}, {})
    check.check(instance)


def test_check_service_checks(instance, aggregator):
    check = GithubRepoCheck('github_repo', {'access_token': "invalid"}, {})
    with pytest.raises(ConfigurationError):
        check.check({"repository_name": "invalid"})

    aggregator.assert_service_check(GithubRepoCheck.SERVICE_CHECK_NAME, status=check.CRITICAL)

    # We need to reset the aggregator between tests
    aggregator.reset()

    check = GithubRepoCheck('github_repo', {'access_token': "<YOUR_ACCESS_TOKEN>"}, {})
    check.check(instance)
    aggregator.assert_service_check(
        GithubRepoCheck.SERVICE_CHECK_NAME, status=check.OK, tags=['repository_name:Datadog/integrations-extras']
    )
