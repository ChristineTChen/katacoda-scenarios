The moment of truth: let's build and run the test harness! We will use the development toolkit to help us with this:
```
ddev test awesome
```{{execute}}

This will take a little longer to run the first time then on subsequent runs as the build phase only needs to happen once. Feel free to execute the test again to see the difference!

Finally, note the last few lines of output: tests were run for two different versions of Python, and there's also a _style checker_ to help us keep the style and syntax of the integrations consistent.
