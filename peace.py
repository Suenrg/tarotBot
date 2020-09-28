async def peace(message, meanings):
    if(len(message.mentions) != 2):
        await message.channel.send("I'm sorry, please use the correct format and @ both players and nobody else")
    p1 = message.mentions[0]
    p2 = message.mentions[1]

    s1 = 0
    s2 = 0
    round = 1
    broken = False

    emoji = '☮️'
    endmoji = '🔚'


    while (s1 < 2 and s2 < 2 and broken == False):
        await message.channel.send("========================================================================== \n ***Peace! Round " + str(round) + "***\n" + str(p1.nick) +": *" + str(s1) + "*, " + str(p2.nick) + ": *" + str(s2) + "* \n ==========================================================================")

        await message.channel.send(str(p1.mention) + " draws!")
        card1 = await draw(message, meanings, False, p1)
        #await asyncio.sleep(1)

        await message.channel.send(str(p2.mention) + " draws!")
        card2 = await draw(message, meanings, False, p2)
        #await asyncio.sleep(1)

        m1 = await message.channel.send("==============================\n" + str(p1.nick) + "\'s card: " + card1.pic)
        await message.channel.send("**Upright:** ***" + card1.up + "***")
        await m1.add_reaction(emoji)

        m2 = await message.channel.send(str(p2.nick) + "\'s card: " + card2.pic)
        await message.channel.send("**Upright:** ***" + card2.up + "***")
        await m2.add_reaction(emoji)

        end = await message.channel.send("React to me to finish voting!")
        await end.add_reaction(endmoji)

        await message.channel.send("==========================================================================")


        ####################################### Code that handles reactions
        fin = False
        r1 = 0 # r1 score
        r2 = 0 # r2 score

        while(fin == False):
            def check(reaction, user):
                    return user != end.author and (user == p1 or user == p2)
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=120.0, check=check)
            except asyncio.TimeoutError:
                print("timed out")
                await message.channel.send("You forgot about me :(")
                broken = True
                fin = True
            else:
                if reaction.message.id == end.id:
                    #if reaction.emoji == endmoji:
                    #    print('endmoji')
                    fin = True
                elif reaction.message.id == m1.id:
                    #if reaction.emoji == emoji:
                    print('m1 score')
                    r1 += 1
                elif reaction.message.id == m2.id:
                    #if reaction.emoji == emoji:
                    print('m2 score')
                    r2 += 1
        #######################################

        if broken == False:
            if r1 >= r2:
                s1 += 1
                await message.channel.send(str(p1.nick) + " scores!")
            else:
                s2 += 1
                await message.channel.send(str(p2.nick) + " scores!")
            round += 1

    if s1 == 2:
        await message.channel.send(str(p1.nick) + " wins and finds peace")
        broken = True
    elif s2 == 2:
        await message.channel.send(str(p2.nick) + " wins and finds peace")
        broken = True
    broken = True
