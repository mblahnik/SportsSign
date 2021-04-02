from bs4 import Beauti
import requests


class GoogleNewsParser:
    brewersNewsURL = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen"
    googleNewsHTML = ""
    soup = None

    def __init__(self):
        super().__init__()
        LoadPage()

    def LoadPage(self):
        page = requests.get(brewersNewsURL)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def GetHomeTeamLogo(self):
        return None

    def GetHomeTeamScore(self):
        return None

    def GetAwayTeamLogo(self):
        return None

    def GetAwayTeamScore(self):
        return None
