'''
Created on Feb 25, 2020

@author: rapienac
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO

def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        print("Load image(): Unable to open" + filename)
        return None #none is a 
