from bs4 import BeautifulSoup, SoupStrainer
import requests
from timeout import timeout
from PIL import Image


class GoogleNewsParser:
    brewersNewsURL = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen"
    googleNewsHTML = ""
    soup = None
    card = None
    Away_Team_Index = 0
    Home_Team_Index = 1

    def __init__(self):
        super().__init__()

    @timeout(60)
    def LoadPage(self):
        page = requests.get(brewersNewsURL)
        parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})
        self.soup = BeautifulSoup(page.content, 'html.parser')
        length = len(page.content)
        start = round(length*.55)
        end = round(length*.65)
        print("GettingSoup")
        soup = BeautifulSoup(
            page.content[start:end], 'html.parser', parse_only=parse_list)
        print("SoupGotten")
        cards = soup.find_all('div', class_='SOsZve')
        card = card[len(cards)-1]

    def GetHomeTeamLogo(self):
        TeamLogos = card.find_all('img')
        Home_Team_Logo_URL = TeamLogos[Home_Team_Index]['src']
        return Image.open(requests.get(Home_Team_Logo_URL, stream=True).raw)

    def GetHomeTeamScore(self):
        Scores = card.find_all('div', class_='nE4ijc')
        return Scores[Home_Team_Index].string

    def GetAwayTeamLogo(self):
        TeamLogos = card.find_all('img')
        Away_Team_Logo_URL = TeamLogos[Home_Team_Index]['src']
        return Image.open(requests.get(Away_Team_Logo_URL, stream=True).raw)

    def GetAwayTeamScore(self):
        Scores = card.find_all('div', class_='nE4ijc')
        return Scores[Home_Team_Index].string

    def GetInning(self):
        InningTag = card.find_all('div', class_='MHBqCc uULV7d')
        InningText = ""
        if len(InningTag) > 0:
            InningText = InningTag[0].string
        return InningText

    def GetAdditionalText(self):
        AdditionalTextTags = card.find_all('div', class_='njYF6e')
        AdditionalText = []
        for tag in AdditionalTextTags:
            AdditionalText.append(tag.string)
        return AdditionalText
