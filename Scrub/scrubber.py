import requests
import bs4
from bs4 import BeautifulSoup
import codecs

links = []
with open("C:/Users/bensh/Documents/GitHub/tarotBot/Scrub/tempLinks.txt",errors='ignore') as p:
    for line in p:
        links.append(line)

for url in links:
    #url = "https://www.alittlesparkofjoy.com/six-of-wands-tarot-card-meanings"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ftwp-postcontent')



    short = ""
    for p in soup.find_all('p'):
        if "Upright:" in p.text:

            short = p.text.replace('Upright:', '')
            short = short.replace(u'\xa0', u'')
            #print(short)
    cut = short.partition('Reversed:')
    #print(cut)
    up = ''
    rev = ''
    if short == '':
        table = soup.find('table')
        if (not (table is None)):
            table_rows = table.find_all('tr')
            up = table_rows[0].find_all('td')[1].text
            rev = table_rows[1].find_all('td')[1].text
    else:
        up = cut[0]
        rev = cut[2]
    print("Upright: "+ up)
    print("Reversed: "+ rev)
    print("============================================")


    div = soup.findAll('img')
    img = div[1]

    print(img['data-src'])

    print("============================================")

    # content = soup.findAll("div", {"id": "ftwp-postcontent"})[0].text#.encode('utf-8'))
    h2s = soup.findAll('h2')

    content = ""
    card = h2s[3].text.replace(" Tarot Card Meaning", '')
    card = card.replace("Upright ", '')
    print(card)
    target = h2s[3]
    for sib in target.find_next_siblings():
        if sib.name=="h2":
            break
        else:
            #print(sib.text)
            content += (sib.text)

    content = content.partition('Money and Career')
    if content[2] == '':
        content = content[0].partition('Work and Money')
    gen = content[0]
    print(content)

    # content2 = content[2]
    # content2 = content2.partition('Love and Relationships')
    # money = content2[0]
    # if(money.startswith('Meaning')):
    #     money = money[8:]
    #
    # content3 = content2[2]
    # content3 = content3.partition('Health and Spirituality')
    # love = content3[0].partition('Get your own Tarot Love Reading')[0]
    # health = content3[2]

    # content4 = content3[2][1:]
    # content4 = content4.partition
    with open("scrubOut2.txt", "a", encoding="utf-8") as f:
        f.write(card + '\n')
        f.write("Upright: "+ up + '\n')
        f.write("Reversed: "+ rev + '\n')
        f.write("General: " + gen + '\n')
        f.write("Img: " + img['data-src'] + '\n')
        # f.write("Work: " + money + '\n')
        # f.write("Love: " + love + '\n')
        # f.write("Health: "+ health + '\n')
        f.write("================================\n\n")
