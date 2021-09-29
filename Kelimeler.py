import requests
from bs4 import BeautifulSoup
import re

URL = 'http://kelimelog.com/oxford-english-a-harfi-ile-baslayan-kelimeler/'
page = requests.get(URL)

results = BeautifulSoup(page.content, "html.parser")


lst = results.get_text()



print(lst)