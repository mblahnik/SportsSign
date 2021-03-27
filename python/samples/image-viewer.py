#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image

image = Image.open("milB.png")
image2 = Image.open("whitesox.png")

font = graphics.Font()
font.LoadFont("./fonts/7x13.bdf")
textColor = graphics.Color(255, 0, 0)
my_text = "dsadasd"

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
offscreen_canvas = matrix.CreateFrameCanvas()

# Make image fit our screen.
image.thumbnail((matrix.width-35, matrix.height-35), Image.ANTIALIAS)
image2.thumbnail((matrix.width-35, matrix.height-35), Image.ANTIALIAS)

#matrix.SetImage(image.convert('RGB'), -2, 33)
#matrix.SetImage(image2.convert('RGB'), 37, 33)

graphics.DrawText(offscreen_canvas, font, 0, 0, textColor, my_text)
matrix.SwapOnVSync(offscreen_canvas)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
