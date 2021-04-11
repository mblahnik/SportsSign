

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
    0, 25), Pixel(0, 26), Pixel(0, 28), Pixel(0, 30), Pixel(1, 6), Pixel(1, 7), Pixel(1, 8), Pixel(1, 17), Pixel(1, 21), Pixel(1, 22), Pixel(1, 23),
    Pixel(2, 5), Pixel(2, 6), Pixel(2, 9), Pixel(2, 16), Pixel(2, 18), Pixel(
        2, 19), Pixel(3, 4), Pixel(3, 10), Pixel(3, 14), Pixel(3, 15),
    Pixel(3, 17), Pixel(3, 18), Pixel(4, 3), Pixel(5, 2), Pixel(6, 2), Pixel(
        7, 0), Pixel(7, 1), Pixel(7, 2), Pixel(8, 1), Pixel(4, 11),
    Pixel(4, 12), Pixel(4, 14), Pixel(8, 28), Pixel(8, 29), Pixel(8, 30), Pixel(
        9, 29), Pixel(10, 29), Pixel(10, 30), Pixel(11, 29), Pixel(12, 30),
    Pixel(13, 0), Pixel(13, 1), Pixel(14, 2), Pixel(15, 2), Pixel(16, 3), Pixel(
        16, 9), Pixel(16, 12), Pixel(17, 4), Pixel(17, 8), Pixel(17, 9),
    Pixel(17, 12), Pixel(17, 13), Pixel(17, 14), Pixel(
        17, 15), Pixel(16, 10), Pixel(16, 11), Pixel(16, 14),
    Pixel(18, 5), Pixel(18, 9), Pixel(18, 16), Pixel(19, 6),
    Pixel(19, 7), Pixel(19, 8), Pixel(19, 17), Pixel(
        19, 18), Pixel(19, 19), Pixel(19, 20),
    Pixel(19, 21), Pixel(19, 22),
    Pixel(20, 23), Pixel(20, 24), Pixel(20, 25), Pixel(20, 27), Pixel(
        20, 29), Pixel(20, 30), Pixel(21, 30), Pixel(21, 29), Pixel(21, 28),
    Pixel(21, 27), Pixel(21, 26), Pixel(22, 30), Pixel(22, 29)]

AstrosLogoBadPixels = [Pixel(0, 6), Pixel(0, 7), Pixel(0, 9), Pixel(0, 21), Pixel(0, 23), Pixel(0, 24),
                       Pixel(1, 5), Pixel(1, 6), Pixel(
                           1, 7), Pixel(1, 23), Pixel(1, 25), Pixel(2, 4), Pixel(3, 3), Pixel(4, 2), Pixel(5, 1), Pixel(6, 0), Pixel(2, 26),
                       Pixel(3, 27), Pixel(4, 28), Pixel(5, 29), Pixel(6, 30),
                       Pixel(24, 0), Pixel(25, 1), Pixel(26, 2), Pixel(
                           27, 3), Pixel(28, 4), Pixel(29, 9), Pixel(24, 30), Pixel(25, 29), Pixel(26, 28), Pixel(27, 27)
                       ]


teamsDict = {"Brewers.png": BrewersLogoBadPixels,
             "Angels.png": AngelsLogoBadPixels,
             "Astros.png": AstrosLogoBadPixels}


def GetBadPixelList(teamLogoFileName):

    if teamLogoFileName in teamsDict:
        return teamsDict[teamLogoFileName]
    else:
        return []
