#! python3
# searchpypi.py - Opens several search results

import requests
import sys
import webbrowser
import bs4


print('Searching...') # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
#res = requests.get('https://pypi.org/search/?q=' + 'pyinputplus')
res.raise_for_status()
#print(res.text)
# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

# Open a browser tab for each result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

