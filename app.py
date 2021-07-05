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
   <center><p style="font-size:30px;color:white;margin-top:10px;">Mid Term 2 Practical</p></center> 
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
kind = st.selectbox("Reflect-X: ",
                     ['Reflect-X', 'Reflect-Y', 'Translation', 'Rotation', 'Shearing', 'Cropping'])

import cv2
from  PIL import Image, ImageOps
def apply_transform(image_data):
  #img = image.load_img(image_data, target_size=(224, 224))
  #image = image.img_to_array(img)
  #img_reshap= np.expand_dims(image, axis=0)
  #img_reshap = preprocess_input(img_reshap)
   
  if kind == "Reflect-X":
     image_data = cv2.flip(image_data, 0)
  elif kind == "Reflect-Y":
     image_data = cv2.flip(image_data, 1)
  st.image(image_data, use_column_width=True)
  return 0
if file is None:
  st.text("Please upload an Image file")
else:
  file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)
    
if st.button("Apply Transformation"):
  result=apply_transform(image)
  
if st.button("About"):
  st.header("Balvinder Singh")
  st.subheader("Student, Department of Computer Engineering 6th Semester")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">DIP Midterm 2</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)