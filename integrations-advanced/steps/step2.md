First, you need to install the PyGithub dependency:
- `pip install PyGithub`{{execute}}

Then, you can run the following script within the Python REPL to print the repo name:
- `python`{{execute}}

<pre class="file" data-target="clipboard">
from github import Github
token = "ACCESS_TOKEN"
g = Github(token)
r = g.get_repo("Datadog/integrations-extras")
r.name
</pre>

- (Forget how to exit the REPL? Type `exit` for a hint!)
