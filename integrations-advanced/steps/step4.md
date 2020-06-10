(You can find our completed solution in the `integrations-extras` repo)

# Create the integration 

Run the following command `ddev create "Github Repo"`{{execute}} and provide the requested information.

You should see the following message:

```
github_repo
├── assets
│   └── configuration
│       └── spec.yaml
│   └── service_checks.json
├── datadog_checks
│   └── github_repo
│       └── data
│           └── conf.yaml.example
│       ├── __about__.py
│       ├── __init__.py
│       └── check.py
│   └── __init__.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_github_repo.py
├── CHANGELOG.md
├── MANIFEST.in
├── README.md
├── manifest.json
├── metadata.csv
├── requirements-dev.txt
├── requirements.in
├── setup.py
└── tox.ini
```

# Dependency

Add the `PyGitHub` dependency to the `github_repo/requirements.in` file.

# Check

Add the following code to `github_repo/datadog_checks/github_repo/check.py` file:
<pre class="file" data-target="clipboard">
class GithubRepoCheck(AgentCheck):
    def check(self, instance):
        # type: (Dict[str, Any]) -> None

        g = Github()

        repo = g.get_repo("Datadog/integrations-extras")
        self.log.debug('Getting stats for: {}'.format(repo.full_name))
</pre>

          
# Test

In order to print debug logs we need to force the test to fail. Add the following code to `github_repo/tests/test_github_repo.py` file:
<pre class="file" data-target="clipboard">
def test_check(instance):
    check = GithubRepoCheck('github_repo', {}, {})
    check.check(instance)

    assert False
</pre>

__NOTES:__

- The `test_check` takes a parameter called `instance` as an argument. This parameter is defined in `github_repo/tests/conftest.py`.
- Don't forget to `import` the Github library!

Use the tooling to run the tests: `ddev test github_repo:py38 -dv`{{execute}}.
