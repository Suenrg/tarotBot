import requests
import bs4
from bs4 import BeautifulSoup
import codecs

url = "https://www.alittlesparkofjoy.com/tarot/suit-of-cups/page/2"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

flip = True

main = soup.find('main')
arts = main.find_all('a')
links =[]
f = open("links.txt", "a")
for x in arts:
    if(flip==True):
        links.append(x.get('href'))
        f.write(x.get('href') + '\n')
    flip = not flip
f.close()

print(links)
