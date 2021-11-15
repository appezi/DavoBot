import os
import discord
import func
import discord.utils

TOKEN = os.environ['TOKEN']

intents = discord.Intents(messages=True, guilds=True, members=True)
intents.typing = False
intents.presences = False
intents.members = True

prayer=False
sender=None
prayed=None
goddem=False

quotes=[]

client = discord.Client(intents=intents)

with open('quotes.txt', 'r') as f:
  for line in f:
    quotes.append(line.strip())

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  global prayer
  global sender
  global prayed
  global goddem

  davoLimit = False
  text=message.content
  text = text.lower()  

  if text.startswith('!battle'):
    await func.battlestart(message)

  if text.startswith('!vote'):
    await func.vote(message)

  if text.startswith('!shares'):
    await func.shares(message)

  if text.startswith('!trade'):
    await func.trade(message)

  if text.startswith('!yes'):
    await func.yes(message)

  if text.startswith('!endbattle'):
    await func.endbattle(message)

  if text.startswith('!chnick'):
    text=text.split()
    text=text[2:]
    text=' '.join(text)
    await func.chnick(message, message.mentions[0], text)

  if text.startswith('!search'):
    gif= await func.search_gifs(text.split()[1:])
    await message.channel.send(gif)

  if text.startswith('!balance') or text.startswith('!bal'):
    await func.balance(message)

  if text.startswith('!work'):
    await func.work(message)

  ##No Other Functions Under This ONE!!!
  if text.startswith('!'):
    text=list(text)[1:]
    text=''.join(text)
    if text.isnumeric() == True:
      await func.setx(text, message)

  if text.startswith('!'):
    await message.channel.send("Error!")

client.run(TOKEN)