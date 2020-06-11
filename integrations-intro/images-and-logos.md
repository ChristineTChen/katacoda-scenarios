If you've ever installed an Integration in the past, you've probably noticed that they tend to have images associated with them; certainly a logo, but also other graphical elements as well. While these images are superflous during the development stage, there are ultimately three mandatory images that need to be included with any integration meant for consideration upstream.

The [Datadog integration documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#add-images-and-logos) describes these files and their formats in detail. For our purposes, however, let's keep it simple and let [somebody else](https://placedog.net/) do the work. 😉
```
cd $HOME/dd/integrations-extras && mkdir -p awesome/images awesome/assets/logos
curl https://placedog.net/200/128/\?random > awesome/assets/logos/saas_logos-bot.png
curl https://placedog.net/120/60/\?random > awesome/assets/logos/saas_logos-small.png
curl https://placedog.net/128/128/\?random > awesome/assets/logos/avatars-bot.png
```{{execute}}
