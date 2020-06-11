While the unit tests helped us to validate discrete elements of code, they don't help us to understand whether the code actually does what it's supposed to do—that's where integration tests come in. (And, yes, it's a little confusing that we're about to write integration tests for an integration, but [naming things is hard](https://www.martinfowler.com/bliki/TwoHardThings.html).)

The idea behind an integration test is that it tests the functionality of the program in question—in this case, how the integration works with regard to the thing it's meant to monitor. Without getting too far into the details, integration tests generally imply the execution of commands and interpretation of results, which further implies sources and targets for that data.

In other words, we're going to set up a scenario where the functionality of the Agent integration is tested. Can it actually look for a string on a web page? Well, we won't know until we have a web page to access, so let's start there!
