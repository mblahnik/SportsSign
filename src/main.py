import sys
import os
import requests
from bs4 import BeautifulSoup, SoupStrainer
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
import time


def main():
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 2
    options.parallel = 1
    options.pixel_mapper_config = "U-mapper"
    options.hardware_mapping = 'adafruit-hat'
    matrix = RGBMatrix(options=options)

    URL = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
    URL2 = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE50TVc0U0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'

    Away_Team_Index = 0
    Home_Team_Index = 1

    page = requests.get(URL2)

    parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})

    length = len(page.content)
    start = round(length*.6)
    end = round(length*.63)

    soup = BeautifulSoup(
        page.content[start:end], 'html.parser', parse_only=parse_list)

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
    Home_Team_Logo_Image.thumbnail(
        (matrix.width-35, matrix.height-35), Image.ANTIALIAS)
    Away_Team_Logo_Image.thumbnail(
        (matrix.width-35, matrix.height-35), Image.ANTIALIAS)

    matrix.SetImage(Away_Team_Logo_Image.convert('RGB'), -2, 33)
    matrix.SetImage(Home_Team_Logo_Image.convert('RGB'), 37, 33)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
