import datetime

dateString = "Sat, Apr 3 6:10 PM"

dateDict = {'Jan': 1, 'Fed': 2, 'Mar': 3,
            'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
dateSplit = dateString.split()

year = datetime.datetime.now().year

nextGameDate = datetime.datetime(year, dateDict[dateSplit[1]], dateSplit[2])
