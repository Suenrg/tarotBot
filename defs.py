import discord
from dispCard import *
async def defs(message, meaningsChosen, client):
    meanings = meaningsChosen[0]
    rev = False
    if 'reversed' in message.content.lower() or'rev' in message.content.lower(): # read a cards
        rev = True
    found = False
    inputs = message.content.lower().split(';')
    for c in inputs:
        for x in meanings:
            if x.lower()[:-1] in c:
                found = True
                await dispCard(message, meaningsChosen, client, meanings[x], rev)
                break
    return found

# async def defUp(message, meanings, text, client):
#     found = False
#     for x in meanings:
#         if x.lower()[:-1] in text.lower():
#             await dispCard(message, meanings, client, card, rev)
