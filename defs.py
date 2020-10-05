import discord
async def defs(message, meanings):
    rev = False
    if 'reversed' in message.content.lower() or'rev' in message.content.lower(): # read a cards
        rev = True
    found = False
    inputs = message.content.lower().split(';')
    for c in inputs:
        for x in meanings:
            if x.lower()[:-1] in c:
                found = True
                drawn = meanings[x]
                await message.channel.send(drawn.pic)
                if rev == False:
                    await message.channel.send("*" + drawn.name + "*\n**Upright:** ***" + drawn.up + "***")
                    if 'full' in c:
                        string = drawn.upB
                        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                        await message.channel.send("```" + string + "```")
                        #await message.channel.send("```" + secondpart + "```")

                else:
                    await message.channel.send("*" + drawn.name + "*\n**Reversed:** ***" + drawn.rev + "***")
                    if 'full' in c:
                        string = drawn.revB
                        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                        await message.channel.send("```" + string + "```")
                    #    await message.channel.send("```" + secondpart + "```")
                break

            #break
    return found

async def defUp(message, meanings, text):
    found = False
    for x in meanings:
        if x.lower()[:-1] in text.lower():
            found = True
            drawn = meanings[x]
            await message.channel.send(drawn.pic)
            await message.channel.send("*" + drawn.name + "*\n**Upright:** ***" + drawn.up + "***")
