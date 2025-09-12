import discord
import json
import string
import re
from random import choice

with open('configs/config.json') as data:
  config = json.load(data)

with open('configs/responses.json') as data:
  shitposts = json.load(data)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  print('Serving the following servers:')
  for g in client.guilds:
    print(' - {}'.format(g.name))

include = set(string.ascii_letters.join(string.digits))
current_avy = ''

@client.event
async def on_message(message):
  if message.author == client.user or message.channel.id not in config['channel_whitelist'] or message.author.bot:
    return

  s = ''.join(ch for ch in message.content if ch in include)
  if re.match(config['quit_command'], s, flags=re.I) and message.author.id in config['manager_ids']:
    await client.close()
  
  if re.match(config['reload_command'], s, flags=re.I) and message.author.id in config['manager_ids']:
    global shitposts
    
    with open('configs/responses.json') as z:
      shitposts = json.load(z)
    
    if config['reload_response']: # If reload_response is blank, this won't trigger.
      message.channel.send(config['reload_response'])
  
  for key in shitposts.keys():
    if re.match(key, s, flags=re.I):
      response = ""
      async with message.channel.typing():
        response = choice(shitposts[key])
        
        new_avy = 'hamtron.png'
        if isinstance(response, list):
          new_avy = response[1]
          response = response[0]
        
        if config['change_avy'] == "on" and new_avy != current_avy:
          with open(new_avy, 'rb') as img:
            try:
              await client.user.edit(
                username='JonTronTron',
                avatar=img.read()
              )
            except HTTPException as e:
              print('Failed to update avatar, reason: {}'.format(e.text))
      
        print('channel: {}, input :"{}", response: "{}"'.format(message.channel.name,s,str(response.encode('utf-8'))))
      await message.channel.send(response)


client.run(config['token'])
