import sys
import os
import requests
from bs4 import BeautifulSoup, SoupStrainer


def main():
    URL = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
    URL2 = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE50TVc0U0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'

    Away_Team_Index = 0
    Home_Team_Index = 1

    print("Getting page")
    page = requests.get(URL)
    print("PageLoaded")

    parse_list = SoupStrainer('div', attrs={"class": "SOsZve"})

    print("Getting Soup")
    soup = BeautifulSoup(page.content, 'html.parser', parse_only=parse_list)
    print("Soup Gotten")

    print("LoadingCard")
    r = soup.find_all('div', class_='SOsZve')
    r = r[len(r)-1]
    print("CardLoaded")

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

    print(AdditionalText)

    print("HomeTeamURL : " + Home_Team_Logo_URL)
    print("HomeTeamScore : " + Home_Team_Score)
    print("\n")
    print("AwayTeamURL : " + Away_Team_Logo_URL)
    print("AwayTeamScore : " + Away_Team_Score)
    print(InningText)


if __name__ == "__main__":
    main()
