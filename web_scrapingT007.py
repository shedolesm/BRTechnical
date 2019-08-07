import requests
import bs4


url = 'https://www.amazon.com/s?k=watch&crid=1BGDXHZEPA3TR&sprefix=watc%2Caps%2C350&ref=nb_sb_ss_i_3_4'
r = requests.get(url)

soup = bs4.BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())