Congratulations, you were able to use the `PyGithub` library.

In this section, we are going to create an integration to run the same logic.

# Goals
- Create a `Github Repo` integration.
- Print the repository name as a debug log line.
- Create a unit test to check that your implementation is working.

# Hints
- Read the [How to create a new integration](https://docs.datadoghq.com/developers/integrations/new_check_howto/#scaffolding) documentation.
- Check the [AgentCheck Class](https://github.com/DataDog/integrations-core/blob/master/datadog_checks_base/datadog_checks/base/checks/base.py) to see what you can use to write logs.
- Debug logs are only printed to `stdout` if the test execution fails.

