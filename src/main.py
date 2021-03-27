import requests
from bs4 import BeautifulSoup


def main():
    URL = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFV4ZG5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(page.content)

    r = soup.find_all('div', class_='Zndgme')

    print(r[len(r)-1])

    # for x in r:
    # print(x)
    # print("/")

   # tableRows = soup.find_all('tr', class_='Table__TR')


if __name__ == "__main__":
    main()
