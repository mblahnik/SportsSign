#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

image = Image.open("milB.png")
image2 = Image.open("whitesox.png")

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

# Make image fit our screen.
image.thumbnail((matrix.width-35, matrix.height-35), Image.ANTIALIAS)
image2.thumbnail((matrix.width-35, matrix.height-35), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'), -3, 30)
matrix.SetImage(image2.convert('RGB'), 45, 30)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
