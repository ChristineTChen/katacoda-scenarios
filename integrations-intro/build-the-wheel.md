Next stop: the wheel. Wheels are a Python-native packaging format. If you've ever used RPM or DEB files, for example, you've encountered a packaging format—wheels are quite similar. And, like all packaging formats, you can tumble down the rabbit hole fairly easily. Luckily for us, the `ddev` tooling takes care of the heavy lifting:
```
ddev release build awesome
```{{execute}}

The output contains an important line: the path where the wheel file that was built. Let's take a look:
```
ls -l /root/dd/integrations-extras/awesome/dist
```{{execute}}

So, what's in that wheel anyway? It's a package, so there should be a way to see the files that are inside it, right? Yes! In fact, it's just a ZIP file with a different extension, so let's take a closer look:
```
unzip -l /root/dd/integrations-extras/awesome/dist/datadog_awesome-0.0.1-py2.py3-none-any.whl
```{{execute}}

Alright, it's question time:
- What is _in_ the wheel? Is it what you expect?
- What _isn't_ in the wheel that we've been working on? Why?
