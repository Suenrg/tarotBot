import random
from datetime import datetime
from discord import Embed
import discord
import asyncio



async def randomCard(message, meanings, client):
    reversed = False
    seed = message.content + str(datetime.now())
    random.seed(seed)
    choice = random.choice(list(meanings.items()))
    card = meanings[choice[0]]
    if 'rev' in message.content.lower():
        reversed = bool(random.getrandbits(1))




        # await message.channel.send(card.pic)
        # await message.channel.send("Gaia gives you *" +card.name + "*")
        # await message.channel.send("**Upright:** ***" + card.up + "***")
        # if 'full' in message.content.lower():
        #     string = card.upB
        #     firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
        #     await message.channel.send("```" + firstpart + "```")
        #     await message.channel.send("```" + secondpart + "```")
    else:
        await message.channel.send(card.pic)
        await message.channel.send("Gaia gives you *" +card.name + "* Reversed")
        await message.channel.send("**Reversed:** ***" + card.rev + "***")
        if 'full' in message.content.lower():
            string = card.revB
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            await message.channel.send("```" + firstpart + "```")
            await message.channel.send("```" + secondpart + "```")

    return(card)
