from Scene import Scene
from NFLGoogleNewsParser import NFLGoogleNewsParser
import datetime

dateDict = {'Jan': 1, 'Fed': 2, 'Mar': 3,
            'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


class NFLSceneGenerator:
    def __init__(self):
        super().__init__()
        self.dataSource = NFLGoogleNewsParser()

    def GetScene(self):
        scene = Scene()
        self.dataSource.LoadPage()
        upComingDateString = self.dataSource.GetUpcomingGameDate()

        if self.shouldDisplayUpComingGame(upComingDateString):
            scene.Home_Team_Logo_Image = self.dataSource.GetUpcomingGameHomeTeamLogo()
            scene.Away_Team_Logo_Image = self.dataSource.GetUpcomingGameAwayTeamLogo()
            split = upComingDateString.split(" ")
            firstline = ""
            secondline = ""
            for line in split[:3]:
                firstline += line + " "
            for line in split[3:]:
                secondline += line + " "

            scene.AdditionalText.append(firstline)
            scene.AdditionalText.append(secondline)
        else:
            scene.Home_Team_Logo_Image = self.dataSource.GetHomeTeamLogo()
            scene.Away_Team_Logo_Image = self.dataSource.GetAwayTeamLogo()
            scene.Home_Team_Score = self.dataSource.GetHomeTeamScore()
            scene.Away_Team_Score = self.dataSource.GetAwayTeamScore()
            scene.MainText = self.dataSource.GetInning()
            scene.AdditionalText = self.dataSource.GetAdditionalText()

        return scene

    def shouldDisplayUpComingGame(self, upcomingDateString):
        currentDate = datetime.datetime.now()
        dateSplit = upcomingDateString.split()
        year = datetime.datetime.now().year
        nextGameDate = datetime.datetime(
            year, dateDict[dateSplit[1]], int(dateSplit[2]))

        print(nextGameDate)
        print(currentDate)
        print((nextGameDate - currentDate).days)

        return (nextGameDate - currentDate).days >= 3