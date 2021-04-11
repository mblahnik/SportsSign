from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
import time
import os
from MLBLogoBadPixels import GetBadPixelList

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


image = Image.open("./TeamLogos/MLB/Mariners.png")

img_x = 0
img_y = 0

image.thumbnail((matrix.width-33, matrix.height-33), Image.ANTIALIAS)

#matrix.SetImage(image.convert('RGB'), 0, 0)


matrix.SetImage(image.convert('RGB'), img_x, img_y)
#matrix.Fill(255, 0, 0)
#matrix.SetPixel(img_x + 0, img_y + 5, 0, 0, 0)

for pixel in GetBadPixelList("Mariners.png"):
    matrix.SetPixel(img_x + pixel.x, img_y + pixel.y, 0, 0, 0)

while True:
    x = 1
