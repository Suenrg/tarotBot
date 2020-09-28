import discord
async def defs(message, meanings):
    broken = False
    rev = False
    if 'reversed' in message.content.lower() or'rev' in message.content.lower(): # read a cards
        rev = True
    if (broken == False):
        response2 = ""
        found = False
        for x in meanings:
            #print(x.lower()[:-1])

            if x.lower()[:-1] in message.content.lower():
                found = True
                drawn = meanings[x]
                await message.channel.send(drawn.pic)
                if rev == False:
                    await message.channel.send("*" + drawn.name + "*\n**Upright:** ***" + drawn.up + "***")
                    if 'full' in message.content.lower():
                        string = drawn.upB
                        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                        await message.channel.send("```" + string + "```")
                        #await message.channel.send("```" + secondpart + "```")

                else:
                    await message.channel.send("*" + drawn.name + "*\n**Reversed:** ***" + drawn.rev + "***")
                    if 'full' in message.content.lower():
                        string = drawn.revB
                        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                        await message.channel.send("```" + string + "```")
                    #    await message.channel.send("```" + secondpart + "```")

                #break
        if (found == False and broken == False):
            await message.channel.send("Are you sure you wrote that correctly?")
