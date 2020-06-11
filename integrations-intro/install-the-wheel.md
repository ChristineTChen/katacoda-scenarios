Now that we have an installable artefact, we can go ahead and install it via the Agent directly:
```
cp /root/dd/integrations-extras/awesome/dist/datadog_awesome-0.0.1-py2.py3-none-any.whl /tmp
sudo -u dd-agent datadog-agent integration install -w /tmp/datadog_awesome-0.0.1-py2.py3-none-any.whl
```{{execute}}

Wondering what's going on there? Let's break it down:
`sudo -u dd-agent`
- Execute the following command as another user—in this case "dd-agent", which is the user that the Datadog Agent uses on Linux systems by default.

`datadog-agent integration`
- Use the "integration" sub-system available in the Agent as of v6.10.0.

`install -w`
- Install an integration from a wheel, specifically.

`/tmp/datadog_awesome-0.0.1-py2.py3-none-any.whl`
- The path of the wheel.

Question: Why copy the wheel to `/tmp/` first?
