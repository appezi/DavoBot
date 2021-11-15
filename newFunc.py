from Functions import economy
from Functions import deprecated
from Functions import battle
import asyncio
##Bennet Corporation Exclusive
def shares(message):
  economy.shares(message)

def trade(message):
  economy.trade(message)

async def vote(message):
  await economy.vote(message)

async def balance(message):
  await economy.balance(message)

async def work(message):
  await economy.work(message)

async def search_gifs(query):
  await deprecated.search_gifs(query)

def hi(message):
   deprecated.hi(message)

def kill(message):
   deprecated.kill(message)
  
async def chnick(message, person, newnick):
  await deprecated.chnick(message, person, newnick)
  
async def setx(text, message):
  await battle.setx(text, message)

def battlestart(message):
  battle.battlestart(message)
  
async def participantlist(message):
  await battle.participantlist(message)

async def initialise():
  await battle.initialise()

async def yes(message):
  await battle.yes(message)

def endbattle(message):
  battle.endbattle(message)