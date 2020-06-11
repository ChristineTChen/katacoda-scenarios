With Docker out of the way, we can concentrate on the test itself. There are two separate but related components to consider: the _configuration_ of the test, and the _instantiation_ of that configuration (i.e. actually running the test).

We'll start with the configuration. Thinking back to the test-related files that the harness prepared, do you recall the `conftest.py` file? That's a great spot to put configuration for tests. 😀

You know the drill by now: look in the [Datadog integration documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#building-an-integration-test) for `awesome/tests/conftest.py`, then use your copy and paste super-powers.

Introspection is a super-power, too. So here are some questions to ponder:
- What's being imported? What is their purpose?
- What global variables are being declared, and why?
- How useful are in-line comments in code? (Answer: _very_.)
- Extra credit: why is `yield` used in `dd_environment()` instead of `return`?
