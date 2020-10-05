import requests
import bs4
from bs4 import BeautifulSoup
import discord
from moonCode import *

async def moon(message, verbose):
    url = "https://www.moongiant.com/phase/today/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.findAll("div", {"id": "todayMoonContainer"})[0]
    img = content.find('img')['src']
    img = "https://www.moongiant.com" + img

    print(img)

    phased = phase(position())

    print(phased)
    if(verbose):
        await message.channel.send(img)
        await message.channel.send("***"+phased+"***")
