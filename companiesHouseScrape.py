from bs4 import BeautifulSoup
import requests

# search for company
# curl 'https://find-and-update.company-information.service.gov.uk/advanced-search/get-results?companyNameIncludes=KINNOULL+HOUSE+LIMITED&companyNameExcludes=&registeredOfficeAddress=&incorporationFromDay=&incorporationFromMonth=&incorporationFromYear=&incorporationToDay=&incorporationToMonth=&incorporationToYear=&sicCodes=&dissolvedFromDay=&dissolvedFromMonth=&dissolvedFromYear=&dissolvedToDay=&dissolvedToMonth=&dissolvedToYear=' \
#  -H 'authority: find-and-update.company-information.service.gov.uk' \
#  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
#  -H 'accept-language: en-GB,en;q=0.9,en-US;q=0.8' \
#  -H 'cookie: __SID=4HITB/1QwdMAdu35AIjuv4YGqBY/MZCP3OMpHuY7qE9n+o1NIdGy/Mg; ch_cookie_consent=eyJ1c2VySGFzQWxsb3dlZENvb2tpZXMiOiJ5ZXMiLCJjb29raWVzQWxsb3dlZCI6WyJwaXdpayIsImdvb2dsZSJdfQ==; _pk_ref.2.4ed3=%5B%22%22%2C%22%22%2C1707724994%2C%22https%3A%2F%2Fwww.bing.com%2F%22%5D; _pk_id.2.4ed3=cd74e862d8e9f9c9.1707724994.; _pk_ses.2.4ed3=1; search.web.user=e7f7a6d9-d198-4149-9cc6-932cecf1b743' \
#  -H 'referer: https://find-and-update.company-information.service.gov.uk/advanced-search' \
#  -H 'sec-ch-ua: "Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"' \
#  -H 'sec-ch-ua-mobile: ?0' \
#  -H 'sec-ch-ua-platform: "Windows"' \
#  -H 'sec-fetch-dest: document' \
#  -H 'sec-fetch-mode: navigate' \
#  -H 'sec-fetch-site: same-origin' \
#  -H 'sec-fetch-user: ?1' \
#  -H 'upgrade-insecure-requests: 1' \
#  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0' \
#  --compressed

# list people in company
# https://find-and-update.company-information.service.gov.uk/company/SC190800/officers

companyNumber = 'SC190800'
search_url = 'https://find-and-update.company-information.service.gov.uk/company/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

res = requests.get(search_url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

elems = soup.select('ul.srp-results li')



