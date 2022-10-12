#!/usr/bin/env python

# Reference: https://github.com/FireHead90544/craiyon.py
from craiyon import Craiyon
from craiyon import Craiyon
from PIL import Image # pip install pillow
from io import BytesIO
import base64
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import streamlit as st


def draw_pic(requirements = "pandas play soccer"):
    generator = Craiyon() # Instantiates the api wrapper
    result = generator.generate(requirements) # Generates 9 images by default and you cannot change that
    images = result.images # A list containing image data as base64 encoded strings

    for i in images:
        # Shows the image
        image = Image.open(BytesIO(base64.decodebytes(i.encode("utf-8"))))
        #image.show()
        #img = mpimg.imread('your_image.png')
        imgplot = plt.imshow(image)
        st.image(image, caption='Sunrise by the mountains')
