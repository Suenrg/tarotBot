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

async def draw(message, meanings2, v, userN, client):
    broken = False
    choice1 = random.choice(list(meanings2.items()))
    choice2 = random.choice(list(meanings2.items()))
    choice3 = random.choice(list(meanings2.items()))
    button = await message.channel.send("Select 1, 2, or 3")
    mess = await message.channel.send(file=discord.File('card back purple 3.png'))
    # msg = await client.wait_for('message', timeout=30)
    # msg = msg.content
    # if msg == "1":
    #     card = meanings[choice1[0]]
    # elif msg == "2":
    #     card = meanings[choice2[0]]
    # elif msg == "3":
    #     card = meanings[choice3[0]]
    # else:
    #     await message.channel.send('I didn\'t get that :( ')
    e1 = "1️⃣"
    e2 = "2️⃣"
    e3 = "3️⃣"
    await mess.add_reaction(e1)
    await mess.add_reaction(e2)
    await mess.add_reaction(e3)
    def check(reaction, user):
            return user != mess.author and (user == userN) and reaction.message.id == mess.id  
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        print("timed out")
        await message.channel.send("You forgot about me :(")
        broken = True
    else:
        if reaction.emoji == e1:
            card = meanings2[choice1[0]]
        elif reaction.emoji == e2:
            card = meanings2[choice2[0]]
        elif reaction.emoji == e3:
            card = meanings2[choice3[0]]





    if v == False:
        await message.channel.send("You drew *"+card.name+"*")
        broken = True

    if broken == False:
        await dispCard(message, meanings2,  client, card, False)
    await button.delete()
    await mess.delete()
    broken = True
    return(card)
