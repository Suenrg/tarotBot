import shelve
import discord

async def switchDeck(message, url):
    s = shelve.open(url, writeback=True)
    ma = str(message.author)
    try:

        if ma in s:
            print("found!")
            s[ma]['old'] = not s[ma]['old']
            if (s[ma]['old'] == True):
                await message.channel.send("Your preference has been switched to the Biddy deck!")
            else:
                await message.channel.send("Your preference has been switched to the Rider deck!")


        else:
            s[ma] = {'old': True}
            await message.channel.send("Your preference has been switched to the Biddy deck!")
    finally:
        s.close()

async def checkDeck(message, url):
    s = shelve.open(url, writeback=True)
    ma = str(message.author)
    try:
        if ma in s:
            if (s[ma]['old'] == True):
                await message.channel.send("Your preference is the Biddy deck!")
            else:
                await message.channel.send("Your preference is the Rider deck!")
        else:
            await message.channel.send("Your preference is Rider deck!")
    finally:
        s.close()
