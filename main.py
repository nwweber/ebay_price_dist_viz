"""
scrape prices off an ebay search and visualize them
"""

from bs4 import BeautifulSoup
import requests

url = "https://www.ebay.de/sch/i.html?_from=R40&_nkw=3080&_sacat=0&LH_BIN=1&rt=nc&LH_ItemCondition=1000|1500|2500" \
      "|3000&_ipg=200 "
r = requests.get(url)
soup = BeautifulSoup(r.text)

price_tags = soup.find_all('span', attrs={"class": "s-item__price"})

s = str(price_tags[0].string)


for pt in price_tags:
    if pt.string == "EUR 1.653,06":
        print(f'found it: {pt.string}')
        print(type(pt.string))
        s = pt.string
      # print(pt.string)
