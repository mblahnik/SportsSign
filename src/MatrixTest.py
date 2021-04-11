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

img_x = 0
img_y = 0

image.thumbnail((matrix.width-33, matrix.height-33), Image.ANTIALIAS)

#matrix.SetImage(image.convert('RGB'), 0, 0)


matrix.SetImage(image.convert('RGB'), img_x, img_y)
#matrix.Fill(255, 0, 0)
matrix.SetPixel(img_x + 0, img_y + 5, 0, 0, 0)
matrix.SetPixel(img_x + 1, img_y + 4, 0, 0, 0)
matrix.SetPixel(img_x + 2, img_y + 3, 0, 0, 0)
matrix.SetPixel(img_x + 3, img_y + 2, 0, 0, 0)
matrix.SetPixel(img_x + 4, img_y + 1, 0, 0, 0)
matrix.SetPixel(img_x + 5, img_y + 1, 0, 0, 0)
matrix.SetPixel(img_x + 6, img_y + 0, 0, 0, 0)
matrix.SetPixel(img_x + 8, img_y + 0, 0, 0, 0)
matrix.SetPixel(img_x + 25, img_y + 0, 0, 0, 0)
matrix.SetPixel(img_x + 26, img_y + 0, 0, 0, 0)
matrix.SetPixel(img_x + 27, img_y + 1, 0, 0, 0)
matrix.SetPixel(img_x + 28, img_y + 2, 0, 0, 0)
matrix.SetPixel(img_x + 0, img_y + 17, 0, 0, 0)
matrix.SetPixel(img_x + 0, img_y + 18, 0, 0, 0)
matrix.SetPixel(img_x + 0, img_y + 19, 0, 0, 0)
matrix.SetPixel(img_x + 1, img_y + 19, 0, 0, 0)
matrix.SetPixel(img_x + 1, img_y + 20, 0, 0, 0)
matrix.SetPixel(img_x + 1, img_y + 21, 0, 0, 0)
matrix.SetPixel(img_x + 2, img_y + 22, 0, 0, 0)
matrix.SetPixel(img_x + 2, img_y + 23, 0, 0, 0)
matrix.SetPixel(img_x + 2, img_y + 24, 0, 0, 0)
matrix.SetPixel(img_x + 3, img_y + 24, 0, 0, 0)
matrix.SetPixel(img_x + 3, img_y + 25, 0, 0, 0)
matrix.SetPixel(img_x + 4, img_y + 26, 0, 0, 0)
matrix.SetPixel(img_x + 4, img_y + 27, 0, 0, 0)
matrix.SetPixel(img_x + 5, img_y + 27, 0, 0, 0)
matrix.SetPixel(img_x + 5, img_y + 28, 0, 0, 0)
matrix.SetPixel(img_x + 6, img_y + 27, 0, 0, 0)
matrix.SetPixel(img_x + 6, img_y + 28, 0, 0, 0)
matrix.SetPixel(img_x + 6, img_y + 29, 0, 0, 0)
matrix.SetPixel(img_x + 7, img_y + 28, 0, 0, 0)
matrix.SetPixel(img_x + 7, img_y + 29, 0, 0, 0)
matrix.SetPixel(img_x + 8, img_y + 30, 0, 0, 0)

# dasd
matrix.SetPixel(img_x + 22, img_y + 30, 0, 0, 0)

matrix.SetPixel(img_x + 23, img_y + 29, 0, 0, 0)

matrix.SetPixel(img_x + 24, img_y + 28, 0, 0, 0)

matrix.SetPixel(img_x + 25, img_y + 27, 0, 0, 0)
matrix.SetPixel(img_x + 25, img_y + 25, 0, 0, 0)

matrix.SetPixel(img_x + 26, img_y + 26, 0, 0, 0)
matrix.SetPixel(img_x + 26, img_y + 25, 0, 0, 0)

matrix.SetPixel(img_x + 27, img_y + 24, 0, 0, 0)
matrix.SetPixel(img_x + 27, img_y + 23, 0, 0, 0)
matrix.SetPixel(img_x + 27, img_y + 22, 0, 0, 0)

matrix.SetPixel(img_x + 28, img_y + 22, 0, 0, 0)
matrix.SetPixel(img_x + 28, img_y + 23, 0, 0, 0)
matrix.SetPixel(img_x + 28, img_y + 24, 0, 0, 0)


while True:
    x = 1
