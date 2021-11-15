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
  with open('Data/roasts.txt', 'r') as f:
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
    with open('Data/roasts.txt', 'w') as f:
      for line in roasts:
        f.write(line)
    await message.channel.send('Quote has been deleted! Ya Flop!')
##End Davobot Functions