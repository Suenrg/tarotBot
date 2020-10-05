import random
from datetime import datetime
from discord import Embed
import discord
import asyncio

async def dispCard(card, meanings, client, rev):
    if rev == False:
        msg = Embed(title=card.name, description=(card.up), color=message.author.color)
        msg.set_image(url = card.pic)
        mess = await message.channel.send(embed = msg)
    else:
        msg = Embed(title=card.name, description=(card.rev), color=message.author.color)
        msg.set_image(url = card.pic)
        mess = await message.channel.send(embed = msg)
    e1 = "❓"
    await mess.add_reaction(e1)
    def check(reaction, user):
            return user != mess.author
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
