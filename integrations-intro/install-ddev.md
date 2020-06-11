The developer toolkit is comprehensive and includes a lot of functionality. We'll touch on a few of the many features as we go, but the first step is to install it:
```
pip install "datadog-checks-dev[cli]"
```{{execute}}

That will take a moment. Don't worry if you see some red lines fly by—it's probably fine. 😉

This is the same toolkit that the developers at Datadog use every day, so by default it expects to work on the core integrations. Let's adjust that expectation, and in so doing, introduce you to the tooling and syntax:
```
ddev config set repo extras
```{{execute}}
