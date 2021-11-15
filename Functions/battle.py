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