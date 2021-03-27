#!/usr/bin/env python
from samplebase import SampleBase


class MyTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()

        while True:
            offset_canvas.SetPixel(15, 15, 0, 0, 255)

            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


# Main function
if __name__ == "__main__":
    simple_square = MyTest()
    if (not simple_square.process()):
        simple_square.print_help()
