
#
# URL = "https://www.amazon.in/s?k=<search_keyword_here>"
# r = requests.get(URL)
# #print(r.content)
# soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
