import discord
import asyncio
from randomCard import *
from defs import *
from discord import Embed

async def spreads(message, meanings, client):
    embedVar = Embed(title="Spreads", description="All the spreads you can choose from", color=0x8D1B80)
    embedVar.add_field(name="Past, Present, Future", value=":clock5: Get a sense for the time around you", inline=True)
    embedVar.add_field(name="Cause, Issue, Focus", value=":mag_right:  Useful when you have a problem in mind", inline=True)
    mess = await message.channel.send(embed=embedVar)
    e1 = "🕔"
    e2 = "🔎"
    await mess.add_reaction(e1)
    await mess.add_reaction(e2)
    def check(reaction, user):
            return user != mess.author
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        print("timed out")
    else:
        if reaction.emoji == e1:
            await ppp(message, meanings, client)
        elif reaction.emoji == e2:
            await cif(message, meanings, client)

async def ppp(message, meanings, client):
    await message.channel.send("***Past:***\n")
    await randomCard(message, meanings, client)
    await message.channel.send("***Present:***\n")
    await randomCard(message, meanings, client)
    await message.channel.send("***Future***:\n")
    await randomCard(message, meanings, client)

async def cif(message, meanings, client):
    await message.channel.send("***Cause:***\n")
    await randomCard(message, meanings, client)
    await message.channel.send("***Issue:***\n")
    await randomCard(message, meanings, client)
    await message.channel.send("***Focus:***\n")
    await randomCard(message, meanings, client)
