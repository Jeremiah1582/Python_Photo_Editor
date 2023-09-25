# This code edits photos. to get more information about the details of this library you can check out the documentation below: 
#  https://pillow.readthedocs.io/en/stable/

from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import os

path = './imgs' #path to the images 
pathOut = '/editedImg'
path = os.path.expanduser(path)

for filename in os.listdir(path):
    # identify img to change
    img= Image.open(f"{path}/{filename}")
    
    # Manipulate images
    # --grey scale and enlarge
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor = 1.2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    # save to directory
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
    
    
# Remember: 
# make sure you are running the code from the directory of you project