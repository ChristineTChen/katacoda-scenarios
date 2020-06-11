The various Datadog Agent integrations fall into one of two categories: "core" and "extras". Core integrations are generally developed and maintained by Datadog directly. Extras integrations are developed and maintained by the community—in other words, *you*! All of the code is open source in both cases. Let's start by cloning a copy of [the extras](https://github.com/DataDog/integrations-extras).

By default, that tooling expects you to be working in the `$HOME/dd/` directory—this is optional and can be adjusted via configuration later, but we'll leave it there for now:
```
mkdir $HOME/dd && cd $HOME/dd
git clone https://github.com/DataDog/integrations-extras.git
```{{execute}}
