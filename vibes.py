import random
from datetime import datetime
from discord import Embed
import discord
import asyncio
from dispCard import *
async def vibeAdd(message, meanings, client):
    found = 0
    for x in meanings:
        if x.lower()[:-1] in message.content.lower():
            found += 1
            card = meanings[x]
    if found == 0:
        await message.channel.send("Make sure to put a card name with the vibe add!")
        return False
    elif found > 1:
        await message.channel.send("Make sure to only put one card!")
        return False
    else:
        info = message.content.replace('!t', '').lower()
        info = info.replace(card.name.lower(), '')
        info = info.replace('addvibe', '')
        if info[0] == ' ':
            info = info[1:]
        if info[-1] == ' ':
            info = info[:-1]
        print(card.name + ':' + info)
        with open("vibeList.txt", "a", encoding="utf-8") as f:
            f.write(card.name.lower() + ':' + info.lower() + '\n')
        await message.channel.send("You just added the vibe of: \"" + card.name + "\" to the phrase: \""+info+"\"")
        await dispCard(message, meanings, client, card, False)
        return True
