import random
from datetime import datetime
from discord import Embed
import discord

async def help(message, client):
    line = False
    embed=Embed(title="Help", description="Hi! My name is Gaia, and I'm excited to help you with all your tarot and witchy needs :) You can either use the prefix !t or @ me for commands!", color=message.author.color)
    embed.add_field(name="!t help", value="Shows this message!", inline=line)
    embed.add_field(name="!t \"prompt\"", value="Draws a random card for the prompt given. ex: \"!t what should I focus on today?\"", inline=line)
    embed.add_field(name="!t draw \"prompt\"", value="Draws 3 cards for you to choose from related to your prompt, ex: \"!t draw for what I should focus on\"", inline=line)
    embed.add_field(name="!t \"name of a card\"", value="Gives you the description and image of a card! Press the ❓ button to get a more detailed description.", inline=line)
    embed.add_field(name="!t daily", value="Pulls a card for your day today, once per day.", inline=line)
    embed.add_field(name="!t switchDeck", value="Switches your deck preference.", inline=line)
    embed.add_field(name="!t spreads", value="Gives you a list of spreads to choose from!", inline=line)
    await message.channel.send(embed = embed)
