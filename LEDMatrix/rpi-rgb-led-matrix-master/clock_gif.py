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

totoro1 = Image.open("testTotoro/testtotorogif_frame_1.jpg")
totoro1.load()          # Must do this before SetImage() calls

totoro2 = Image.open("testTotoro/testtotorogif_frame_2.jpg")
totoro2.load()          # Must do this before SetImage() calls

totoro3 = Image.open("testTotoro/testtotorogif_frame_3.jpg")
totoro3.load()          # Must do this before SetImage() calls



# Then scroll image across matrix...
while 1 : # Start off top-left, move off bottom-right
	# IMPORTANT: *MUST* pass image ID, *NOT* image object!

        image = Image.new("1", (30, 12)) # Can be larger than matrix if wanted!!
        image = image.convert("RGBA")
	draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
        curDate = datetime.datetime.now().strftime("%H:%M")
        draw.text((0, 0), curDate, fill=(128, 128, 128))
        matrix.SetImage(image.im.id, 0, 0)


        for n in range(0, 16) :
            if n % 8 == 0:
                matrix.SetImage(totoro1.im.id, 31, 0)
            if n % 8 == 1:
                matrix.SetImage(totoro2.im.id, 31, 0)
            if n % 8 == 2:
                matrix.SetImage(totoro1.im.id, 31, 0)
            if n % 8 == 3:
                matrix.SetImage(totoro2.im.id, 31, 0)
            if n % 8 == 4:
                matrix.SetImage(totoro1.im.id, 31, 0)
            if n % 8 == 5:
                matrix.SetImage(totoro3.im.id, 31, 0)
            if n % 8 == 6:
                matrix.SetImage(totoro1.im.id, 31, 0)
            if n % 8 == 7:
                matrix.SetImage(totoro3.im.id, 31, 0)
            time.sleep(0.5)

        matrix.Clear()	
	del draw
	del image

	
matrix.Clear()
