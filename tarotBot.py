# tarotBot.py
import os
import sys
import random

import discord
from dotenv import load_dotenv

from datetime import datetime

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
        await message.channel.send("*" + drawn.name + "*\n**Upright:** ***" + drawn.up + "***")
        if 'full' in message.content.lower():
            string = drawn.upB
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            await message.channel.send("```" + firstpart + "```")
            await message.channel.send("```" + secondpart + "```")
    broken = True
    return(card)

async def randomCard(message, meanings):
    reversed = False
    seed = message.content + str(datetime.now())
    random.seed(seed)
    choice = random.choice(list(meanings.items()))
    card = meanings[choice[0]]
    if 'rev' in message.content.lower():
        reversed = bool(random.getrandbits(1))
    if reversed == False:
        await message.channel.send(card.pic)
        await message.channel.send("Gaia gives you *" +card.name + "*")
        await message.channel.send("**Upright:** ***" + card.up + "***")
        if 'full' in message.content.lower():
            string = card.upB
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            await message.channel.send("```" + firstpart + "```")
            await message.channel.send("```" + secondpart + "```")
    else:
        await message.channel.send(card.pic)
        await message.channel.send("Gaia gives you *" +card.name + "* Reversed")
        await message.channel.send("**Reversed:** ***" + card.rev + "***")
        if 'full' in message.content.lower():
            string = card.revB
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            await message.channel.send("```" + firstpart + "```")
            await message.channel.send("```" + secondpart + "```")


async def peace(message, meanings):
    if(len(message.mentions) != 2):
        await message.channel.send("I'm sorry, please use the correct format and @ both players and nobody else")
    p1 = message.mentions[0]
    p2 = message.mentions[1]

    s1 = 0
    s2 = 0
    round = 1

    while (s1 < 2 and s2 < 2):
        await message.channel.send("Peace! Round " + round + "\n" + p1.nick +": " + s1 + ", " + p2.nick + ": " + s2)
        await message.channel.send(p1.nick + " draws!")
        card1 = await draw(p1.nick, meanings)
        await message.channel.send(p2.nick + " draws!")
        card2 = await draw(p2.nick, meanings)
        m1 = await message.channel.send(p1.nick + "\'s card: " + card1.pic)
        await bot.add_reaction(m1, "\:peace:")
        m2 = await message.channel.send(p2.nick + "\'s card: " + card2.pic)
        await bot.add_reaction(m2, "\:peace:")
        s1 += 1
        round += 1
    await message.channel.send("The game is over! I haven't coded this yet")





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
        broken = False #keep track of flow
        rev = False #keeps track of reversed

        if (broken == False and (message.content.startswith(prefix + 't help') or client.user.mention.lower() + " help" in message.content.lower())):
            broken = True
            await message.channel.send('Hi! Thanks for asking for help, my name is Gaia!\nHere is a list of my commands:\n*!t two of wands* : this command will give you the definition of the card! add full to see the longer description, and add rev to see reversed.\n*!t random [prompt]* or *@tarotBot [prompt]* : this will pull a random card for you, pertaining to the prompt.\n*!t draw [prompt]* : draws three cards randomy and asks you to choose one.')

        if ('random' in message.content.lower() or client.user.mention.lower() in message.content.lower()) and broken == False: # get a quick random card
            await randomCard(message, meanings)
            broken = True


        if 'draw' in message.content.lower() and broken == False: # get a draw
            tmp = await draw(message, meanings)
            broken = True


        if ('peace' in message.content.lower() and broken == False):
            print('kendale')

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
