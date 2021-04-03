from bs4 import BeautifulSoup, SoupStrainer
import requests
from timeout import timeout

brewersNewsURL = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen"
page = requests.get(brewersNewsURL)
parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})
length = len(page.content)
start = round(length*.55)
end = round(length*.65)
soup = BeautifulSoup(page.content[start:], 'html.parser')
cards = soup.find_all('div', class_='SOsZve')
card = cards[len(cards)-1]

Scores = card.find_all('div', class_='nE4ijc')
print(Scores[0].string)
