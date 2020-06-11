The first thing we're going to do is [install the Datadog Agent](https://app.datadoghq.com/account/settings#agent). There are installation instructions for a variety of environments, so which one do we choose? Let's find out: try running `lsb_release -a`{{execute}}. (And, yes, that's already a hint as to our current operating environment).

Now we know! Install the Agent by copying and pasting the "[easy one-step install](https://app.datadoghq.com/account/settings#agent/ubuntu)" one-liner into the console. It won't take long.

So why install the Agent now—before we've even started coding? This way, when we're ready to test things later on, our little virtual machine will have been reporting data for a while, which will make it more interesting by the time we get to the end of this course. 😀

Once you've got a prompt again, be sure to verify that the Agent is running before continuing: `systemctl status datadog-agent`{{execute}}.
