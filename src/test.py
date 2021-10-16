import datetime

dateString = "Sat, Oct 24 8:10 PM"

dateDict = {'Jan': 1, 'Fed': 2, 'Mar': 3,
            'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
dateSplit = dateString.split()

year = datetime.datetime.now().year

currentDate = datetime.datetime.now()

nextGameDate = datetime.datetime(
    year, dateDict[dateSplit[1]], int(dateSplit[2]))

difference = nextGameDate - currentDate

print(currentDate)

print(nextGameDate)

print((nextGameDate - currentDate).days >= 3)