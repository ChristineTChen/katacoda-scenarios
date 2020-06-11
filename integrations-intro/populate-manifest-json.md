Next up is the `manifest.json` file, generally referred to simply as "the manifest". This file describes the opereating parameters of the integration, and is used by Datadog to help position the integration within the greater eco-system. Accordingly, the contents of this file are not generally used by the integration itself, which means it's not necessary for the integration to function; however, without a correctly populated manifest, a given integration cannot be included upstream.

The [Datadog integrations documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#manifest-file) covers the contents of this file extensively. Let's take a look at the `awesome/manifest.json`, which was created by the scaffolding. In particular, note:
- `display_name`: A unique, human-readable name for the integration.
- `short_description`: A short description of the integration.
- `categories`: This corresponds to the [list of integration categories](https://docs.datadoghq.com/integrations/); in this case, let's classify it as `web`.
- `public_title`: By convention, this is `Datadog-<display_name> Integration`.
- `is_public`: Whether or not to display it on the public integration list; this should be `false` until the integration is ready for prime time.

The next two are worth noting because they're _almost_ the same. They're both unique, machine-readable strings for the integration, but with one critical difference:
- `integration_id`: No underscores `_`, only dashes `-`.
- `name`: No dashes `-`, only underscores `_` (and it must match the _directory name_ of the integration).

Finally, note the reference to the `service_checks` asset, because that's where we're headed next!
