# converts all jpeg into png in a new dir
from PIL import Image, ImageFilter
import sys
import os

## grab 1st and 2nd arg
jpeg_path = sys.argv[1]
png_path  = sys.argv[2]

## check if 2nd arg exists
if not os.path.exists(png_path):
    os.makedirs(png_path)

## loop 1st arg 
for file_name in os.listdir(jpeg_path):
    clean_name = os.path.splitext(file_name)[0]
    img = Image.open(f'{jpeg_path}{file_name}')

    ## convert to png
    img.save(f'{png_path}/{clean_name}.png','png')
    print('all done')

# count total files
list_jpeg    = os.listdir(jpeg_path) 
list_png     = os.listdir(jpeg_path) 
number_jpeg  = len(list_jpeg)
number_png   = len(list_png)

if number_png == number_jpeg:
    print(f'all {number_files} are converted!!!' )
else:
    print(f'not all files could be converted')
