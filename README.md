#Prerequisites

[Install Python 3.](https://www.python.org)

[Install the Async branch of Discord.py.](https://github.com/Rapptz/discord.py/tree/async)

#Download

[Download the latest version of JonTronTron and place it in a folder by itself.](https://github.com/Hamsterface/jontrontron/archive/master.zip)

#Configuration

Edit config.json as such, filling in any necessary information:

`configs/config.json`
```
{
    "email" : "email@address.com",
    "password" : "This is your bot password.",
    "owner_id" : "Place your Discord ID here.",
	"channels" : [
		"place a list of channel ids as a whitelist to speak in here",
		"they will look like:",
		"12345674536628194"
	],
	"quit_command" : "a regular expression the owner can use to shut down the bot"
}
```

#Activation

Run `main.py` in Python 3.

Congratulations, you have a ~~JonTronTron~~ DreamcastBot.
