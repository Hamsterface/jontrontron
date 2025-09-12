# Prerequisites

[Install Python 3.](https://www.python.org)

[Install the Async branch of Discord.py.](https://github.com/Rapptz/discord.py/tree/async)

# Download

[Download the latest version of JonTronTron and place it in a folder by itself.](https://github.com/Hamsterface/jontrontron/archive/master.zip)

# Configuration

Create a file with this name, filling in any necessary information:

`configs/config.json`
```
{
  "token" : "xxxxxx",
  This is your bot's auth token
  
  "manager_ids" : [1234567890, 2345678901],
  This is a list of user IDs you want to be able to shut down the bot
  
  "quit_command" : "^jttstop$",
  This is the command to send to shut down jtt
  
  "reload_command" : "^jttreload$",
  This is the command to send to reload the responses
  
  Commands use the same formatting as the responses; all non-alphanumeric characters are ignored
  
  "reload_response" : "Responses updated!",
  Message to send when responses are reloaded. If you leave an empty string it will be silent.
  
  "change_avy" : "off",
  Set to "on" to enable changing avatar. All other values are disabled.
  
  "channel_whitelist" : [
    1234567890,
    2345678901,
    3456789012
  ]
  List of channel IDs to respond to messages in.
}
```

# Activation

Run `main.py` in Python 3.

Congratulations, you have a JonTronTron.
