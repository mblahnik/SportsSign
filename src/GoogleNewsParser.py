from bs4 import BeautifulSoup, SoupStrainer
import requests
from timeout import timeout
from PIL import Image


class GoogleNewsParser:

    def __init__(self):
        super().__init__()
        self.soup = None
        self.card = None
        self.brewersNewsURL = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen"
        self.Away_Team_Index = 0
        self.Home_Team_Index = 1

    def LoadPage(self):
        page = requests.get(self.brewersNewsURL)
        parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})
        length = len(page.content)
        start = round(length*.60)
        end = round(length*.67)
        self.soup = BeautifulSoup(
            page.content[start:end], 'html.parser', parse_only=parse_list)
        cards = self.soup.find_all('div', class_='SOsZve')
        self.card = cards[len(cards)-1]

    def GetHomeTeamLogo(self):
        TeamLogos = self.card.find_all('img')
        Home_Team_Logo_URL = TeamLogos[self.Home_Team_Index]['src']
        return Image.open(requests.get(Home_Team_Logo_URL, stream=True).raw)

    def GetHomeTeamScore(self):
        Scores = self.card.find_all('div', class_='nE4ijc')
        return Scores[self.Home_Team_Index].string

    def GetAwayTeamLogo(self):
        TeamLogos = self.card.find_all('img')
        Away_Team_Logo_URL = TeamLogos[self.Away_Team_Index]['src']
        return Image.open(requests.get(Away_Team_Logo_URL, stream=True).raw)

    def GetAwayTeamScore(self):
        Scores = self.card.find_all('div', class_='nE4ijc')
        return Scores[self.Away_Team_Index].string

    def GetInning(self):
        InningTag = self.card.find_all('div', class_='MHBqCc uULV7d')
        InningText = ""
        if len(InningTag) > 0:
            InningText = InningTag[0].string
        return InningText

    def GetAdditionalText(self):
        AdditionalTextTags = self.card.find_all('div', class_='njYF6e')
        AdditionalText = []
        for tag in AdditionalTextTags:
            AdditionalText.append(tag.string)
        return AdditionalText
