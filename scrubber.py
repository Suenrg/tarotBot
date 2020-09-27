import requests
import bs4
from bs4 import BeautifulSoup
import codecs



url = "https://www.alittlesparkofjoy.com/the-star-tarot-card-meanings"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ftwp-postcontent')



short = ""
for p in soup.find_all('p'):
    if "Upright:" in p.text:

        short = p.text.replace('Upright:', '')
        short = short.replace(u'\xa0', u'')
        print(short)
cut = short.partition('Reversed:')
print(cut)
print("Upright: "+cut[0])
print("Reversed: "+cut[2])
print("============================================")


div = soup.findAll('img')
img = div[1]

print(img['data-src'])

print("============================================")

# content = soup.findAll("div", {"id": "ftwp-postcontent"})[0].text#.encode('utf-8'))
h2s = soup.findAll('h2')

content = ""
print(h2s[3])
target = h2s[3]
for sib in target.find_next_siblings():
    if sib.name=="h2":
        break
    else:
        #print(sib.text)
        content += (sib.text)

content = content.partition('Money and Career Meaning')

content2 = content[2][1:]
content2 = content2.partition('Love and Relationships Meaning')

content3 = content2[2][1:]
content3 = content3.partition('Health and Spirituality Meaning')
love = content3[0].partition('Get your own Tarot Love Reading')[0]

# content4 = content3[2][1:]
# content4 = content4.partition
with open("scrubOut.txt", "w", encoding="utf-8") as f:
    f.write("Upright: "+cut[0] + '\n')
    f.write("Reversed: "+cut[2] + '\n')
    f.write("General: " + content[0] + '\n')
    f.write("Work: " + content2[0]+ '\n')
    f.write("Love: " + love + '\n')
    f.write("Health: "+ content3[2])
