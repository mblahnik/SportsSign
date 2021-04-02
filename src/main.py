import sys
import os
import requests
from bs4 import BeautifulSoup, SoupStrainer
import time
from Scene import Scene
from MLBSceneRenderer import MLBSceneRenderer
from PIL import Image
from GoogleNewsParser import GoogleNewsParser


def main():

    sceneRenderer = MLBSceneRenderer()
    parser = GoogleNewsParser()

    URL = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
    URL2 = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRGRzT0dZU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'

    Away_Team_Index = 0
    Home_Team_Index = 1

    sceneRenderer.printText("Loading...")

    while True:
        try:
            parser.LoadPage()
            #page = requests.get(URL2)

            #parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})

            #length = len(page.content)
            #start = round(length*.55)
            #end = round(length*.65)
            # print("GettingSoup")
            # soup = BeautifulSoup(
            # page.content[start:end], 'html.parser', parse_only=parse_list)
            # print("SoupGotten")
            #r = soup.find_all('div', class_='SOsZve')
            #r = r[len(r)-1]

            #TeamLogos = r.find_all('img')
            #Home_Team_Logo_URL = TeamLogos[Home_Team_Index]['src']
            #Away_Team_Logo_URL = TeamLogos[Away_Team_Index]['src']

            #Scores = r.find_all('div', class_='nE4ijc')

            #Home_Team_Score = Scores[Home_Team_Index].string
            #Away_Team_Score = Scores[Away_Team_Index].string

            #AdditionalTextTags = r.find_all('div', class_='njYF6e')
            #AdditionalText = []

            # for tag in AdditionalTextTags:
            # AdditionalText.append(tag.string)

            #InningTag = r.find_all('div', class_='MHBqCc uULV7d')
            #InningText = ""

            # if len(InningTag) > 0:
            #InningText = InningTag[0].string

            # Scene starts here
            # Home_Team_Logo_Image = Image.open(
            # requests.get(Home_Team_Logo_URL, stream=True).raw)
            # Away_Team_Logo_Image = Image.open(
            # requests.get(Away_Team_Logo_URL, stream=True).raw)

            scene = Scene()
            scene.Home_Team_Logo_Image = parser.GetHomeTeamLogo
            scene.Away_Team_Logo_Image = parser.GetAwayTeamLogo
            scene.Home_Team_Score = parser.GetHomeTeamScore
            scene.Away_Team_Score = parser.GetAwayTeamScore
            scene.InningText = parser.GetInning
            scene.AdditionalText = parser.GetAdditionalText

            sceneRenderer.RenderScene(scene)
        except KeyboardInterrupt:
            quit()
        except TimeoutError:
            print("Request taking too long, starting over")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
