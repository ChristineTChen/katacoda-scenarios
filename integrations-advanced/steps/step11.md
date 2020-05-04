Congratulations, your integration is almost complete!
Now we need to package the integration so that it can be added to the Datadog ecosystem.
Once done, we will be able to install the integration and run it with the Agent.

# Goals

- Update the `manifest.json` file.
- Update the `metadata.csv` file.
- Update the `service_checks.json` file.
- Update the `README.md` file.
- Create a wheel, then install and configure the integration.
- Make sure metrics are being submitted to Datadog.
- Visualize this integration with a Datadog dashboard.

# Hints

- See `manifest.json` [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#manifest-file).
- See `metadata.csv` [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#metrics-metadata-file).
- See `service_checks.json` [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#service-check-file).
- See the [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#building) to build and install an integration.
- See the Agent [documentation](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/?tab=agentv6#commands) to see Agent commands.
  - Use the `check` command to make sure your integration runs correctly.
 
