All integrations come with a `conf.yaml.example` file that provides a starting point for actually setting up and using the integration. Depending on the nature of the integration—and, more to the point, the thing that integration is interacting with—this file can get pretty complex. However, every `conf.yaml` has some things in common, for example, they all contain an `init_config` block and an `instance` block. Furthermore, they all follow a very specific syntax covering not only the keywords and types, but the _comments_ as well. The [Datadog integrations documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#configuration-file) goes into the details and it's absolutely worth reviewing in order to make sure you understand the guidelines, defaults, and expectations.

Once you're comfortable with that section, we'll once again scoop up the example from the [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#example-configuration) and pop it into our `awesome/datadog_checks/awesome/data/conf.yaml.example`.

We're back into the weeds here, so let's ask some questions about what we're looking at:
- What, if any, are the global settings? How about the per-instance settings?
- If we wanted to monitor _another_ URL, how would we do that?
- What, if anything, would un-commenting the `follow_redirects` option do?
