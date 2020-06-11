As with the check logic, there's some great sample code for the tests in the [Datadog documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#writing-tests). Go ahead and paste that code into `awesome/tests/test_awesome.py`.

And, as before, here are some good questions to ask yourself about that code:
- What's being imported? What's purpose might it serve?
- What does the line that starts with `@` mean?
- What elements are being tested, and what happens if they fail?
