import requests
from bs4 import BeautifulSoup
import random

def scrapeWiki(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    allLinks = soup.find(id="bodyContent").find_all('a')
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        if link['href'].find('/wiki/') == -1:
            continue
        
        linkToScrape = link
        break

    scrapeWiki('https://en.wikipedia.org' + linkToScrape['href'])

scrapeWiki('https://en.wikipedia.org/wiki/Web_scraping')