The `metadata.csv` describes all of the metrics that can be collected by the integration. In our case, we're not actually collecting any metrics, so there's no need to touch this file. It's worth mentioning however, because this file is important for one of the most interesting aspects of integrations: white-listed metrics. Any metrics listed in `metadata.csv`, once accepted upstream, won't count against the custom metric limit!

The [Datadog Agent documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#metrics-metadata-file) has more details if you're interested. If you want to really dive deep into the underlying mechanics, you can also examine the [Metrics section](https://docs.datadoghq.com/developers/metrics/) of the developer documentation—for now, just bookmark it though. 😉

Ok, let's keep it moving!
