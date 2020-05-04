(You can find our completed solution in the `/workspace/solution` folder, as generated from the steps outlined below.)

- See the `/workspace/solution/github_repo/manifest.json` file.
- See the `/workspace/solution/github_repo/metadata.csv` file.
- See the `/workspace/solution/github_repo/assets/service_checks.json` file.
- See the `/workspace/solution/github_repo/README.md` file.

# Build

- Build the wheel:
  `ddev -e release build github_repo`{{execute}}
- Install the integration via the Agent:
  `sudo -u dd-agent datadog-agent integration install -w github_repo/dist/datadog_github_repo-0.0.1-py2.py3-none-any.whl`{{execute}}
- Create a configuration file for the integration:
  `cp /etc/datadog-agent/conf.d/github_repo.d/conf.yaml.example /etc/datadog-agent/conf.d/github_repo.d/conf.yaml`{{execute}}
- Configure your Github access token and repository name to
  `vim /etc/datadog-agent/conf.d/github_repo.d/conf.yaml`{{execute}}
  - Hint: The `nano` text editor is also available.
- Install the required dependencies into the embedded Python environment of the Agent:
  `sudo -u dd-agent /opt/datadog-agent/embedded/bin/pip install -r github_repo/requirements.in --no-cache`{{execute}}
- Restart the Agent in order to activate the integration:
  `sudo service datadog-agent restart`{{execute}}
- Verify that the integration is functioning:
  `sudo datadog-agent status`{{execute}}
- Examine the status and submitted metrics of the check:
  `sudo -u dd-agent -- datadog-agent check github_repo`{{execute}}

# Visualize

- Log in to your [Datadog account](https://app.datadoghq.com/).
- Go to the [metrics explorer](https://app.datadoghq.com/metric/explorer) and verify that you are receiving the `github_repo.contributors` metrics.
- Create a [new dash or screenboard](https://app.datadoghq.com/dashboard/lists) and display the submitted metrics.
