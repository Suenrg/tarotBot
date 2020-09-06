# tarotBot.py
import os
import sys
import random

import discord
from dotenv import load_dotenv

class Card:
  def __init__(self, name, up, rev, upB, revB, pic):
    self.name = name
    self.up = up
    self.rev = rev
    self.upB = upB
    self.revB = revB
    self.pic = pic


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

prefix = '!'

meanings = {}
with open("detailedMeanings.txt",errors='ignore') as f:
    for line in f:
        print(line)
        split = line.split('\t')
        print(split)
        meanings[split[0]] = Card(split[0],split[1],split[2],split[3],split[4],split[5])

print(meanings)

async def draw(message, meanings):
    broken = False
    choice1 = random.choice(list(meanings.items()))
    choice2 = random.choice(list(meanings.items()))
    choice3 = random.choice(list(meanings.items()))
    button = await message.channel.send("Select 1, 2, or 3")
    await message.channel.send(file=discord.File('card back purple 3.png'))
    msg = await client.wait_for('message', timeout=30)
    msg = msg.content
    if msg == "1":
        card = meanings[choice1[0]]
    elif msg == "2":
        card = meanings[choice2[0]]
    elif msg == "3":
        card = meanings[choice3[0]]
    else:
        await message.channel.send('I didn\'t get that :( ')

    if broken == False:
        drawn = card
        await message.channel.send(drawn.pic)
        if rev == False:
            await message.channel.send("*" + drawn.name + "*\n**Upright:** ***" + drawn.up + "***")
            if 'full' in message.content.lower():
                string = drawn.upB
                firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                await message.channel.send("```" + firstpart + "```")
                await message.channel.send("```" + secondpart + "```")
    broken = True

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith(prefix + 't') or '> ' in message.content.lower(): #check for prefix
        print(message)
        print (message.content.lower())
        print (message.mentions)
        print("====================================")
        broken = False
        if 'exit' in message.content.lower():
            await message.channel.send("Shutting down")
        #    sys.exit()
        rev = False #keeps track of reversed

        if (broken == False and (message.content.startswith(prefix + 't help') or '> help' in message.content.lower())):
            broken = True
            await message.channel.send('Hi! Thanks for asking for help, my name is Gaia!\nHere is a list of my commands:\n*!t two of wands* : this command will give you the definition of the card! add full to see the longer description, and add rev to see reversed.\n*!t random [prompt]* or *@tarotBot [prompt]* : this will pull a random card for you, pertaining to the prompt.\n*!t draw [prompt]* : draws three cards randomy and asks you to choose one.')

        if ('random' in message.content.lower() or '> ' in message.content.lower()) and broken == False: # get a quick random card
            choice = random.choice(list(meanings.items()))
            card = meanings[choice[0]]
            await message.channel.send(card.pic)
            await message.channel.send("Gaia gives you *" +card.name + "*")
            await message.channel.send("**Upright:** ***" + card.up + "***")
            if 'full' in message.content.lower():
                string = card.upB
                firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                await message.channel.send("```" + firstpart + "```")
                await message.channel.send("```" + secondpart + "```")
            broken = True

        if ('peace' in message.content.lower() and broken == False):
            print('kendale')


        if 'draw' in message.content.lower() and broken == False: # get a draw
            await draw(message, meanings)



        if 'reversed' in message.content.lower() or'rev' in message.content.lower(): # read a cards
            rev = True
        if (broken == False):
            response2 = ""
            found = False
            for x in meanings:
                if x.lower() in message.content.lower():
                    found = True
                    drawn = meanings[x]
                    await message.channel.send(drawn.pic)
                    if rev == False:
                        await message.channel.send("*" + drawn.name + "*\n**Upright:** ***" + drawn.up + "***")
                        if 'full' in message.content.lower():
                            string = drawn.upB
                            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                            await message.channel.send("```" + firstpart + "```")
                            await message.channel.send("```" + secondpart + "```")

                    else:
                        await message.channel.send("*" + drawn.name + "*\n**Reversed:** ***" + drawn.rev + "***")
                        if 'full' in message.content.lower():
                            string = drawn.revB
                            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                            await message.channel.send("```" + firstpart + "```")
                            await message.channel.send("```" + secondpart + "```")

                    #break
            if (found==False):
                await message.channel.send("Are you sure you wrote the card correctly?")



client.run(TOKEN)
