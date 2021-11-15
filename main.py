import os
import discord
import newFunc
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

with open('Data/quotes.txt', 'r') as f:
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
    await newFunc.battlestart(message)

  if text.startswith('!vote'):
    await newFunc.vote(message)

  if text.startswith('!shares'):
    await newFunc.shares(message)

  if text.startswith('!trade'):
    await newFunc.trade(message)

  if text.startswith('!yes'):
    await newFunc.yes(message)

  if text.startswith('!endbattle'):
    await newFunc.endbattle(message)

  if text.startswith('!chnick'):
    text=text.split()
    text=text[2:]
    text=' '.join(text)
    await newFunc.chnick(message, message.mentions[0], text)

  if text.startswith('!search'):
    gif= await newFunc.search_gifs(text.split()[1:])
    await message.channel.send(gif)

  if text.startswith('!balance') or text.startswith('!bal'):
    await newFunc.balance(message)

  if text.startswith('!work'):
    await newFunc.work(message)

  ##No Other newFunctions Under This ONE!!!
  if text.startswith('!'):
    text=list(text)[1:]
    text=''.join(text)
    if text.isnumeric() == True:
      await newFunc.setx(text, message)

  if text.startswith('!'):
    await message.channel.send("Error!")

client.run(TOKEN)