async def test(message, meanings):
    emoji = '\N{THUMBS UP SIGN}'
    mess = await message.channel.send("This is a test!")
    await mess.add_reaction(emoji)
    print(mess.reactions)

    def check(reaction, user):
            return user != mess.author and str(reaction.emoji) == emoji

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await message.channel.send('nobody reacted :(')
    else:
        await message.channel.send(':o you reacted to me!!! ^////^')
        print(mess.reactions)
