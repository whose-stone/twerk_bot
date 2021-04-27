import discord
import os
import requests
from heartbeat import beat
import random

client = discord.Client()
my_secret = os.environ['TOKEN']

gangsta = ['pimp','hood rich','gangsta', 'RAIN', 'that\'s hot', '...please']

whome = ['Drop_it']

hellos = ['everyone', 'hello', 'Hey', 'hey']

goodbyes = ['goodbye', 'laters', 'I\'m out', 'got to go', 'gotta go']

john = ['tweak']

shutdown = ['turn homie off', 'sucky bot', 'shut you down', 'horrible bot']

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

@client.event
async def on_message(message):

  if message.content.endswith("Homie?") == True:
    predictions = ["No way", "Absolutely", "Maybe", "Of course", "Never", "Seek the Savage one, only he can help you.", "Always", "It will be so.","My sources say, YES."]
    await message.channel.send(f"The answer to your quesiton is\:  {random.choice(predictions)}")

  if any(word in message.content for word in shutdown):
    predictions = ["I will cut you.", "Imma shut you down!", "I'd like to see you try.", "You wish you could turn me off.", ]
    await message.channel.send(f"{random.choice(predictions)}")

  if message.content.find("TWERK") != -1:
    await message.channel.send('Ask me nicely.', file=discord.File('askmenice.gif'))

  if message.content.find("story") != -1:
    await message.channel.send('It was Thursday the 12th...there I was...at a pizza party...')
  
  if message.content.find("weather") != -1:
    await message.channel.send('\*LOOKS OUT WINDOW\*  I donno...sunny?')
  
  if any(word in message.content for word in hellos):
    await message.channel.send('Hola.')

  if any(word in message.content for word in goodbyes):
    await message.channel.send('Later fool.')
  
  if any(word in message.content for word in john):
    await message.channel.send(file=discord.File('tweakgif.gif'))
  
  if any(word in message.content for word in whome):
    await message.channel.send('Yeah?')

  if any(word in message.content for word in gangsta):
    await message.channel.send(file=discord.File('twerking3.gif'))

@client.event
async def on_member_remove(member):
  await message.channel.send("I was tired of {} anyway.".format(member))



#beat()  turn off server
client.run(my_secret)