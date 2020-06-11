There are lots of ways to accomplish our goal. One popular technique is to use Docker to spin up a very small, very lightweight environment that meets the needs of the testing scenario. In our case, we'll use it to set up and run a web server, query that server for a page, and then analyse the result acording to our check logic.

We'll start by setting up a Docker configuration. Head back to the Datadog integration documentation and check out [the docker-compose.yml file](https://docs.datadoghq.com/developers/integrations/new_check_howto/#building-an-integration-test). Copy and paste it to `awesome/tests/docker-compose.yml` for the win!

As always, it's good to ask some questions:
- Which web server software will be installed?
- What port will be exposed to our test harness?
