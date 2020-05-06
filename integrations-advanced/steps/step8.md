(You can find our completed solution in the `/workspace/solution` folder, as generated from the steps outlined below.)

# Check

Edit the `github_repo/datadog_checks/github_repo/github_repo.py` file and submit a service check every time you raise an exception or an error.

In our example, we created the following variable `SERVICE_CHECK_NAME = "github_repo.up"` and we updated the `handle_exception` method:

![github_repo-6](https://github.com/DataDog/LearningLabs/blob/master/integrations-advanced/assets/github_repo-6.png)

Do not forget to also submit the service check when the integration is running correctly.

![github_repo-7](https://github.com/DataDog/LearningLabs/blob/master/integrations-advanced/assets/github_repo-7.png)

# Test

Add the following code to `github_repo/tests/test_github_repo.py`:

![test_github_repo-3](https://github.com/DataDog/LearningLabs/blob/master/integrations-advanced/assets/test_github_repo-3.png)

__NOTES:__ 

- Replace `<YOUR_ACCESS_TOKEN>` with your Github Access Token.
- The `aggregator` stub is created by default and can be used to assert what is being submitted by the check method. You just need to add it as method parameter—like we did for `instance`.

