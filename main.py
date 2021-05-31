import os
import discord
import func
from replit import db
import random

client = discord.Client()
TOKEN = os.environ['TOKEN']

intents = discord.Intents(messages=True, guilds=True)
intents.typing = False
intents.presences = False


quotes=[]
with open('quotes.txt', 'r') as f:
  for line in f:
    quotes.append(line.strip())

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
    print(text.split()[1])

  if text.startswith('!battle'):
    await func.battlestart(message)

  if text.startswith('!yes'):
    await func.yes(message)

  if text.startswith('!endbattle'):
    await func.endbattle(message)

  if (text.startswith('!theGrace')) or (text.startswith('!grace')):
    await func.theGrace(message)

  if (text.startswith('!test')):
    print(message.author)

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

  if text.startswith('!messiah'):
    with open('messiah.png', 'rb') as f:
      img=discord.File(f)
      await message.channel.send(file=img)
    await message.channel.send("'"+' '.join(list(random.choices(quotes)))+"'")

  if text.startswith('!pray'):
    await func.pray(message)

  if text.startswith('!list'):
    listMem(message)

  if text.startswith('!'):
    text=list(text)[1:]
    text=''.join(text)
    if text.isnumeric() == True:
      await func.setx(text, message)
      
#message.guild.get_member("Williloooooooooooooooooooooooooo#9895")

def listMem(message):
  print("list")
  x = message.guild.members
  for member in x:
    print(member)

client.run(TOKEN)