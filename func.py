import discord
import main
participants=[]
battleon=False


def hi(message):
  msg=message.channel.send('Hello {0.author.mention}!'.format(message))
  return msg

def kill(message):
  text=message.content
  text=text.split()
  msg= message.channel.send(f'You have killed {text[1]}. He is a flop.')
  return msg
  
async def chnick(member: discord.Member, nick):
    await member.edit(nick=nick)

def battle(message):
  global battleon
  global participants
  if battleon==False:
    msg= message.channel.send(f'Battle was been called, ready up!')
    participants=[]
    battleon=True
    return msg
  elif battleon==True:
    msg=message.channel.send(f'There is another battle in progress.')
    return msg




async def participantlist(message):
  for participant in participants:
    await message.channel.send(participant.mention)

async def yes(message):
  global battleon
  if battleon==True:
    if (message.author in participants):
      await message.channel.send(f"{message.author.mention} You're already participating!\n{len(participants)}/10 ready.")
    else:
      participants.append(message.author)
      await message.channel.send(f'{message.author.mention} has joined the battle!\n{len(participants)}/10 ready.') 
      if len(participants)==10:
        await message.channel.send('Battle has began! The following people are participating:')
        await participantlist(message)
        battleon=False

def endbattle(message):
  global battleon
  if battleon==True:
    battleon==False
    return message.channel.send('Awww. What a let down.')
  else:
    return message.channel.send("There's no battle on y'a flop!")


def theGrace(message):
  msg= message.channel.send(f'May the grace of our Lord David Wang be with us all everymore')
  return msg

