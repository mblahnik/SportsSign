

class Pixel():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y


BrewersLogoBadPixels = [Pixel(0, 5), Pixel(1, 4), Pixel(2, 3), Pixel(3, 2), Pixel(4, 1), Pixel(
    5, 1), Pixel(6, 0), Pixel(8, 0), Pixel(25, 0), Pixel(26, 0), Pixel(27, 1), Pixel(28, 2), Pixel(0, 17),
    Pixel(0, 18), Pixel(0, 19), Pixel(1, 19), Pixel(1, 20), Pixel(
        1, 21), Pixel(2, 22), Pixel(2, 23), Pixel(2, 24),
    Pixel(3, 24), Pixel(3, 25), Pixel(4, 26), Pixel(4, 27), Pixel(5, 27),
    Pixel(5, 28), Pixel(6, 27), Pixel(6, 28), Pixel(
        6, 29), Pixel(7, 28), Pixel(7, 29), Pixel(8, 30),
    Pixel(22, 30), Pixel(23, 29), Pixel(24, 28), Pixel(
        25, 27), Pixel(25, 25), Pixel(26, 26), Pixel(26, 25),
    Pixel(27, 24), Pixel(27, 23), Pixel(27, 22), Pixel(28, 21), Pixel(28, 22), Pixel(28, 23)]

AngelsLogoBadPixels = [Pixel(0, 24), Pixel(
    0, 25), Pixel(0, 26), Pixel(0, 28), Pixel(0, 30)]


teamsDict = {"Brewers.png": BrewersLogoBadPixels,
             "Angels.png": AngelsLogoBadPixels}


def GetBadPixelList(teamLogoFileName):

    if teamLogoFileName in teamsDict:
        return teamsDict[teamLogoFileName]
    else:
        return []
