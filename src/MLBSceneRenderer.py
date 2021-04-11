from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
import time
import os

x = os.path.dirname(os.path.abspath(__file__))


class MLBSceneRenderer:

    def __init__(self):
        super().__init__()
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 64
        options.chain_length = 2
        options.pixel_mapper_config = "U-mapper"
        options.hardware_mapping = 'adafruit-hat-pwm'
        options.pwm_lsb_nanoseconds = 130
        options.gpio_slowdown = 4
        self.matrix = RGBMatrix(options=options)
        self.buffer = self.matrix.CreateFrameCanvas()

    def RenderScene(self, scene):

        scene.Home_Team_Logo_Image.thumbnail(
            (self.matrix.width-33, self.matrix.height-33), Image.ANTIALIAS)
        scene.Away_Team_Logo_Image.thumbnail(
            (self.matrix.width-33, self.matrix.height-33), Image.ANTIALIAS)

        font = graphics.Font()
        font.LoadFont(x + "/fonts/7x13.bdf")
        bigfont = graphics.Font()
        bigfont.LoadFont(x + "/fonts/10x20.bdf")
        textColor = graphics.Color(255, 255, 255)
        my_text = "@"
        score = scene.Away_Team_Score + "-" + scene.Home_Team_Score
        scorePositionOffset = (score.index("-")+1) * 8
        self.buffer.Clear()
        graphics.DrawText(self.buffer, bigfont, 32-scorePositionOffset,
                          32, textColor, score)
        graphics.DrawText(self.buffer, font, 29, 50, textColor, my_text)
        self.buffer.SetImage(scene.Away_Team_Logo_Image.convert('RGB'), -2, 33)
        self.buffer.SetImage(scene.Home_Team_Logo_Image.convert('RGB'), 37, 33)

        if scene.MainText:
            textFont = graphics.Font()
            textFont.LoadFont(x + "/fonts/6x13.bdf")
            positionOffset = (len(scene.MainText)/2) * 6
            graphics.DrawText(self.buffer, textFont, 32-positionOffset,
                              13, textColor, scene.MainText)
        else:
            textFont = graphics.Font()
            textFont.LoadFont(x + "/fonts/5x7.bdf")
            y_pos = 7
            for line in scene.AdditionalText:
                positionOffset = (len(line)/2) * 4
                if len(line) % 2 == 0:
                    positionOffset += 4
                graphics.DrawText(self.buffer, textFont, 32-positionOffset,
                                  y_pos, textColor, line)
                y_pos = y_pos + 8

        self.cleanUpLogos()

        self.buffer = self.matrix.SwapOnVSync(self.buffer)

    def cleanUpLogos(self):
        self.buffer.SetPixel(0, 36, 0, 0, 0)
        self.buffer.SetPixel(1, 35, 0, 0, 0)
        self.buffer.SetPixel(2, 34, 0, 0, 0)
        self.buffer.SetPixel(3, 34, 0, 0, 0)
        self.buffer.SetPixel(4, 33, 0, 0, 0)
        self.buffer.SetPixel(24, 33, 0, 0, 0)
        self.buffer.SetPixel(25, 33, 0, 0, 0)
        self.buffer.SetPixel(26, 34, 0, 0, 0)
        self.buffer.SetPixel(27, 35, 0, 0, 0)

    def printText(self, text):
        self.buffer.Clear()
        textColor = graphics.Color(0, 0, 255)
        font = graphics.Font()
        font.LoadFont(x + "/fonts/6x13.bdf")
        positionOffset = (len(text)/2) * 6
        graphics.DrawText(self.buffer, font, 32-positionOffset,
                          13, textColor, text)
        self.buffer = self.matrix.SwapOnVSync(self.buffer)
