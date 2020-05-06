(You can find our completed solution in the `/workspace/solution` folder, as generated from the steps outlined below.)

# Create the integration 

Run the following command `ddev create "Github Repo"`{{execute}} and provide the requested information.

# Dependency

Add the `PyGitHub` dependency to the `github_repo/requirements.in` file.

# Check

Add the `github_repo/datadog_checks/github_repo/check.py` file with the following code:

```python
class GithubRepoCheck(AgentCheck):
    def check(self, instance):
        g = Github()

        repo = g.get_repo("Datadog/integrations-extras")
        self.log.debug('Getting stats for: {}'.format(repo.full_name))
```

# Test

Add the `github_repo/tests/test_github_repo.py` file with the following code:

```python
def test_check(instance):
    check = GithubRepoCheck('github_repo', {}, {})
    check.check(instance)

    # In order to print debug logs we need to force the test to fail
    assert False
```

__NOTES:__

- The `test_check` takes a parameter called `instance` as an argument. This parameter is defined in `github_repo/tests/conftest.py`.
- Don't forget to `import` the Github library!

Use the tooling to run the tests: `ddev test github_repo -dv`{{execute}}.
