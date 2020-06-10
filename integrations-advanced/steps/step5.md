Now that we have created the basis for our integration, we are going to add some configuration options.

The `/assets/configuration/spec.yaml` of your integration directory contains the integration's specification detailing options that influence behavior.

# Goals

- Create an `access_token` configuration parameter in the `init_config` section of the integration specification file.
- Create a `repository_name` configuration parameter in the `instances` section of the integration specification file.
- Use `ddev validate config --sync` to sync your configuration file.
- Use both parameters in your `check` function logic.
- Handle exceptions by raising `ConfigurationError` errors. 
  - Check that required parameters are set and valid.
- Create a test to make sure that your code works.

# Hints
- See `spec.yaml` [options documentation][https://datadoghq.dev/integrations-core/meta/config_specs/#options]
- Implement the `__init__` method to retrieve `init_config` configurations.
  - You still need to instantiate the super `AgentCheck` class.
- Create methods to factorize code.
- For examples, see the existing open source [Datadog integrations](https://github.com/DataDog/integrations-core) repository.
- Take a look at the [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#configuration-file) to see how to edit your configuration file.
