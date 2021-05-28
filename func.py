import discord
participants=[]
battleon=False

#<editor-fold desc="Description">
def hi(message):
  msg=message.channel.send('Hello {0.author.mention}!'.format(message))
  return msg

def kill(message):
  text=message.content
  text=text.split()
  msg= message.channel.send(f'You have killed {text[1]}. He is a flop.')
  return msg
  
async def chnick(message,person, newnick):
  await person.edit(nick=newnick)
  await message.channel.send(str(message.mentions[0])+' Changed Into '+newnick)

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
  return message.channel.send(f'May the intelligence of our lord Davo Wang, his weird Reddit facts, and the fellowship of his Sketchup skills be with us all, ever more, Amen.')


async def theDavoceneCreed(message):
    await message.channel.send('\n We believe in one Davo the Messiah, the peculiar child, the bear and dolphin lover, the true ego inspector, the solver of all that has been solved and unsolved.') 

    await message.channel.send('\nWe believe in one Genius Child, Wavo Dang, the only prodigy of year 10, eternally begotten of his brain, thought from thought, gif from gif, animal sexual facts from animal sexual facts. Begotten, not made, of one brainwave with himself; through him all things were made in Sketchup. For us and for our damnation he came down from China, incarnate of a big brain and twig like body and became truly a Scots “Boy”. For our sake he was imported from Trinity; he suffered confusion and had no mates. On the third day he rose again in accordance with the Social norms; he ascended into having mates and is seated at the balcony of the S400’s. He will come again in pity to judge Michael and Company, and his Python game will have no end.') 

    await message.channel.send('\nWe believe in the brain of Davo, the intelligent, the giver of roasts, who proceeds from the peculiar child and the child prodigy, who with the peculiar child and the child prodigy is worshipped and glorified in IST class, who has spoken through his roasts. We believe in one holy catholic and apostolic S400s. We acknowledge there is no baptism for his forgiveness of sins. We look for the new hangouts constantly created, and the day when they finally stop appearing. Amen."') 


async def genesis(message):
  await message.channel.send('In the beginning, David created the template and scale. Now the workspace was formless and empty, emptiness was over the surface of the desktop, and the mouse of Davo was hovering over the screen. \n\nAnd David said, “Let there be dots,” and there were dots. Davo saw that the dots were good, and he connected the dots to each other. Davo called the dots “points,” and the connection he called “lines.” And there was length, and there was an angle—the first shape.')


  #</editor-fold>

