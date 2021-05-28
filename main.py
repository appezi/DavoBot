import os
import discord
import func

client = discord.Client()
TOKEN = os.environ['TOKEN']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  text=message.content

  if text.startswith('!hi'):
    await func.hi(message)

  if text.startswith('!kill'):
    await func.kill(message)

  if text.startswith('!battle'):
    await func.battle(message)

  if text.startswith('!yes'):
    await func.yes(message)

  if text.startswith('!endbattle'):
    await func.endbattle(message)

  if text.startswith('!theGrace'):
    await func.theGrace(message)
  
  if text.startswith('!chnick'):
    await func.chnick(message)

client.run(TOKEN)