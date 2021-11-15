import discord
from replit import db
import os
import giphy_client
from giphy_client.rest import ApiException
import random
import asyncio
import csv

intents = discord.Intents(messages=True, guilds=True, members=True)

prayer=False
client=discord.Client(intents=intents)
participants=[]
players =[]
battleon=False
partcount=False
x=10
giphy_token = os.environ['giphykey']
placeHolderID =1

##Older, Easier Functions
api_instance = giphy_client.DefaultApi()
async def search_gifs(query):
  try:
    response = api_instance.gifs_search_get(giphy_token, query, limit=50)
    lst = list(response.data)
    gif = random.choices(lst)
    return gif[0].url

  except ApiException as e:
    return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

def hi(message):
  msg=message.channel.send('Hello {0.author.mention}!'.format(message))
  return msg

def kill(message):
  text=message.content
  text=text.split()
  msg= message.channel.send(f'You have killed {text[1]}. He is a flop.')
  return msg
  
async def chnick(message, person, newnick):
  await person.edit(nick=newnick)
  await message.channel.send(str(message.mentions[0])+' Changed Into '+newnick)
##End Older, Easier Functions

##Bennet Corporation Exclusive
def shares(message):
  with open('shares.csv', 'r') as f:
    data=csv.DictReader(f)
    finalMess=''
    for row in data:
      finalMess+=row['Name']+': '+str(row['Shares'])+'\n'
  return message.channel.send(finalMess)

def trade(message):
  member1=message.author.id
  member2=message.mentions[0].id
  return print(member1, member2)

async def vote(message):
  counter = 0
  topic = message.content.split(' ')[1:]
  topic = topic[:-1]
  topic=' '.join(topic)
  timeLimit=float(message.content.split()[-1])
  msg=await message.channel.send(f"{topic}")
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')
  msg = await msg.channel.fetch_message(msg.id)
  
  while (counter<int(timeLimit*60)):
    counter+=1
    await asyncio.sleep(1)

  msg = await msg.channel.fetch_message(msg.id)
  num1=msg.reactions[0].users()
  num1users=[]
  async for dude in num1:
    num1users.append(dude.id)

  num2=msg.reactions[1].users()
  num2users=[]
  async for dude in num2:
    num2users.append(dude.id)

 #list of users voting Yes
  num1users=num1users[1:]

  #list of users voting No
  num2users=num2users[1:]

  await message.channel.send('The users who voted yes:')
  for user in num1users:
    await message.channel.send(f'<@{user}>')
  
  await message.channel.send('The users who voted no:')
  for user in num2users:
    await message.channel.send(f'<@{user}>')
  
  with open("shares.csv", 'r') as f:
    reader=csv.DictReader(f)
    num1Total=0
    num2Total=0
    print(num1users)
    print(num2users)
    for line in reader:
      if int(line['User']) in num1users:
        num1Total+=int(line['Shares'])
      if int(line['User']) in num2users:
        num2Total+=int(line['Shares'])
  
  if num1Total>num2Total:
    await message.channel.send(f"The vote won with the total {num1Total}-{num2Total}")
  elif num1Total<num2Total:
    await message.channel.send(f"The vote lost with the total {num2Total}-{num1Total}")
  else:
    await message.channel.send(f"The vote drew with the total {num1Total}-{num2Total}")

async def balance(message):
  user=message.author
  if (str(user)+'balance') not in db.keys():
    db[str(user)+'balance']=0
  await message.channel.send(f"{user.mention} You have {db[str(user)+'balance']} Bennett Cash.")

async def work(message):
  user = message.author
  if (str(user)+'balance') not in db.keys():
    db[str(user)+'balance']=0
  gain=random.randrange(-5, 10, 1)
  db[str(user)+'balance']+=gain
  await message.channel.send(f"{user.mention} You have gained {gain} Bennett Cash!")
  await balance(message)
##End Bennett Exclusive Functions

##Battle Royale Functions
async def setx(text, message):
  global x
  global battleon
  global partcount
  if partcount==True:
    x=int(text)
    if x>1:
      await message.channel.send(f'{x} Participants will be allowed.')
      partcount=False
    else:
      await message.channel.send("That's too few people!")
  elif battleon ==True:
    await message.channel.send("Participant number already set.")
  else:
    await message.channel.send('No battle in progress.')

def battlestart(message):
  global battleon
  global participants
  global partcount
  if battleon==False:
    msg= message.channel.send(f'Battle was been called, ready up!\nHow many participants?')
    partcount=True
    participants=[]
    battleon=True
    return msg
  elif battleon==True:
    msg=message.channel.send(f'There is another battle in progress.')
    return msg

  

async def participantlist(message):

  for participant in participants:
    await message.channel.send(participant.mention)

async def initialise():
  for participant in participants:
    if participant not in db.keys():
      db[str(participant)+'stats']={'strength':10, 'speed':10, 'hp':10}
    await participant.send(f"These are your stats:")
    for stat in db[str(participant)+'stats']:
      await participant.send(f"{stat.capitalize()}: {db[str(participant)+'stats'][stat]}")

async def yes(message):
  global battleon
  global x
  global partcount
  partcount=False
  if battleon==True:
    if (message.author in participants):
      await message.channel.send(f"{message.author.mention} You're already participating!\n{len(participants)}/{x} ready.")
    else:
      participants.append(message.author)
      await message.channel.send(f'{message.author.mention} has joined the battle!\n{len(participants)}/{x} ready.') 
      if len(participants)==x:
        await message.channel.send('Battle has began! The following people are participating:')
        await participantlist(message)
        await initialise()
        battleon=False

def endbattle(message):
  global battleon
  if battleon==True:
    battleon=False
    return message.channel.send('Awww. What a let down.')
  else:
    return message.channel.send("There's no battle on y'a flop!")
##End Battle Royale Functions

##Outdated Davobot Functions (Fun)
async def pray(message, prayer):
  counter=0
  will=await message.guild.fetch_member(500558569704521728)
  msg=await will.send(str(message.author)+f" has prayed to you:\n'{prayer}'")
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')
  
  msg = await msg.channel.fetch_message(msg.id)
  
  while (counter<86400) and (msg.reactions[0].count==1) and (msg.reactions[1].count==1):
    counter+=1
    await asyncio.sleep(1)
    msg = await msg.channel.fetch_message(msg.id)

  msg = await msg.channel.fetch_message(msg.id)
  num1=msg.reactions[0].count
  num2=msg.reactions[1].count

  if num1>num2:
    await message.channel.send(f"Prayer Granted!\nYou prayed that: '{prayer}'")
  elif num2>num1:
    await message.channel.send(f"Prayer Denied!\nYou prayed that: '{prayer}'")
  else:
    await message.channel.send(f"Prayer Ignored.\nYou prayed that: '{prayer}'")

async def roast(message, user):
  roasts=[]
  with open('roasts.txt', 'r') as f:
    for roast in f:
      roasts.append(roast)
  lol=random.choice(roasts)
  msg=await message.channel.send(str(user.mention)+' '+lol)
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')
  await msg.add_reaction('🚫')
  msg = await msg.channel.fetch_message(msg.id)
  counter=0
  while (counter<100) and (msg.reactions[2].count==1):
    counter+=1
    await asyncio.sleep(1)
    msg = await msg.channel.fetch_message(msg.id)
  if msg.reactions[2].count>1:
    roasts.remove(lol)
    n=0
    with open('roasts.txt', 'w') as f:
      for line in roasts:
        f.write(line)
    await message.channel.send('Quote has been deleted! Ya Flop!')
##End Davobot Functions