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
        options.parallel = 1
        options.pixel_mapper_config = "U-mapper"
        options.hardware_mapping = 'adafruit-hat-pwm'
        self.matrix = RGBMatrix(options=options)
        self.buffer = self.matrix.CreateFrameCanvas()

    def RenderScene(self, scene):

        scene.Home_Team_Logo_Image.thumbnail(
            (self.matrix.width-35, self.matrix.height-35), Image.ANTIALIAS)
        scene.Away_Team_Logo_Image.thumbnail(
            (self.matrix.width-35, self.matrix.height-35), Image.ANTIALIAS)

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

        if scene.InningText:
            textFont = graphics.Font()
            font.LoadFont(x + "/fonts/6x13.bdf")
            positionOffset = (len(scene.InningText)/2) * 6
            graphics.DrawText(self.buffer, font, 32-positionOffset,
                              13, textColor, scene.InningText)
        else:
            textFont = graphics.Font()
            font.LoadFont(x + "/fonts/5x7.bdf")
            y_pos = 7
            for line in scene.AdditionalText:
                positionOffset = (len(line)/2) * 4
                if len(line) % 2 == 0:
                    positionOffset += 4
                graphics.DrawText(self.buffer, font, 32-positionOffset,
                                  y_pos, textColor, line)
                y_pos = y_pos + 8

        self.buffer = self.matrix.SwapOnVSync(self.buffer)

    def printText(self, text):
        self.buffer.Clear()
        textColor = graphics.Color(0, 0, 255)
        font = graphics.Font()
        font.LoadFont(x + "/fonts/6x13.bdf")
        positionOffset = (len(text)/2) * 6
        graphics.DrawText(self.buffer, font, 32-positionOffset,
                          13, textColor, text)
        self.buffer = self.matrix.SwapOnVSync(self.buffer)
