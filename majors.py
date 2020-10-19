from randomCard import *
import discord

async def majors(message, meanings, client):
    card = await randomCardQuiet(message, meanings, client)

    while ((card.name.lower() != "wheel of fortune") and ('of' in card.name)):
        card = await randomCardQuiet(message, meanings, client)

    await dispCard(message, meanings, client, card, False)
