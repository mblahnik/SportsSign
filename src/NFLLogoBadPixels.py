

class Pixel():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

BearsLogoBadPixels = [Pixel(3, 17), Pixel(3,18)]

teamsDict = {"bears.png": BearsLogoBadPixels,
#             "Angels.png": AngelsLogoBadPixels,
#             "Astros.png": AstrosLogoBadPixels,
#             "BlueJays.png": BlueJaysLogoBadPixels,
#             "Braves.png": BravesLogoBadPixels,
#             "Cubs.png": CubsLogoBadPixels,
#             "DiamondBacks.png": DiamondBacksBadPixels,
#             "Mariners.png": MarinersLogoBadPixels,
#             "Marlins.png": MarlinsLogoBadPixels,
#             "Mets.png": MetsLogoBadPixels,
#             "Nationals.png": NationalsLogoBadPixels,
#             "Orioles.png": OriolesLogoBadPixels,
#             "Phillies.png": PhilliesLogoBadPixels,
#             "Rangers.png": RangersLogoBadPixels,
#             "Rays.png": RaysLogoBadPixels,
#             "Reds.png": RedsLogoBadPixels,
#             "RedSox.png": RedSoxLogoBadPixels,
#             "Tigers.png": TigersLogoBadPixels,
#             "Twins.png": TwinsLogoBadPixels,
#             "WhiteSox.png": WhiteSoxLogoBadPixels,
#             "Yankees.png": YankeesLogoBadPixels,
#             "Rockies.png": RockiesLogoBadPixels
             }


def GetBadPixelList(teamLogoFileName):
    if teamLogoFileName in teamsDict:
        return teamsDict[teamLogoFileName]
    else:
        return []
