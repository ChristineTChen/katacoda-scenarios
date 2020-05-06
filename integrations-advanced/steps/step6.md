(You can find our completed solution in the `/workspace/solution` folder, as generated from the steps outlined below.)

# Edit the configuration file

Add the following content to `github_repo/assets/configuration/spec.yaml`:

<pre class="file" data-target="clipboard">
  - template: init_config
    options:
      - name: access_token
        required: true
        value:
          type: string
        description: The Github access token to authenticate the Github API.
      - template: init_config/default
  - template: instances
    options:
      - name: repository
        required: true
        value:
          type: string
        description: The Github repository name to monitor.
      - template: instances/default
</pre>

and sync the configuration file to automatically apply these changes:

`ddev validate config --sync`{{execute}}

You should see the `access_token` and `repository` configuration options in `github_repo/datadog_checks/github_repo/data/conf.yaml.example`.

# Init

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file.  
- Add an `__init__` method to retrieve your `access_token` from the `init_config` section of your configuration.
- Check that the `access_token` is set correctly; otherwise, raise a `ConfigurationError` error.

<pre class="file" data-target="clipboard">
class GithubRepoCheck(AgentCheck):
    def __init__(selfself, name, init_config, instances):
        super(GithubRepoCheck, self).__init__(name, init_config, instances)
        
        # Fetch config
        self.access_token = init_config.get('access_token')
        if not self.access_token:
            raise ConfigurationError('Configuration error, please set an access_token.')
</pre>

# Check

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file. 
- Similar to what you did with the `__init__` method, fetch and validate the `repository_name` parameter.

<pre class="file" data-target="clipboard">
def check(self, instance):
    repository_name = instance.get('repository_name')
    if not repository_name:
        raise ConfigurationError('Configuration error, please set a repository name.')
</pre>

- Use both parameters in your logic. Catch exceptions that may be raised by the `PyGithub` library.

<pre class="file" data-target="clipboard">
        # Get repository
        g = Github(self.access_token)

        try:
            repo = g.get_repo(repository_name)
            self.log.debug('Getting stats for: {}'.format(repo.name))
            tags.append("repository_name:{}".format(repository_name))

        except BadCredentialsException as e:
            self.handle_exception("Failed to authenticate to Github with given access_token", e)
        except UnknownObjectException as e:
            self.handle_exception("Failed to access repository. Check your repository_name config", e)
        except RateLimitExceededException as e:
            self.handle_exception("Rate limit exceeded. Make sure you provided an access_token", e)
</pre>

We created the following method to avoid code duplication:

<pre class="file" data-target="clipboard">
def handle_exception(self, msg, e):
    self.warning(msg)
    self.log.debug("{}: {}".format(msg, e))
    raise ConfigurationError(msg)
</pre>

# Test

Edit the `github_repo/tests/test_github_repo.py` file with the following code:

<pre class="file" data-target="clipboard">
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
</pre>

__NOTES:__ 

- Replace `<YOUR_ACCESS_TOKEN>` with your Github access token.

We are using the `instance` parameter in the test method `def test_check_invalid_configs(instance):`
As a result, the `repository_name` parameter for that instance needs to be set.

Add the following code to `github_repo/tests/conftest.py`:

<pre class="file" data-target="clipboard">
@pytest.fixture
def instance():
    return {"repository_name": "Datadog/integrations-extras"}
</pre>