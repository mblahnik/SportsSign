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

image.thumbnail((matrix.width-32, matrix.height-32))

matrix.SetImage(image.convert('RGB'))
#matrix.Fill(255, 0, 0)
# matrix.SetPixel(x,y,r,g,b)

while True:
    x = 1
