import os
import discord
import func
from replit import db

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
    await func.battlestart(message)

  if text.startswith('!yes'):
    await func.yes(message)

  if text.startswith('!endbattle'):
    await func.endbattle(message)

  if (text.startswith('!theGrace')) or (text.startswith('!grace')):
    await func.theGrace(message)
  
  if text.startswith('!chnick'):
    text=text.split()
    text=text[2:]
    text=' '.join(text)
    await func.chnick(message, message.mentions[0], text)

  if text.startswith('!DavoceneCreed') or text.startswith('!theDavoceneCreed') or text.startswith('!creed'):
    await func.theDavoceneCreed(message) 

  if text.startswith('!Genesis') or text.startswith('!genesis'):
    await func.genesis(message)

  if text.startswith('!search'):
    gif= await func.search_gifs(text.split()[1:])
    await message.channel.send(gif)

  if text.startswith('!'):
    text=list(text)[1:]
    text=''.join(text)
    if text.isnumeric() == True:
      await func.setx(text, message)

client.run(TOKEN)