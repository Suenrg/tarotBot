import discord
import shelve
import datetime
import asyncio
from randomCard import *
from defs import *

async def daily(message, meanings, url, client):
    s = shelve.open(url, writeback=True)
    ma = str(message.author)
    try:
        day = datetime.now().strftime('%x')
        if ma in s and 'day' in s[ma]:
            if (s[ma]['day'] != day):
                card = await randomCard(message, meanings, client)
                s[ma]['card'] = card
                s[ma]['day'] = day
            else:
                mess = await message.channel.send("You've already pulled "+ s[ma]['card'].name + " today!")
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
                        await defUp(message, meanings, s[ma]['card'].name)

        else: #they're not in the sheet yet
            card = await randomCard(message, meanings, client)
            s[ma] = {'card': card, 'day': day, 'old': False}
    finally:
        s.close()
