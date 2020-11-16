import shelve
import discord
import asyncio
from discord import Embed

async def chooseArt(message, url, client):
    embedVar = Embed(title="Art", description="What you want your cards to look like!", color=0x8D1B80)
    embedVar.add_field(name="Everyday Tarot", value=":milky_way: The Biddy Deck", inline=True)
    embedVar.add_field(name="Rider Waite", value=":crystal_ball: A classic", inline=True)
    mess = await message.channel.send(embed=embedVar)
    e1 = "🌌"
    e2 = "🔮"
    await mess.add_reaction(e1)
    await mess.add_reaction(e2)
    def check(reaction, user):
            return user != mess.author and reaction.message.id == mess.id and user == message.author
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        print("timed out")
    else:
        if reaction.emoji == e1:
            choice = 'Biddy'
        elif reaction.emoji == e2:
            choice = 'Rider'
        else:
            choice = 'n/a'
        if choice != 'n/a':
            with shelve.open(url, writeback=True) as s:
                ma = str(message.author)
                s[ma]['art'] = choice
                await message.channel.send("You've chosen the " + choice + " deck!")
