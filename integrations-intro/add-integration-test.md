Now we'll use the configuration elements defined in the previous step to actually implement an integration test. Head back to the [Datadog integration documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#building-an-integration-test) and look for the second part of `awesome/tests/test_awesome.py` (the one that starts with `@pytest.mark.integration`), then add it to our local copy of that same file.

In general, it's good policy to look before you leap, so here are some things to consider:
- This is an integration test—how is that specified?
- How does it know to use the Docker environment for this test?
- Which two states are being tested (and which is _not_)?
- Where does the `instance` parameter come from?
- Bonus: What is the `aggregator` parameter?
