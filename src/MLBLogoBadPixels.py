

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
                           27, 3), Pixel(28, 4), Pixel(24, 30), Pixel(25, 29), Pixel(26, 28), Pixel(27, 27),
                       Pixel(29, 5), Pixel(29, 6), Pixel(29, 7), Pixel(
                           30, 6), Pixel(30, 7), Pixel(30, 9),
                       Pixel(30, 21), Pixel(30, 23), Pixel(30, 24), Pixel(
                           29, 24), Pixel(29, 23), Pixel(29, 25), Pixel(28, 26)
                       ]

BlueJaysLogoBadPixels = [Pixel(0, 7), Pixel(1, 7), Pixel(2, 7), Pixel(3, 6), Pixel(4, 6), Pixel(5, 6), Pixel(6, 5), Pixel(7, 5), Pixel(8, 4), Pixel(9, 3),
                         Pixel(10, 3), Pixel(11, 2), Pixel(12, 2), Pixel(13, 2), Pixel(14, 2), Pixel(
                             15, 2), Pixel(17, 1), Pixel(18, 1), Pixel(19, 1), Pixel(20, 1),
                         Pixel(21, 0), Pixel(16, 2), Pixel(22, 0), Pixel(1, 14), Pixel(2, 14), Pixel(3, 15), Pixel(
                             4, 15), Pixel(5, 15), Pixel(6, 15), Pixel(7, 16), Pixel(8, 16), Pixel(9, 17), Pixel(9, 18),
                         Pixel(10, 18), Pixel(10, 19), Pixel(11, 20), Pixel(11, 21), Pixel(
                             12, 22), Pixel(12, 23), Pixel(12, 24), Pixel(13, 24), Pixel(13, 25), Pixel(27, 6), Pixel(28, 6), Pixel(29, 2),
                         Pixel(28, 1), Pixel(28, 2), Pixel(28, 3), Pixel(28, 4), Pixel(28, 5), Pixel(29, 1), Pixel(29, 3), Pixel(
                             29, 4), Pixel(29, 5), Pixel(29, 6), Pixel(30, 1), Pixel(30, 2), Pixel(30, 3), Pixel(30, 4), Pixel(30, 6),
                         Pixel(15, 25), Pixel(16, 25), Pixel(17, 25), Pixel(18, 25), Pixel(18, 24), Pixel(
                             18, 23), Pixel(19, 23), Pixel(19, 22), Pixel(20, 21), Pixel(21, 20), Pixel(21, 19),
                         Pixel(22, 19), Pixel(22, 18), Pixel(23, 18), Pixel(23, 17), Pixel(24, 17), Pixel(25, 17), Pixel(26, 17), Pixel(27, 17), Pixel(28, 15), Pixel(29, 14), Pixel(30, 13), Pixel(30, 14), Pixel(30, 15)]

BravesLogoBadPixels = [Pixel(1, 18), Pixel(0, 28), Pixel(4, 21), Pixel(4, 20), Pixel(
    5, 19), Pixel(6, 18), Pixel(7, 17), Pixel(8, 16), Pixel(9, 15), Pixel(10, 14), Pixel(21, 0), Pixel(20, 1), Pixel(19, 3), Pixel(18, 4), Pixel(17, 5), Pixel(16, 5), Pixel(15, 6), Pixel(14, 7), Pixel(13, 8), Pixel(13, 9),
    Pixel(12, 10), Pixel(11, 11), Pixel(11, 12), Pixel(11, 14), Pixel(10, 13), Pixel(10, 28), Pixel(11, 27), Pixel(
        12, 26), Pixel(13, 25), Pixel(13, 24), Pixel(14, 23), Pixel(15, 22), Pixel(16, 22), Pixel(17, 22),
    Pixel(18, 22), Pixel(18, 24), Pixel(19, 25), Pixel(19, 26), Pixel(
        20, 27), Pixel(21, 28), Pixel(29, 1), Pixel(30, 28),
    Pixel(28, 2), Pixel(28, 3), Pixel(27, 4), Pixel(26, 6), Pixel(26, 7), Pixel(
        27, 8), Pixel(25, 5), Pixel(24, 9), Pixel(23, 13), Pixel(26, 22),
    Pixel(25, 21), Pixel(25, 20), Pixel(24, 20), Pixel(26, 19), Pixel(27, 18), Pixel(29, 29), Pixel(25, 8), Pixel(29, 10), Pixel(30, 12), Pixel(30, 13), Pixel(29, 15), Pixel(29, 16), Pixel(28, 17)]

CubsLogoBadPixels = [Pixel(0, 6), Pixel(0, 7), Pixel(1, 5), Pixel(2, 4), Pixel(3, 3), Pixel(4, 2), Pixel(5, 1), Pixel(6, 0), Pixel(7, 0),
                     Pixel(0, 21), Pixel(0, 23), Pixel(0, 24), Pixel(1, 25), Pixel(2, 26), Pixel(
                         3, 27), Pixel(4, 28), Pixel(5, 29), Pixel(6, 30), Pixel(7, 30),
                     Pixel(23, 0), Pixel(24, 0), Pixel(25, 1), Pixel(26, 2), Pixel(27, 3), Pixel(
                         28, 4), Pixel(29, 5), Pixel(29, 7), Pixel(30, 6), Pixel(30, 7),
                     Pixel(23, 30), Pixel(24, 30), Pixel(25, 29), Pixel(26, 28), Pixel(27, 27), Pixel(28, 26), Pixel(29, 25), Pixel(30, 24), Pixel(30, 23)]

DiamondBacksBadPixels = [Pixel(0, 19), Pixel(0, 20), Pixel(1, 18), Pixel(1, 17), Pixel(2, 17), Pixel(2, 16), Pixel(3, 15), Pixel(3, 14), Pixel(4, 13), Pixel(5, 12),
                         Pixel(5, 11), Pixel(6, 10), Pixel(6, 9), Pixel(7, 8), Pixel(7, 9), Pixel(
                             8, 6), Pixel(8, 7), Pixel(9, 6), Pixel(9, 5), Pixel(10, 4),
                         Pixel(10, 3), Pixel(11, 2), Pixel(12, 1), Pixel(12, 0), Pixel(11, 23), Pixel(11, 22), Pixel(
                             12, 23), Pixel(13, 23), Pixel(13, 22), Pixel(13, 21), Pixel(14, 19), Pixel(14, 23),
                         Pixel(15, 23), Pixel(15, 22), Pixel(16, 20), Pixel(
                             16, 21), Pixel(15, 19), Pixel(14, 20),
                         Pixel(28, 23), Pixel(30, 23), Pixel(29, 22), Pixel(29, 21), Pixel(29, 20), Pixel(
                             29, 19), Pixel(28, 17), Pixel(28, 16), Pixel(28, 15), Pixel(27, 13),
                         Pixel(27, 12), Pixel(27, 11), Pixel(27, 10), Pixel(26, 8), Pixel(26, 7), Pixel(26, 6), Pixel(25, 4), Pixel(25, 3), Pixel(25, 2), Pixel(25, 1), Pixel(24, 0)]

MarinersLogoBadPixels = [Pixel(0, 3), Pixel(0, 4), Pixel(1, 2), Pixel(2, 1), Pixel(
    3, 0), Pixel(0, 8), Pixel(0, 9), Pixel(0, 12), Pixel(0, 14), Pixel(0, 15), Pixel(0, 30),
    Pixel(2, 17), Pixel(3, 17), Pixel(4, 18), Pixel(5, 18), Pixel(4, 19), Pixel(
        5, 19), Pixel(6, 19), Pixel(5, 20), Pixel(6, 21), Pixel(6, 22), Pixel(7, 24),
    Pixel(16, 12), Pixel(17, 12), Pixel(17, 14), Pixel(17, 15), Pixel(18, 14), Pixel(18, 15), Pixel(
        18, 17), Pixel(18, 25), Pixel(17, 26), Pixel(17, 27), Pixel(16, 28), Pixel(15, 29), Pixel(14, 30),
    Pixel(1, 13), Pixel(1, 14), Pixel(1, 15), Pixel(2, 14), Pixel(2, 15), Pixel(17, 16)]

MarlinsLogoBadPixels = [Pixel(7, 0), Pixel(7, 1), Pixel(7, 2), Pixel(7, 3), Pixel(6, 4), Pixel(5, 5), Pixel(3, 7), Pixel(2, 8), Pixel(1, 8), Pixel(1, 13),
                        Pixel(1, 13), Pixel(2, 13), Pixel(2, 17), Pixel(2, 21), Pixel(2, 24), Pixel(
                            1, 25), Pixel(13, 0), Pixel(14, 1), Pixel(15, 2), Pixel(15, 3),
                        Pixel(18, 2), Pixel(19, 2), Pixel(20, 2), Pixel(26, 4), Pixel(17, 11), Pixel(
                            18, 9), Pixel(19, 9), Pixel(19, 8), Pixel(20, 8), Pixel(25, 4),
                        Pixel(27, 5), Pixel(28, 5), Pixel(29, 5), Pixel(30, 5), Pixel(30, 6), Pixel(
                            30, 7), Pixel(30, 9), Pixel(29, 9), Pixel(29, 10), Pixel(28, 11),
                        Pixel(8, 27), Pixel(12, 28), Pixel(13, 27), Pixel(
                            13, 28), Pixel(15, 28), Pixel(16, 27), Pixel(16, 26),
                        Pixel(28, 15), Pixel(27, 17), Pixel(27, 18), Pixel(26, 20), Pixel(26, 21), Pixel(
                            26, 22), Pixel(25, 23), Pixel(25, 24), Pixel(25, 25), Pixel(25, 26), Pixel(25, 27),
                        Pixel(24, 26), Pixel(24, 27)]

NationalsLogoBadPixels = [Pixel(0, 6), Pixel(0, 7), Pixel(1, 5), Pixel(2, 4), Pixel(3, 4), Pixel(4, 3), Pixel(6, 2), Pixel(7, 2), Pixel(8, 2), Pixel(10, 1),
                          Pixel(11, 1), Pixel(12, 1), Pixel(13, 1), Pixel(14, 1), Pixel(15, 1), Pixel(
                              18, 2), Pixel(19, 2), Pixel(20, 2), Pixel(21, 2), Pixel(22, 1),
                          Pixel(22, 0), Pixel(17, 2), Pixel(21, 0), Pixel(21, 1), Pixel(0, 16), Pixel(
                              1, 17), Pixel(2, 18), Pixel(3, 18), Pixel(2, 19), Pixel(2, 20),
                          Pixel(2, 21), Pixel(2, 22), Pixel(2, 23), Pixel(2, 24), Pixel(
                              2, 25), Pixel(3, 26), Pixel(3, 27), Pixel(4, 28), Pixel(5, 29),
                          Pixel(16, 29), Pixel(17, 28), Pixel(18, 29), Pixel(19, 29), Pixel(20, 29), Pixel(
                              21, 29), Pixel(22, 28), Pixel(23, 28), Pixel(24, 27), Pixel(26, 26), Pixel(26, 25),
                          Pixel(27, 25), Pixel(30, 0), Pixel(30, 1), Pixel(
                              30, 19), Pixel(30, 20), Pixel(29, 21), Pixel(29, 22),
                          Pixel(28, 23), Pixel(28, 24), Pixel(27, 24), Pixel(
                              9, 23), Pixel(10, 23), Pixel(10, 22), Pixel(10, 21),
                          Pixel(10, 20), Pixel(10, 19), Pixel(10, 18), Pixel(11, 23), Pixel(
                              11, 22), Pixel(11, 21), Pixel(12, 23), Pixel(13, 7),
                          Pixel(9, 18), Pixel(11, 12), Pixel(12, 9), Pixel(17, 18), Pixel(
                              18, 17), Pixel(18, 14), Pixel(18, 13), Pixel(18, 12),
                          Pixel(18, 11), Pixel(17, 11), Pixel(
                              19, 11), Pixel(23, 20), Pixel(24, 17),
                          Pixel(24, 5), Pixel(24, 6)]

OriolesLogoBadPixels = [Pixel(0, 5), Pixel(0, 6), Pixel(1, 4), Pixel(1, 3), Pixel(2, 3), Pixel(2, 2), Pixel(3, 2), Pixel(3, 1), Pixel(4, 1), Pixel(16, 0),
                        Pixel(17, 1), Pixel(18, 1), Pixel(19, 1), Pixel(20, 0), Pixel(21, 0), Pixel(
                            22, 0), Pixel(23, 0), Pixel(24, 0), Pixel(30, 0), Pixel(30, 8),
                        Pixel(29, 9), Pixel(28, 10), Pixel(27, 10), Pixel(28, 11), Pixel(
                            29, 13), Pixel(4, 0), Pixel(29, 11), Pixel(30, 13), Pixel(30, 14),
                        Pixel(0, 10), Pixel(1, 10), Pixel(0, 11), Pixel(0, 12), Pixel(1, 12), Pixel(
                            0, 19), Pixel(0, 22), Pixel(0, 23), Pixel(1, 24), Pixel(1, 25),
                        Pixel(2, 24), Pixel(2, 25), Pixel(2, 26), Pixel(
                            3, 27), Pixel(4, 28), Pixel(4, 29), Pixel(5, 28),
                        Pixel(20, 28), Pixel(21, 27), Pixel(21, 26), Pixel(22, 26), Pixel(
                            22, 27), Pixel(23, 26), Pixel(23, 25), Pixel(24, 24), Pixel(26, 19),
                        Pixel(25, 23), Pixel(25, 22), Pixel(25, 21), Pixel(25, 19), Pixel(26, 20), Pixel(26, 18), Pixel(27, 18), Pixel(27, 17), Pixel(28, 17), Pixel(29, 17), Pixel(30, 15)]

PhilliesLogoBadPixels = [Pixel(0, 3), Pixel(0, 4), Pixel(1, 2), Pixel(2, 1), Pixel(3, 0), Pixel(4, 0), Pixel(0, 14), Pixel(1, 15), Pixel(2, 16), Pixel(3, 16),
                         Pixel(4, 16), Pixel(5, 16), Pixel(6, 15), Pixel(5, 17), Pixel(5, 18), Pixel(
                             5, 19), Pixel(5, 20), Pixel(5, 21), Pixel(5, 22), Pixel(5, 23),
                         Pixel(20, 0), Pixel(21, 1), Pixel(22, 1), Pixel(22, 2), Pixel(23, 3), Pixel(
                             23, 2), Pixel(6, 22), Pixel(4, 24), Pixel(4, 25), Pixel(3, 25),
                         Pixel(3, 26), Pixel(3, 27), Pixel(3, 28), Pixel(3, 29), Pixel(4, 29), Pixel(
                             4, 30), Pixel(15, 9), Pixel(15, 8), Pixel(16, 8), Pixel(23, 13),
                         Pixel(22, 14), Pixel(21, 15), Pixel(20, 16), Pixel(19, 17), Pixel(18, 18), Pixel(
                             17, 18), Pixel(15, 19), Pixel(16, 19), Pixel(16, 20), Pixel(16, 21),
                         Pixel(16, 22), Pixel(16, 23), Pixel(16, 24), Pixel(16, 25), Pixel(16, 26), Pixel(16, 27), Pixel(15, 28), Pixel(15, 29), Pixel(14, 29), Pixel(14, 30)]

RangersLogoBadPixels = [Pixel(1, 13), Pixel(2, 13), Pixel(3, 13), Pixel(4, 13), Pixel(6, 13), Pixel(6, 12), Pixel(6, 7), Pixel(7, 7), Pixel(7, 8), Pixel(7, 9),
                        Pixel(7, 10), Pixel(7, 11), Pixel(7, 12), Pixel(7, 13), Pixel(7, 14), Pixel(
                            7, 15), Pixel(7, 16), Pixel(7, 17), Pixel(7, 18), Pixel(7, 19),
                        Pixel(7, 20), Pixel(7, 21), Pixel(7, 21), Pixel(
                            8, 6), Pixel(8, 10), Pixel(8, 12), Pixel(8, 13),
                        Pixel(8, 15), Pixel(8, 22), Pixel(7, 22), Pixel(4, 25), Pixel(
                            4, 26), Pixel(4, 27), Pixel(4, 28), Pixel(5, 30),
                        Pixel(26, 13), Pixel(26, 13), Pixel(24, 13), Pixel(23, 13), Pixel(22, 13), Pixel(
                            22, 11), Pixel(22, 10), Pixel(21, 8), Pixel(21, 7), Pixel(21, 6),
                        Pixel(20, 5), Pixel(20, 7), Pixel(20, 8), Pixel(20, 9), Pixel(
                            20, 10), Pixel(20, 11), Pixel(18, 5), Pixel(25, 13), Pixel(21, 13),
                        Pixel(21, 11), Pixel(21, 10), Pixel(19, 5), Pixel(19, 6), Pixel(
                            20, 6), Pixel(19, 7), Pixel(19, 8), Pixel(19, 9),
                        Pixel(19, 10), Pixel(19, 11), Pixel(18, 11), Pixel(18, 12), Pixel(
                            18, 13), Pixel(18, 14), Pixel(19, 13), Pixel(19, 14), Pixel(20, 14),
                        Pixel(18, 16), Pixel(19, 16), Pixel(19, 17), Pixel(19, 18), Pixel(19, 19), Pixel(19, 20), Pixel(
                            19, 21), Pixel(19, 22), Pixel(19, 23), Pixel(20, 24), Pixel(21, 25), Pixel(22, 26),
                        Pixel(22, 27), Pixel(22, 28), Pixel(22, 29), Pixel(22, 30)]

RaysLogoBadPixels = [Pixel(0, 7), Pixel(1, 7), Pixel(2, 5), Pixel(3, 5), Pixel(3, 4), Pixel(4, 4), Pixel(6, 4), Pixel(5, 4), Pixel(5, 5), Pixel(5, 6), Pixel(5, 7),
                     Pixel(5, 8), Pixel(5, 9), Pixel(5, 10), Pixel(5, 11), Pixel(5, 12), Pixel(
                         5, 13), Pixel(5, 14), Pixel(5, 15), Pixel(5, 16), Pixel(6, 15),
                     Pixel(2, 18), Pixel(2, 19), Pixel(5, 21), Pixel(6, 21), Pixel(7, 21), Pixel(
                         8, 21), Pixel(9, 21), Pixel(10, 21), Pixel(11, 21), Pixel(13, 21),
                     Pixel(14, 21), Pixel(13, 22), Pixel(13, 23), Pixel(
                         12, 23), Pixel(10, 25), Pixel(10, 26), Pixel(12, 21),
                     Pixel(12, 4), Pixel(13, 4), Pixel(14, 4), Pixel(15, 4), Pixel(12, 10), Pixel(
                         13, 10), Pixel(13, 11), Pixel(13, 12), Pixel(13, 13), Pixel(13, 14),
                     Pixel(13, 15), Pixel(13, 16), Pixel(14, 16), Pixel(
                         12, 15), Pixel(20, 0), Pixel(20, 1), Pixel(20, 4),
                     Pixel(21, 4), Pixel(19, 4), Pixel(19, 5), Pixel(19, 3), Pixel(
                         25, 5), Pixel(26, 5), Pixel(27, 6), Pixel(28, 7),
                     Pixel(29, 8), Pixel(29, 9), Pixel(30, 9), Pixel(30, 10), Pixel(30, 11), Pixel(
                         30, 12), Pixel(30, 13), Pixel(29, 13), Pixel(29, 14), Pixel(28, 15),
                     Pixel(29, 16), Pixel(30, 17), Pixel(30, 18), Pixel(
                         30, 24), Pixel(30, 25), Pixel(29, 25), Pixel(29, 26),
                     Pixel(20, 10), Pixel(21, 10), Pixel(21, 11), Pixel(21, 12), Pixel(
                         21, 13), Pixel(22, 13), Pixel(22, 12), Pixel(22, 11), Pixel(23, 12),
                     Pixel(20, 19), Pixel(21, 19), Pixel(22, 18), Pixel(21, 20), Pixel(21, 22), Pixel(
                         21, 23), Pixel(21, 24), Pixel(20, 23), Pixel(23, 20), Pixel(23, 21),
                     Pixel(23, 22), Pixel(21, 21), Pixel(24, 21)]

RedsLogoBadPixels = [Pixel(0, 7), Pixel(1, 6), Pixel(2, 5), Pixel(3, 4), Pixel(4, 3), Pixel(5, 2), Pixel(6, 1), Pixel(7, 0), Pixel(8, 0), Pixel(0, 12),
                     Pixel(1, 13), Pixel(2, 14), Pixel(3, 15), Pixel(4, 16), Pixel(
                         5, 17), Pixel(6, 18), Pixel(7, 19), Pixel(8, 20), Pixel(9, 20),
                     Pixel(26, 0), Pixel(27, 1), Pixel(28, 2), Pixel(29, 2), Pixel(29, 3), Pixel(
                         30, 3), Pixel(30, 4), Pixel(30, 7), Pixel(29, 11), Pixel(28, 11), Pixel(27, 11),
                     Pixel(26, 11), Pixel(25, 11), Pixel(24, 12), Pixel(23, 12), Pixel(22, 13), Pixel(
                         21, 13), Pixel(20, 14), Pixel(19, 14), Pixel(18, 14), Pixel(17, 14), Pixel(16, 14),
                     Pixel(15, 14), Pixel(14, 14), Pixel(13, 14), Pixel(12, 13), Pixel(11, 13), Pixel(
                         10, 12), Pixel(10, 11), Pixel(9, 11), Pixel(10, 10), Pixel(10, 9), Pixel(10, 8),
                     Pixel(10, 7), Pixel(11, 5), Pixel(12, 6), Pixel(15, 5), Pixel(16, 5), Pixel(17, 5), Pixel(18, 5), Pixel(19, 5), Pixel(21, 6), Pixel(22, 6), Pixel(23, 7), Pixel(25, 8)]

RedSoxLogoBadPixels = [Pixel(1, 8), Pixel(2, 8), Pixel(2, 7), Pixel(3, 7), Pixel(2, 9), Pixel(2, 10), Pixel(2, 11), Pixel(2, 12), Pixel(3, 11),
                       Pixel(2, 18), Pixel(2, 19), Pixel(2, 20), Pixel(2, 21), Pixel(
                           2, 22), Pixel(2, 23), Pixel(3, 19), Pixel(3, 23), Pixel(1, 22),
                       Pixel(11, 6), Pixel(11, 7), Pixel(10, 7), Pixel(10, 8), Pixel(11, 8), Pixel(
                           12, 8), Pixel(12, 9), Pixel(10, 9), Pixel(10, 10), Pixel(11, 10),
                       Pixel(10, 20), Pixel(12, 20), Pixel(10, 21), Pixel(
                           10, 22), Pixel(11, 22), Pixel(12, 22), Pixel(12, 21),
                       Pixel(11, 20), Pixel(11, 23), Pixel(11, 24), Pixel(17, 0), Pixel(18, 1), Pixel(
                           19, 2), Pixel(19, 3), Pixel(20, 3), Pixel(20, 4), Pixel(20, 5), Pixel(19, 5), Pixel(21, 6),
                       Pixel(20, 7), Pixel(21, 8), Pixel(21, 9), Pixel(21, 11), Pixel(21, 12), Pixel(
                           21, 13), Pixel(21, 14), Pixel(21, 16), Pixel(21, 17), Pixel(21, 18), Pixel(21, 19),
                       Pixel(21, 21), Pixel(21, 22), Pixel(21, 24), Pixel(20, 12), Pixel(20, 14), Pixel(
                           20, 15), Pixel(20, 16), Pixel(20, 18), Pixel(20, 23), Pixel(20, 25),
                       Pixel(20, 26), Pixel(20, 27), Pixel(19, 27), Pixel(19, 28), Pixel(18, 29), Pixel(17, 30), Pixel(19, 25)]

MetsLogoBadPixels = [Pixel(0, 24), Pixel(1, 24), Pixel(
    2, 24), Pixel(3, 24), Pixel(4, 24), Pixel(5, 24), Pixel(6, 24), Pixel(9, 0), Pixel(11, 0), Pixel(8, 1), Pixel(9, 1), Pixel(10, 1), Pixel(8, 2), Pixel(10, 2),
    Pixel(8, 3), Pixel(8, 4), Pixel(9, 5), Pixel(10, 6), Pixel(10, 7), Pixel(11, 7), Pixel(
        11, 8), Pixel(12, 9), Pixel(13, 8), Pixel(13, 7), Pixel(14, 7), Pixel(13, 6),
    Pixel(13, 5), Pixel(13, 4), Pixel(14, 4), Pixel(12, 0), Pixel(12, 1), Pixel(12, 2), Pixel(
        20, 0), Pixel(21, 0), Pixel(20, 1), Pixel(20, 2), Pixel(21, 1), Pixel(21, 2),
    Pixel(18, 4), Pixel(19, 4), Pixel(19, 5), Pixel(19, 6), Pixel(
        18, 6), Pixel(19, 7), Pixel(20, 8), Pixel(22, 1), Pixel(22, 2),
    Pixel(21, 9), Pixel(22, 10), Pixel(22, 11), Pixel(22, 12), Pixel(22, 13), Pixel(
        21, 14), Pixel(19, 15), Pixel(20, 15), Pixel(19, 16), Pixel(20, 16), Pixel(21, 16), Pixel(6, 9), Pixel(6, 15), Pixel(7, 16), Pixel(7, 17), Pixel(6, 17),
    Pixel(7, 24), Pixel(6, 25), Pixel(6, 26), Pixel(7, 26), Pixel(4, 28), Pixel(4, 29), Pixel(
        4, 30), Pixel(5, 30), Pixel(14, 28), Pixel(14, 29), Pixel(14, 30), Pixel(15, 30), Pixel(16, 29), Pixel(16, 28), Pixel(12, 23), Pixel(12, 26), Pixel(13, 26),
    Pixel(13, 27), Pixel(13, 25), Pixel(13, 24), Pixel(14, 24), Pixel(15, 24), Pixel(16, 24), Pixel(
        17, 24), Pixel(18, 24), Pixel(19, 24), Pixel(20, 23), Pixel(21, 22), Pixel(22, 21), Pixel(22, 20),
    Pixel(22, 19), Pixel(14, 26), Pixel(0, 4), Pixel(1, 4), Pixel(18, 16), Pixel(
        18, 17), Pixel(19, 17), Pixel(20, 17), Pixel(0, 5), Pixel(0, 6), Pixel(0, 7),
    Pixel(1, 7), Pixel(0, 8), Pixel(0, 15), Pixel(0, 16), Pixel(1, 16), Pixel(
        0, 17), Pixel(1, 17), Pixel(6, 4), Pixel(7, 5), Pixel(8, 6), Pixel(9, 7),
    Pixel(13, 17), Pixel(12, 16)]
TigersLogoBadPixels = [Pixel(3, 0), Pixel(4, 0), Pixel(5, 1), Pixel(6, 1), Pixel(
    7, 1), Pixel(8, 1), Pixel(9, 1), Pixel(11, 0), Pixel(12, 0), Pixel(13, 0), Pixel(10, 1), Pixel(14, 0), Pixel(17, 1), Pixel(18, 2), Pixel(19, 3),
    Pixel(0, 3), Pixel(1, 4), Pixel(2, 5), Pixel(3, 6), Pixel(3, 7), Pixel(2, 7), Pixel(
        2, 8), Pixel(1, 8), Pixel(0, 9), Pixel(7, 16), Pixel(0, 18), Pixel(1, 18),
    Pixel(1, 19), Pixel(1, 20), Pixel(1, 21), Pixel(2, 20), Pixel(0, 22), Pixel(
        0, 23), Pixel(0, 24), Pixel(1, 23), Pixel(11, 8), Pixel(12, 8), Pixel(13, 7), Pixel(14, 7), Pixel(14, 8), Pixel(15, 8)]
TwinsLogoBadPixels = []
WhiteSoxLogoBadPixels = []
YankeesLogoBasPixels = []

teamsDict = {"Brewers.png": BrewersLogoBadPixels,
             "Angels.png": AngelsLogoBadPixels,
             "Astros.png": AstrosLogoBadPixels,
             "BlueJays.png": BlueJaysLogoBadPixels,
             "Braves.png": BravesLogoBadPixels,
             "Cubs.png": CubsLogoBadPixels,
             "DiamondBacks.png": DiamondBacksBadPixels,
             "Mariners.png": MarinersLogoBadPixels,
             "Marlins.png": MarlinsLogoBadPixels,
             "Mets.png": MetsLogoBadPixels,
             "Nationals.png": NationalsLogoBadPixels,
             "Orioles.png": OriolesLogoBadPixels,
             "Phillies.png": PhilliesLogoBadPixels,
             "Rangers.png": RangersLogoBadPixels,
             "Rays.png": RaysLogoBadPixels,
             "Reds.png": RedsLogoBadPixels,
             "RedSox.png": RedSoxLogoBadPixels,
             "Tigers.png": TigersLogoBadPixels,
             "Twins.png": TwinsLogoBadPixels,
             "WhiteSox.png": WhiteSoxLogoBadPixels,
             "Yankees.png": YankeesLogoBasPixels}


def GetBadPixelList(teamLogoFileName):
    if teamLogoFileName in teamsDict:
        return teamsDict[teamLogoFileName]
    else:
        return []
