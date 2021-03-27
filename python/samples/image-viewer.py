#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
import requests

image_url = "https://lh3.googleusercontent.com/proxy/V6KZ6m33ku3Vdj7zsSnsi6uDIUuzfNhxgFRg4kV89P0cQ-ExSaBF5ir-kcCw8WdsxamUl1bZ7l_gNr-Nfk0t7xxhEsuIL-4Xh6IpROUyFK0XZhzWn3mvinbn4W9yYyOgjD-wzlU2a3g4Ic-TMB4p=p-h96-w96-rw"
image2_url = "https://lh6.googleusercontent.com/proxy/Kuysu_p4Eeijarmvn5-aOATsarGJPVw7z4YJ0iE8zIGHSldg1_pJO5UCD7AwRcodgLv1IATwq94MDJmL7X5EhPNuw6J32PJCeRfkNnwmCm3GLAWclIokDA12QY2RLR-LKtL8ojVkwKBx9-A0q2yI=p-h96-w96-rw"

image = Image.open(requests.get(image_url, stream=True).raw)
image2 = Image.open(requests.get(image2_url, stream=True).raw)

font = graphics.Font()
font.LoadFont("./fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 255)
my_text = "@"

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.pixel_mapper_config = "U-mapper"
# If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options=options)
#offscreen_canvas = matrix.CreateFrameCanvas()

# Make image fit our screen.
image.thumbnail((matrix.width-35, matrix.height-35), Image.ANTIALIAS)
image2.thumbnail((matrix.width-35, matrix.height-35), Image.ANTIALIAS)

#graphics.DrawText(offscreen_canvas, font, 14, 20, textColor, my_text)

matrix.SetImage(image.convert('RGB'), -2, 33)
matrix.SetImage(image2.convert('RGB'), 37, 33)

# matrix.SwapOnVSync(offscreen_canvas)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
