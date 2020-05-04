(You can find our completed solution in the `/workspace/solution` folder, as generated from the steps outlined below.)

# Create the integration 

Run the following command `ddev create "Github Repo"`{{execute}} and provide the requested information.

# Dependency

Add the `PyGitHub` dependency to the `github_repo/requirements.in` file.

# Check

Add the `github_repo/datadog_checks/github_repo/check.py` file with the following code:

![github_repo.py](https://raw.githubusercontent.com/ChristineTChen/katacoda-scenarios/master/integrations-advanced/assets/github_repo-1.png)

# Test

Add the `github_repo/tests/test_github_repo.py` file with the following code:

![test_github_repo-1.py](https://raw.githubusercontent.com/ChristineTChen/katacoda-scenarios/master/integrations-advanced/assets/test_github_repo-1.png)

__NOTES:__

- The `test_check` takes a parameter called `instance` as an argument. This parameter is defined in `github_repo/tests/conftest.py`.
- Don't forget to `import` the Github library!

Use the tooling to run the tests: `ddev test github_repo -dv`{{execute}}.
