import os
import discord
import func
from replit import db
import random
import asyncio
import discord.utils
from discord.utils import get

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

  davo = await message.guild.fetch_member(606748122378403844)
  if message.author == davo:
    number = random.randint(20)
    if number == 5:
      await message.channel.send("All Hail Davo")
    if number == 3:
      await message.channel.send("What is life without our gracious lord Davo")     

    if number == 13:
      await message.channel.send("Davo bot likes Davo...yum")   
    if number == 12:
      await message.channel.send("SHUT UP JEHIEL!")   
    


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
    if prayer == True:
      await message.channel.send('There is already a prayer!')
    else:
      await message.channel.send('Please type your prayer!')
      sender=message.author
      prayer=True
      while goddem==False:
        await asyncio.sleep(0.5)
      await func.pray(message, prayed)
      prayer=False
      sender=None
      prayed=None
      goddem=False

  if text.lower().startswith('!iq'):
    await message.channel.send('Testing your IQ')
    counter=0
    while counter<6:
      await asyncio.sleep(1)
      await message.channel.send('.')
      counter+=1
    will =await message.guild.fetch_member(391376093527015434)
    dav = await message.guild.fetch_member(606748122378403844) 
    if message.author==will:
      await message.channel.send("Results are in!\nOMG ur IQ is still lower than Davo's and you thought you can trick the great DAVO bot SHAME on you...")
      await asyncio.sleep(2)
      await message.channel.send("You're still a big big flop tho...")
    elif message.author==dav:
      await message.channel.send("You're IQ is equal to Davo's... Wait a second...")
    else:
      await message.channel.send("Results are in!\nYour IQ is less than Davo's ya flop")

  if text.startswith('!roast'):
    user=message.mentions[0]
    await func.roast(message, user)

  if text.startswith('!balance'):
    await func.balance(message)

  if text.startswith('!work'):
    await func.work(message)

  ##No Other Functions Under This ONE!!!
  if text.startswith('!'):
    text=list(text)[1:]
    text=''.join(text)
    if text.isnumeric() == True:
      await func.setx(text, message)
  
  if (prayer == True) and (message.author==sender):
    prayed=message.content
    goddem=True

  if text.startswith('!'):
    await message.channel.send("That isn't a command ya flop!")

@client.event
async def on_member_update(before, after):
  if before.nick=='HamiltonFanGirl':
    await after.edit(nick='HamiltonFanGirl')

client.run(TOKEN)