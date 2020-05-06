(You can find our completed solution in the `/workspace/solution` folder, as generated from the steps outlined below.)

# Check

Edit the `check.py` file in the `ådatadog_checks/github_repo/` directory and submit a service check every time you raise an exception or an error.

In our example, we created the following variable `SERVICE_CHECK_NAME = "github_repo.up"` and we updated the `handle_exception` method:

<pre class="file" data-target="clipboard">
def handle_exception(self, msg, status, tags, e):
    self.warning(msg)
    self.log.debug("{}: {}".format(msg, e))
    self.service_check(self.SERVICE_CHECK_NAME, status, tags=tags)
    raise ConfigurationError(msg)
</pre>

Do not forget to also submit the service check when the integration is running correctly.
The `OK` state service check must be submitted at the end of the check run.

<pre class="file" data-target="clipboard">
self.service_check(self.SERVICE_CHECK_NAME, AgentCheck.OK, tags=tags)
</pre>

# Test

Add the following code to `github_repo/tests/test_github_repo.py`:

<pre class="file" data-target="clipboard">
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
</pre>

__NOTES:__ 

- Replace `<YOUR_ACCESS_TOKEN>` with your Github Access Token.
- The `aggregator` stub is created by default and can be used to assert what is being submitted by the check method. You just need to add it as method parameter—like we did for `instance`.

