# mothermayi-rescuetime

A rescuetime plugin for mothermayi (https://github.com/EliRibble/mothermayi). This adds a post-commit hook which will send the title of your commit message (the first line) to recuetime every time you commit. You configure it by adding the rescuetime API key to your mothermayi config

For example, you may want to put this in `~/.mothermayi`

```
rescuetime:
	api_key: abc-123
```

You can get your api key from Rescuetime. I'm on a plane, so I'm not going to look up how or where.
