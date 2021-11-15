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