from bs4 import BeautifulSoup, SoupStrainer
import requests
from timeout import timeout
from PIL import Image
from NFLTeamLogos import GetNFLTeamLogoImage


class NFLGoogleNewsParser:

    def __init__(self):
        super().__init__()
        self.soup = None
        self.card = None
        self.UpcomingGameCard = None
        self.packersNewsURL = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE5pTTJvU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen"
        self.Away_Team_Index = 0
        self.Home_Team_Index = 1

    def LoadPage(self):
        page = requests.get(self.packersNewsURL)
        parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})
        length = len(page.content)
        start = page.text.find("<div class=\"SOsZve\">")
        end = page.text.find(
            "<h2 class=\"oOr8M  uP1HId Ir3o3e cS3HJf\" jsname=\"smh91d\">Standings")
        self.soup = BeautifulSoup(
            page.content[start:end], 'html.parser')
        cards = self.soup.find_all('div', class_='SOsZve')
        self.card = cards[len(cards)-1]
        self.UpcomingGameCard = self.soup.find('div', class_='LI3zEe uP1HId')

    def GetHomeTeamLogo(self):
        hometeamName = self.card.findAll('div', class_='MlH7je')[
            1].string.lower()
        return GetNFLTeamLogoImage(hometeamName)

    def GetHomeTeamScore(self):
        Scores = self.card.find_all('div', class_='nE4ijc')
        return Scores[self.Home_Team_Index].string

    def GetAwayTeamLogo(self):
        awayteamName = self.card.findAll('div', class_='MlH7je')[
            0].string.lower()
        return GetNFLTeamLogoImage(awayteamName)

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

    def GetUpcomingGameDate(self):
        return self.UpcomingGameCard.find('div', class_='fMAqYb').string

    def GetUpcomingGameHomeTeamLogo(self):
        homeTeamName = self.UpcomingGameCard.find_all(
            'div', class_='MlH7je')[1].string.lower()
        return GetNFLTeamLogoImage(homeTeamName)

    def GetUpcomingGameAwayTeamLogo(self):
        awayTeamName = self.UpcomingGameCard.find_all(
            'div', class_='MlH7je')[0].string.lower()
        return GetNFLTeamLogoImage(awayTeamName)
