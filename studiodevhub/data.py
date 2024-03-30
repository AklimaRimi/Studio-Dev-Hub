import requests

from bs4 import BeautifulSoup

link = 'https://www.amazon.com/Storms-Secrets-Small-Town-Claire-Kingsley-ebook/dp/B0CWR5LSND/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr='

response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')


print(soup)