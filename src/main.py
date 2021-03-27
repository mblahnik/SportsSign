import requests
from bs4 import BeautifulSoup


def main():
    URL = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
    URL2 = 'https://www.espn.com/nfl/team/schedule/_/name/gb'
    URL3 = 'https://www.espn.com/mlb/boxscore?gameId=401289013'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(page.content)

    r = soup.find_all('div', class_='Zndgme')

    print(r[len(r)-1])

    # for x in r:
    # print(x)
    # print("/")

   # tableRows = soup.find_all('tr', class_='Table__TR')

   # for i in range(1, len(tableRows)):
    #    print(tableRows[i].findAll('td')[0].get_text())

    #url = "https://therundown-therundown-v1.p.rapidapi.com/sports"

    # headers = {
    #    'x-rapidapi-key': "478c0ebbc0msh9d93f83fb216aeep1a8f36jsnfb4817fac2b8",
    #    'x-rapidapi-host': "therundown-therundown-v1.p.rapidapi.com"
    # }

    #response = requests.request("GET", url, headers=headers)

    # print(response.text)


if __name__ == "__main__":
    main()
