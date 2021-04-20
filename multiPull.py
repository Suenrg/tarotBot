import random
from datetime import datetime
from discord import Embed
import discord
import asyncio
from randomCard import *

# method for displaying a few cards to the user
async def multiPull(message, meanings, client, num):
    for x in range(num):
        asyncio.create_task(
            randomCardOS(message, meanings, client)
            )
        message.content = message.content + "asdyguhi"

    print("fin")
