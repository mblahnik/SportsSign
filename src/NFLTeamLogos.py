import os
from PIL import Image

x = os.path.dirname(os.path.abspath(__file__))

mydict = {'gb': 'packers.png',
          'packers': 'packers.png',
          'det': 'lions.png',
          'lions': 'lions.png',
          'min': 'vikings.png',
          'vikings': 'vikings.png',
          'chi': 'bears.png',
          'bears': 'bears.png',
          'dal': 'cowboys.png',
          'cowboys': 'cowboys.png',
          'phi': 'eagles.png',
          'eagles': 'eagles.png',
          'was': 'wtf.png',
          'washington': 'wtf.png',
          'nyg': 'giants.png',
          'giants': 'giants.png',
          'no': 'saints.png',
          'saints': 'saints.png',
          'tb': 'buccaneers.png',
          'buccaneers': 'buccaneers.png',
          'car': 'panthers.png',
          'panthers': 'panthers.png',
          'atl': 'falcons.png',
          'falcons': 'falcons.png',
          'la': 'rams.png',
          'rams': 'rams.png',
          'sf': '49ers.png',
          '49ers': '49ers.png',
          'ari': 'cardinals.png',
          'cardinals': 'cardinals.png',
          'sea': 'seahawks.png',
          'seahawks': 'seahawks.png',
          'pit': 'steelers.png',
          'steelers': 'steelers.png',
          'cin': 'bengals.png',
          'bengals': 'bengals.png',
          'cle': 'browns.png',
          'browns': 'browns.png',
          'bal': 'ravens.png',
          'ravens': 'ravens.png',
          'mia': 'dolphins.png',
          'dolphins': 'dolphins.png',
          'nyj': 'jets.png',
          'jets': 'jets.png',
          'buf': 'bills.png',
          'bills': 'bills.png',
          'ne': 'patriots.png',
          'patriots': 'patriots.png',
          'hou': 'texans.png',
          'texans': 'texans.png',
          'ind': 'colts.png',
          'colts': 'colts.png',
          'ten': 'titans.png',
          'titans': 'titans.png',
          'jac': 'jaguars.png',
          'jaguars': 'jaguars.png',
          'den': 'broncos.png',
          'broncos': 'broncos.png',
          'lv': 'radiers.png',
          'radiers': 'radiers.png',
          'kc': 'chiefs.png',
          'chiefs': 'chiefs.png',
          'lac': 'chargers.png',
          'chargers': 'chargers.png'}


def GetNFLTeamLogoImage(teamName):
    filename = mydict[teamName]
    return Image.open(x + "/TeamLogos/NFL/" + filename)
