(You can find our completed solution in the `/workspace/solution` folder, as generated from the steps outlined below.)

# Check 

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file and submit the collected metrics:

![github_repo-8](https://raw.githubusercontent.com/ChristineTChen/katacoda-scenarios/master/integrations-advanced/assets/github_repo-8.png)

# Test

Create a new Python file called `test_e2e.py` in `github_repo/tests/` in order to separate the tests.

Below is a example of how we mocked `PyGithub` methods to test the integration. There are _many_ different ways to do this—this is just one possibility.

![test_github_repo-4](https://raw.githubusercontent.com/ChristineTChen/katacoda-scenarios/master/integrations-advanced/assets/test_github_repo-4.png)

__NOTES:__
- Replace `<YOUR_ACCESS_TOKEN>` with your Github Access Token.
- The `aggregator` stub is created by default and can be used to assert what is being submitted by the check method.
- We use the `mock.patch` annotation to mock `PyGithub` methods.
- We call the `assert_all_metrics_covered()` method to make sure we asserted all the submitted metrics.
