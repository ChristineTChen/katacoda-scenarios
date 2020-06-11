Functional code is necessary but insufficient—we also need to be able to _test_ that functionality. There are a lot of differing opinions on when and how to write tests during the development cycle, but no matter how you feel about the subject, one thing is always true: if you want your integration to be included in a Datadog repository (such as extras), it must have test coverage.

There are two basic types of tests: unit tests that cover discrete elements of of functionality, and integration tests that execute the check method and verify proper data collection. Datadog uses pytest and tox to build and run the test harness, if those details are important to you. 🙂

The scaffolding put some test-related files into place, so let's take a look:
```
tree $HOME/dd/integrations-extras/awesome/tests/
```{{execute}}

`test_awesome.py` sounds like what we want! Let's take a closer look…
