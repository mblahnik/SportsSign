import datetime

dateString = "Sat, Apr 10 8:10 PM"

dateDict = {'Jan': 1, 'Fed': 2, 'Mar': 3,
            'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
dateSplit = dateString.split()

year = datetime.datetime.now().year

currentDate = datetime.datetime.now()

nextGameDate = datetime.datetime(
    year, dateDict[dateSplit[1]], int(dateSplit[2]))

print(currentDate.date().day == nextGameDate.date().day and (
    currentDate.date().month == nextGameDate.date().month) and currentDate.date().year == nextGameDate.date().year)
print(currentDate.date())
print(nextGameDate.date())
