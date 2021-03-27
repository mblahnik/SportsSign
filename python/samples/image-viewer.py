#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

image = Image.open(image_file)

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
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'), 30, 30)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
