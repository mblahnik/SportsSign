from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
import time


class MLBSceneGenerator:

    @staticmethod
    def RenderScene(scene):
        print("Drawing scene")
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 64
        options.chain_length = 2
        options.parallel = 1
        options.pixel_mapper_config = "U-mapper"
        options.hardware_mapping = 'adafruit-hat'
        matrix = RGBMatrix(options=options)

        scene.Home_Team_Logo_Image.thumbnail(
            (matrix.width-35, matrix.height-35), Image.ANTIALIAS)
        scene.Away_Team_Logo_Image.thumbnail(
            (matrix.width-35, matrix.height-35), Image.ANTIALIAS)

        font = graphics.Font()
        font.LoadFont("./fonts/7x13.bdf")
        bigfont = graphics.Font()
        bigfont.LoadFont("./fonts/10x20.bdf")
        textColor = graphics.Color(255, 255, 255)
        my_text = "@"
        score = scene.Away_Team_Score + "-" + scene.Home_Team_Score
        scorePositionOffset = (score.index("-")+1) * 8
        graphics.DrawText(matrix, bigfont, 32-scorePositionOffset,
                          32, textColor, score)
        graphics.DrawText(matrix, font, 29, 50, textColor, my_text)
        matrix.SetImage(scene.Away_Team_Logo_Image.convert('RGB'), -2, 33)
        matrix.SetImage(scene.Home_Team_Logo_Image.convert('RGB'), 37, 33)

        textFont = graphics.Font()
        font.LoadFont("./fonts/5x7.bdf")

        y_pos = 7
        for line in scene.AdditionalText:
            positionOffset = (len(line)/2) * 4
            graphics.DrawText(matrix, font, 32-positionOffset,
                              y_pos, textColor, line)
            y_pos = y_pos + 8

        while True:
            time.sleep(10000)
