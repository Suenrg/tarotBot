import random
from datetime import datetime
from discord import Embed
import discord
import asyncio
from dispCard import *



async def randomCard(message, meaningsChosen, client):
    meanings = meaningsChosen[0]
    reversed = False
    seed = message.content + str(datetime.now())
    random.seed(seed)
    choice = random.choice(list(meanings.items()))
    card = meanings[choice[0]]
    if 'rev' in message.content.lower():
        reversed = bool(random.getrandbits(1))
    await dispCard(message, meaningsChosen, client, card, reversed)

    return(card)


async def randomCardQuiet(message, meaningsChosen, client):
    meanings = meaningsChosen[0]
    seed = message.content + str(datetime.now())
    random.seed(seed)
    choice = random.choice(list(meanings.items()))
    card = meanings[choice[0]]
    return(card)
