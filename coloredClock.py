#!/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import ImageFont
import time
import datetime
from rgbmatrix import Adafruit_RGBmatrix


# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 2)
matrix.SetWriteCycles(2)


rTime = 0
gTime = 1
bTime = 0

r =  255
g = 0
b = 0

# Then scroll image across matrix...
while 1 : # Start off top-left, move off bottom-right
	# IMPORTANT: *MUST* pass image ID, *NOT* image object!

        image = Image.new("1", (30, 12)) # Can be larger than matrix if wanted!!
        image = image.convert("RGBA")
	draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
        curDate = datetime.datetime.now().strftime("%H:%M")
        draw.text((0, 0), curDate, fill=(r,g,b))
        matrix.SetImage(image.im.id, 0, 0)

        if  gTime > 0:
                r -= 1
                g += 1
                if g == 255:
                        gTime = 0
                        bTime = 1
        elif bTime > 0:
                g -= 1
                b += 1
                if b == 255:
                        bTime = 0
                        rTime = 1
        elif rTime > 0:
                b -= 1
                r += 1
                if r == 255:
                        rTime = 0
                        gTime = 1

	time.sleep(20)
	del draw
	del image
	matrix.Clear()

	

matrix.Clear()
