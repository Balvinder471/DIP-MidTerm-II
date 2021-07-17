# -*- coding: utf-8 -*-

import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import tensorflow as tf
#from keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
#from keras.models import load_model

html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">End Term Practical</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Image Transformation
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))
kind = st.selectbox("Shear-X: ",
                     ["Shear-X", "Shear-Y", "Translation", "Rotation", "Cropping", "Reflection"])
value = st.text_input("Enter the amount of shear", "Type Here ...")

value = float(value)

import cv2
from  PIL import Image, ImageOps
def apply_transform(image_data, value):
  #img = image.load_img(image_data, target_size=(224, 224))
  #image = image.img_to_array(img)
  #img_reshap= np.expand_dims(image, axis=0)
  #img_reshap = preprocess_input(img_reshap)

  xshear = np.float32([[1, 0, 0],
             	[value, 1  , 0],
            	[0, 0  , 1]])

  yshear = np.float32([[1, value, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])
   
  if kind == "Shear-X":
     image_data =  cv.warpPerspective(img, xshear , (int(cols*1.5),int(rows*1.5)))
  elif kind == "Shear-Y":
     image_data =  cv.warpPerspective(img, yshear , (int(cols*1.5),int(rows*1.5)))
  st.image(image_data, use_column_width=True)
  return 0
if file is None:
  st.text("Please upload an Image file")
else:
  file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)
  
    
if st.button("Apply Transformation"):
  result=apply_transform(image, value)
  
if st.button("About"):
  st.header("Balvinder Singh")
  st.subheader("Student, Department of Computer Science 6th Semester")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">DIP Endterm Practical</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)