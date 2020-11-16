import random
from datetime import datetime
from discord import Embed
import discord
import asyncio


async def dispCard(message, meaningsChosen, client, card, rev):
    meanings = meaningsChosen[0]
    art = meaningsChosen[1]
    #async with message.channel.typing():
    if rev == False:
        msg = Embed(title=card.name, description=(card.up), color=message.author.color)
    else:
        msg = Embed(title=card.name +' Reversed', description=(card.rev), color=message.author.color)
    msg.set_image(url = art[card.name].pic)
    mess = await message.channel.send(embed = msg)
    e1 = "❓"
    await mess.add_reaction(e1)
    def check(reaction, user):
        return user != mess.author and reaction.message.id == mess.id
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        print("timed out")
    else:
        if reaction.emoji == e1:
            if(rev == False):
                if len(card.upB) > 2048:
                    msg.set_footer(text = card.upB[:2048])
                else:
                    msg.set_footer(text = card.upB)
            else:
                if len(card.revB) > 2048:
                    msg.set_footer(text = card.revB[:2048])
                else:
                    msg.set_footer(text = card.revB)
        await mess.edit(embed = msg)
