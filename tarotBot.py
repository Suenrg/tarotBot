# tarotBot.py
import os
import sys
import random
import asyncio

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

async def draw(message, meanings, v):
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

    if v == False:
        await message.channel.send("You drew *"+card.name+"*")
        broken = True

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
    print("am I getting called?")
    reversed = False
    seed = message.content + str(datetime.now())
    random.seed(seed)
    choice = random.choice(list(meanings.items()))
    card = meanings[choice[0]]
    if 'rev' in message.content.lower():
        reversed = bool(random.getrandbits(1))
    if reversed == False:
        print('this should go twice')
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

    emoji = '☮️'
    endmoji = '🔚'


    while (s1 < 2 and s2 < 2):
        await message.channel.send("========================================================================== \n ***Peace! Round " + str(round) + "***\n" + str(p1.nick) +": *" + str(s1) + "*, " + str(p2.nick) + ": *" + str(s2) + "* \n ==========================================================================")

        await message.channel.send(str(p1.nick) + " draws!")
        card1 = await draw(message, meanings, False)
        await asyncio.sleep(1)

        await message.channel.send(str(p2.nick) + " draws!")
        card2 = await draw(message, meanings, False)
        await asyncio.sleep(1)

        m1 = await message.channel.send("==============================\n" + str(p1.nick) + "\'s card: " + card1.pic)
        await message.channel.send("**Upright:** ***" + card1.up + "***")
        await m1.add_reaction(emoji)

        m2 = await message.channel.send(str(p2.nick) + "\'s card: " + card2.pic)
        await message.channel.send("**Upright:** ***" + card2.up + "***")
        await m2.add_reaction(emoji)

        end = await message.channel.send("React to me to finish voting!")
        await end.add_reaction(endmoji)

        await message.channel.send("==========================================================================")


        ####################################### Code that handles reactions
        fin = False
        r1 = 0 # r1 score
        r2 = 0 # r2 score

        while(fin == False):
            def check(reaction, user):
                    return user != end.author and (user == p1 or user == p2)
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                print("timed out")
                fin = True
            else:
                if reaction.message.id == end.id:
                    #if reaction.emoji == endmoji:
                    #    print('endmoji')
                    fin = True
                elif reaction.message.id == m1.id:
                    #if reaction.emoji == emoji:
                    print('m1 score')
                    await message.channel.send(str(p1.nick) + "scores!")
                    r1 += 1
                elif reaction.message.id == m2.id:
                    #if reaction.emoji == emoji:
                    print('m2 score')
                    await message.channel.send(str(p2.nick) + "scores!")
                    r2 += 1
        #######################################

        if r1 >= r2:
            s1 += 1
        else:
            s2 += 1
        round += 1

    if s1 == 2:
        await message.channel.send(str(p1.nick) + " wins and finds peace")
        broken = True
    elif s2 == 2:
        await message.channel.send(str(p2.nick) + " wins and finds peace")
        broken = True
    broken = True

async def test(message, meanings):
    emoji = '\N{THUMBS UP SIGN}'
    mess = await message.channel.send("This is a test!")
    await mess.add_reaction(emoji)
    print(mess.reactions)

    def check(reaction, user):
            return user != mess.author and str(reaction.emoji) == emoji

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await message.channel.send('nobody reacted :(')
    else:
        await message.channel.send(':o you reacted to me!!! ^////^')
        print(mess.reactions)







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


    if message.content.startswith(prefix + 't') or client.user.mention.lower()[3:] in message.content.lower(): #check for prefix
        #print(client.user.mention.lower()[3:])
        print("====================================")
        print(message)
        print (message.content.lower())
        #print (message.mentions)
        print("====================================")
        broken = False #keep track of flow
        rev = False #keeps track of reversed

        if (broken == False and (message.content.startswith(prefix + 't help') or client.user.mention.lower()[:3] + " help" in message.content.lower())):
            broken = True
            await message.channel.send('Hi! Thanks for asking for help, my name is Gaia!\nHere is a list of my commands:\n*!t two of wands* : this command will give you the definition of the card! add full to see the longer description, and add rev to see reversed.\n*!t random [prompt]* or *@tarotBot [prompt]* : this will pull a random card for you, pertaining to the prompt.\n*!t draw [prompt]* : draws three cards randomy and asks you to choose one.')

        if 'test' in message.content.lower() and broken == False:
            print('testing')
            await test(message, meanings)
            broken = True

        if 'draw' in message.content.lower() and broken == False: # get a draw
            print('Drawing')
            tmp = await draw(message, meanings, True)
            broken = True


        if ('peace' in message.content.lower() and broken == False):
            print("Playing Peace")
            await peace(message, meanings)
            broken == True

        if ('random' in message.content.lower() or client.user.mention.lower()[3:] in message.content.lower()) and broken == False: # get a quick random card
            print("Pulling random")
            await randomCard(message, meanings)
            broken = True

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
