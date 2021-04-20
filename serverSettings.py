import shelve
import discord
import asyncio
from discord import Embed

async def serverSettings(message, url, client):
    embedVar = Embed(title="Talking", description="Should Gaia be able to talk without being prompted?", color=0x8D1B80)
    embedVar.add_field(name="Talkative!", value="😃", inline=True)
    embedVar.add_field(name="Quiet", value="🤐", inline=True)
    mess = await message.channel.send(embed=embedVar)
    e1 = "😃"
    e2 = "🤐"
    await mess.add_reaction(e1)
    await mess.add_reaction(e2)
    def check(reaction, user):
            return user != mess.author and reaction.message.id == mess.id and user == message.author
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=90.0, check=check)
    except asyncio.TimeoutError:
        print("timed out")
    else:
        if reaction.emoji == e1:
            talk = True
            await message.channel.send("Gaia can now talk freely!")
        elif reaction.emoji == e2:
            talk = False
            await message.channel.send("Gaia is gonna be quiet")
        else:
            talk = False
        with shelve.open(url, writeback=True) as s:
            ma = str(message.channel.guild.id)
            s[ma] = talk

    return talk
