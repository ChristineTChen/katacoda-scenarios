from datadog_checks.github_repo import GithubRepoCheck


def test_check(instance):
    check = GithubRepoCheck('github_repo', {}, {})
    check.check(instance)

    # In order to print debug logs we need to force the test to fail
    assert False
