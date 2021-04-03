from bs4 import BeautifulSoup, SoupStrainer
import requests
from timeout import timeout
import datetime

brewersNewsURL = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen"
page = requests.get(brewersNewsURL)
parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})

dateString = "Sat, Apr 3 6:10 PM"


length = len(page.content)
start = page.text.find("<div class=\"SOsZve\">")
#end = page.text.find("<div class=\"gF8v3d\">")
end = page.text.find(
    "<h2 class=\"oOr8M  uP1HId Ir3o3e cS3HJf\" jsname=\"smh91d\">Standings")

soup = BeautifulSoup(page.content[start:end], 'html.parser')
cards = soup.find_all('div', class_='SOsZve')
card = cards[len(cards)-1]

Scores = card.find_all('div', class_='nE4ijc')
# print(Scores)

date = soup.find_all('div', class_='fMAqYb')
# print(date)

test = card.findAll('div', class_='MlH7je')
print(test)
