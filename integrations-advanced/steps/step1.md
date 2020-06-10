# Setup
Before we get started, wait about 30 seconds for the setup script to finish.
The setup script prints this message in the terminal when the setup is complete:

```
Your workspace setup is done! Enjoy the workshop :)
```

The setup script did the following things for you:

1. Cloned the community-driven integration repository into the workspace directory.
  `git clone -q https://github.com/DataDog/integrations-extras.git /workspace/integration-extras`

2. Set up a Python virtual environment.
   ```
   virtualenv -p python3.8 venv
   source venv/bin/activate
   ```

3. Installed and configured the Datadog CLI.
   ```
   pip install "datadog-checks-dev[cli]"
   ddev config set extras "/workspace/integrations-extras"
   ddev config set repo extras
   ```
  

# Getting started

Make sure that your terminal is in the correct folder and that your virtual environment is activated:
1. `cd /workspace/integration-extras/`{{execute}}
2. `source venv/bin/activate`{{execute}}

Now that you are fully set up, you can start your first assignment.

# Goals
1. [Create a Github Access Token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
  - Select scope `repo:public_repo`

2. Log in to your Datadog account, then install the Agent in the workshop environment.
  - [Installation Instructions](https://app.datadoghq.com/account/settings#agent/ubuntu)
  - [Check that you can see your instance running](https://app.datadoghq.com/infrastructure)
3. In your terminal, install `PyGithub` via the Python CLI, then write a script to return the `Datadog/integrations-extras` repository name.

