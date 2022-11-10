import os
import time

from PIL import Image

SOURCE_FOLDER = "source_images/"
RESIZED_FOLDER = "thumbnail_images/"
WIDTH = 300
HEIGHT = 300
PREFIX = "resized-"

if not os.path.exists(RESIZED_FOLDER):
    os.makedirs(RESIZED_FOLDER)

dirs = os.listdir(SOURCE_FOLDER)
print ("THUMBNAIL CREATOR")

for file in dirs:
    image_path = SOURCE_FOLDER + file
    print ( image_path, "--thumbnail_created" )
    im = Image.open( image_path )
    resize = im.resize( (WIDTH, HEIGHT), Image.ANTIALIAS )
    resize.save( RESIZED_FOLDER + PREFIX + file )


time.sleep(1)
print ("FINISHED")