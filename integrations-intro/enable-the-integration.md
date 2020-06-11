You're almost there! All that's left to do now is to enable the integration within the Agent. In the Real World this would normally be done as part of some larger configuration management strategy, but that's a bit out of scope for this workshop. There's also a [built-in web GUI](https://docs.datadoghq.com/agent/?tab=agentv6#gui) for most operating environments, but since we've spent so much time in the console already, let's keep the trend going. 😀

Let's take a look at the example configuration:
```
cat /etc/datadog-agent/conf.d/awesome.d/conf.yaml.example | grep -v "^$\|#"
```{{execute}}

[Looks familiar](https://docs.datadoghq.com/developers/integrations/new_check_howto/#example-configuration), right? In fact, this configration is ready to go, so let's activate it:
```
cp /etc/datadog-agent/conf.d/awesome.d/conf.yaml.example /etc/datadog-agent/conf.d/awesome.d/conf.yaml
chown dd-agent /etc/datadog-agent/conf.d/awesome.d/conf.yaml
```{{execute}}

The last thing to do now is to restart the Agent so that it picks up the new configuration file:
```
systemctl restart datadog-agent
```{{execute}}

And let's make sure that worked:
```
systemctl status datadog-agent
```{{execute}}
