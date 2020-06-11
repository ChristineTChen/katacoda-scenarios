Now we'll run the integration test on its own:
```
ddev test -m integration awesome
```{{execute}}

This takes a little longer than the unit test since it needs to spin up a Docker environment—but it's still pretty quick. It's possible that you ran into a "linter failure", which looks like this:
```
ERROR:   style: commands failed
```

If you didn't, congratulations! If you _did_, it's very easy to fix; the tooling can help or even do it for you. Take a look at the `-s` and `-fs` switches:
```
ddev test -h
```{{execute}}

Looks promising! Let's try it out:
```
ddev test -fs awesome
```{{execute}}

And that's it: we now have a functional integration, complete with tests! We're done with code (for now), so let's move on to the rest of the bits and pieces that make up a complete integration…
