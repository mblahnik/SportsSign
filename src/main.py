import sys
import os
import requests
from bs4 import BeautifulSoup, SoupStrainer
import time
from Scene import Scene
from MLBSceneGenerator import MLBSceneGenerator
from PIL import Image


def main():

    URL = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'

    Away_Team_Index = 0
    Home_Team_Index = 1

    page = requests.get(URL)

    parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})

    length = len(page.content)
    start = round(length*.60)
    end = round(length*.65)
    print("GettingSoup")
    soup = BeautifulSoup(
        page.content[start:end], 'html.parser', parse_only=parse_list)
    print("SoupGotten")
    r = soup.find_all('div', class_='SOsZve')
    r = r[len(r)-1]

    TeamLogos = r.find_all('img')
    Home_Team_Logo_URL = TeamLogos[Home_Team_Index]['src']
    Away_Team_Logo_URL = TeamLogos[Away_Team_Index]['src']

    Scores = r.find_all('div', class_='nE4ijc')

    Home_Team_Score = Scores[Home_Team_Index].string
    Away_Team_Score = Scores[Away_Team_Index].string

    AdditionalTextTags = r.find_all('div', class_='njYF6e')
    AdditionalText = []

    for tag in AdditionalTextTags:
        AdditionalText.append(tag.string)

    InningTag = r.find_all('div', class_='MHBqCc uULV7d')
    InningText = ""

    if len(InningTag) > 0:
        Inning = InningTag[0].string

    # Scene starts here
    Home_Team_Logo_Image = Image.open(
        requests.get(Home_Team_Logo_URL, stream=True).raw)
    Away_Team_Logo_Image = Image.open(
        requests.get(Away_Team_Logo_URL, stream=True).raw)

    scene = Scene()
    scene.Home_Team_Logo_Image = Home_Team_Logo_Image
    scene.Away_Team_Logo_Image = Away_Team_Logo_Image
    scene.Home_Team_Score = Home_Team_Score
    scene.Away_Team_Score = Away_Team_Score

    MLBSceneGenerator.RenderScene(scene)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
