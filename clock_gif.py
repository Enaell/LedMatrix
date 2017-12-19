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


#check sudoers to add scripts. and think about chmod new scripts too

import os
import sys
import Image
import ImageDraw
import ImageFont
import time
import datetime
from rgbmatrix import Adafruit_RGBmatrix


def hex_to_rgb(value):
  value = value.lstrip('#')
  lv = len(value)
  return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))



#r = sys.argv[1]
#g = sys.argv[2]
#b = sys.argv[3]

#print (r)
#print (g)
#print (b)

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 2)
matrix.SetWriteCycles(3)



# Then scroll image across matrix...
while not (os.path.isfile('/home/pi/Documents/LEDMatrix/rpi-rgb-led-matrix-master/stopLedScript.txt')) :
  # Start off top-left, move off bottom-right
	# IMPORTANT: *MUST* pass image ID, *NOT* image object!

        gif = os.listdir("/home/pi/Documents/LEDMatrix/rpi-rgb-led-matrix-master/Gifs")[0]
     #   print (gif)

        gifDirectory = os.listdir("/home/pi/Documents/LEDMatrix/rpi-rgb-led-matrix-master/gifDirectory/" + gif)
      #  print len(gifDirectory)

          
        hexa = os.listdir("/home/pi/Documents/LEDMatrix/rpi-rgb-led-matrix-master/Color")[0]


        curDate = datetime.datetime.now().strftime("%H:%M")

        image = Image.new("1", (30, 12)) # Can be larger than matrix if wanted!!
        image = image.convert("RGBA")
        draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims

	draw.text((0, 0), curDate, fill=hex_to_rgb(hexa))

#        draw.text((0, 0), curDate, fill=(int(float(r)), int(float(g)), int(float(b))))
     #   matrix.Clear()	

        matrix.SetImage(image.im.id, 0, 0)


        for n in range(1, len(gifDirectory)+ 1) :
          pict = Image.open("/home/pi/Documents/LEDMatrix/rpi-rgb-led-matrix-master/gifDirectory/" + gif + "/" + str(n) + ".jpg")
          pict.load()          # Must do this before SetImage() calls
          matrix.SetImage(pict.im.id, 31, 0)
          time.sleep(0.5)


        del draw
        del image
        



matrix.Clear()
os.remove('/home/pi/Documents/LEDMatrix/rpi-rgb-led-matrix-master/stopLedScript.txt')
