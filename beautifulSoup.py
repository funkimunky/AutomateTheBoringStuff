from bs4 import BeautifulSoup
import requests
#https://www.ebay.co.uk/sch/i.html?_nkw=planner+thicknesser&_sacat=0
url = 'https://www.ebay.co.uk'
search_item = 'planner+thicknesser'
search_url = '/sch/i.html?_nkw='+search_item+'&_sacat=0&_blrs=spell_auto_correct'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

res = requests.get(url+search_url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

elems = soup.select('ul.srp-results li')
print(elems[0].text)


