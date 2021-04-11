from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
import time
import os


options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.pixel_mapper_config = "U-mapper"
options.hardware_mapping = 'adafruit-hat-pwm'
options.pwm_lsb_nanoseconds = 130
options.gpio_slowdown = 4
matrix = RGBMatrix(options=options)
buffer = matrix.CreateFrameCanvas()


image = Image.open("./TeamLogos/MLB/Brewers.png")

image.thumbnail((matrix.width-33, matrix.height-33), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'), 0, 0)
#matrix.Fill(255, 0, 0)
matrix.SetPixel(0, 5, 0, 0, 0)
matrix.SetPixel(1, 4, 0, 0, 0)
matrix.SetPixel(2, 3, 0, 0, 0)
matrix.SetPixel(3, 2, 0, 0, 0)
matrix.SetPixel(4, 1, 0, 0, 0)
matrix.SetPixel(5, 1, 0, 0, 0)
matrix.SetPixel(5, 0, 0, 0, 0)
matrix.SetPixel(7, 0, 0, 0, 0)


while True:
    x = 1
