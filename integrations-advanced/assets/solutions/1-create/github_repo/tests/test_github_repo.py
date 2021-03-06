# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.github_repo import GithubRepoCheck


def test_check(aggregator, instance):
    check = GithubRepoCheck('github_repo', {}, [instance])
    check.check(instance)

    aggregator.assert_all_metrics_covered()

    # In order to print debug logs we need to force the test to fail
    assert False
