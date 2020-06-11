So… is the new integration working? Let's find out! We'll use the `status` command to get the details:
```
datadog-agent status
```{{execute}}

Well, that was verbose. The `status` command has lots of information but we only want some of it, so let's use one of the oldest tools in the box: grep.
```
datadog-agent status | grep -A7 awesome
```{{execute}}

Oh, and if JSON is your jam:
```
datadog-agent status -p | jq '.runnerStats.Checks.awesome'
```{{execute}}

Feel free to play around with the status output to get a feel for what's available. 👍
