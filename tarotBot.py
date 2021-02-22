# tarotBot.py
import os
import sys
import random
import asyncio
import shelve
import discord
from datetime import datetime
from dotenv import load_dotenv
from randomCard import *
from peace import *
from test import *
from defs import *
from draw import *
from switchDeck import *
from moon import *
from daily import *
from spreads import *
from help import *
from majors import *
from sigils import *
from vibes import *
import random
from serverSettings import *

class Card:
    def __init__(self, name, up, rev, upB, revB, pic):
        self.name = name
        self.up = up
        self.rev = rev
        self.upB = upB
        self.revB = revB
        self.pic = pic
    def prints(self):
        print("Name: " + self.name +" Up: " + self.up + " rev: "+ self.rev + " gen: "+self.upB + ' revB: '+self.revB + ' pic: '+ self.pic)



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

prefix = '!'
settings = "serverSettings.txt"
step = 1



biddy = {}
with open("detailedMeanings.txt",errors='ignore') as f:
    for line in f:
        #print(line)
        split = line.split('\t')
        #print(split)
        biddy[split[0]] = Card(split[0],split[1],split[2],split[3],split[4],split[5])

#print(meanings)

rider = {}
with open('scrubOut.txt',errors='ignore') as p:
    buffer = []
    for line in p:
        if(not(line == '\n')):
            #print(line)
            if('=====' in line):
                #print("card")
                buffer[1] = buffer[1][9:-1].lstrip().capitalize()
                buffer[2] = buffer[2][10:-1].lstrip().capitalize()
                #print(buffer)
                rider[buffer[0][:-1]] = Card(buffer[0][:-1],buffer[1],buffer[2],buffer[3][:-1],'n/a',buffer[4][5:-1])
                #meanings2[buffer[0]].prints()
                buffer = []
            else:
                buffer.append(line)
deckArts = [rider, biddy]

talkers = []
chances = []
with shelve.open(settings) as s:
    for x in s:
        if s[x]:
            talkers.append(x)
            chances.append(0)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!t help"))
    sigils()

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


    print(talkers)

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
        preferences = 'preferences.txt'
        words = biddy

        with shelve.open(preferences) as s:
            ma = str(message.author)
            if('cleansedata' in  message.content.lower()):
                s[ma] ={'art': "Rider"}
                await message.channel.send('Your data has been cleansed! :)')
                broken = True;
            if ma in s:
                if ('art') in s[ma]:
                    if s[ma]['art'] == 'Biddy':
                        art = biddy
                    elif s[ma]['art'] == 'Rider':
                        art = rider
                else:
                    art = rider
            else:
                art = rider

        meaningsChosen = (words, art)


        if (broken == False):
            if (message.content.startswith(prefix + 't help') or client.user.mention.lower()[:3] + " help" in message.content.lower()):
                print('helping')
                await help(message, client)

            elif 'TesT' in message.content.lower() and broken == False:
                print('testing')
                await test(message, meaningsChosen)
                broken = True

            elif('chooseart' in message.content.lower() and broken == False):
                print('art time')
                await chooseArt(message, preferences, client)
                broken = True

            elif('moonphase' in message.content.lower() and broken == False):
                print('mooning')
                await moon(message, True)
                broken = True

            elif('sleepmodenow'in message.content.lower() and broken == False):
                print('night night')

            elif 'draw' in message.content.lower() and broken == False: # get a draw
                print('Drawing')
                tmp = await draw(message, meaningsChosen, True, message.author, client)
                broken = True

            elif ('peace' in message.content.lower() and broken == False):
                print("Playing Peace")
                await peace(message, meaningsChosen)
                broken = True

            elif ('daily' in message.content.lower()):
                print('daily')
                await daily(message, meaningsChosen, preferences, client)

            elif ('spreads' in message.content.lower()):
                print('spreads')
                await spreads(message, meaningsChosen, client)

            elif ('majors' in message.content.lower()):
                print('majors')
                await majors(message, meaningsChosen, client)

            elif ('addvibe' in message.content.lower()):
                print('vibe adding')
                await vibeAdd(message, meaningsChosen, client)

            elif('serversettings' in message.content.lower()):
                print("settings")
                talks = await serverSettings(message, settings, client)
                if (talks):
                    with shelve.open(settings) as s:
                        global talkers
                        global chances
                        talkers.append(message.channel.guild.id)
                        chances.append(0)

            else:
                found = await defs(message, meaningsChosen, client)
                if (not found):
                    print("Pulling random")
                    await randomCard(message, meaningsChosen, client)
    else:
        global chance
        for x in range(len(talkers)):
            if talkers[x] == str(message.channel.guild.id):
                num = random.randint(0,100)
                print("Chance: "+ str(chances[x]) + " Num: "+ str(num))
                if(num <= chances[x]):
                    print("talking!")
                    meaningsChosen = (biddy, random.choice(deckArts))
                    chances[x] = 0
                    await randomCard(message, meaningsChosen, client)
                else:
                    chances[x] += step




client.run(TOKEN)
