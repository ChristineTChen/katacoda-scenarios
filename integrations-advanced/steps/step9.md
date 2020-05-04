It is now time to collect and submit metrics.

# Goals

- Submit the following metrics:
  - `github_repo.stargazers`: The total number of repository stargazers.
  - `github_repo.watchers`: The total number of repository watchers.
  - `github_repo.contributors`: The total number of repository contributors.
  - `github_repo.subscribers`: The total number of repository subscribers.
- Create a test to assert metric submission.

# Hints

- Use `self.gauge` to [submit metrics](https://docs.datadoghq.com/developers/metrics/gauges/).
- Use `import mock` to [mock PyGithub objects and methods](https://docs.python.org/3/library/unittest.mock.html#).
