# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
from PIL import Image

def show_preproc():
    
   
    st.header("Data Processing Pipeline", divider='red')
    
    
    st.write(
         """
         A data processing pipeline is a systematic approach to handling the flow of data from its raw state to a usable format for analysis. It's essentially a series of steps that transform and prepare the data for its intended use.
     """)
     
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Data Flow Diagram</u></h5>", unsafe_allow_html=True)
          
            # Load the image
    image = Image.open("images/dataflow.jpg")
    st.image(image, use_column_width=True)
    
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Train Data Snapshot</u></h5>", unsafe_allow_html=True)
          
            # Load the image
    image = Image.open("images/dataset.jpg")
    st.image(image, use_column_width=True)
    st.markdown("\n") 
    st.markdown("\n") 
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Feature Predictive Power Asessment:</u></h5>", unsafe_allow_html=True) 
         

    

    # Define image dictionary with filenames as keys and image objects as values
    images = {
        "Affluence Score": Image.open("images/aff_opt.jpg"),
        "Age": Image.open("images/age_opt.jpg"),
        "Gender": Image.open("images/gender_opt.jpg"),
        "Income": Image.open("images/income_opt.jpg"),
        "Sum Assured": Image.open("images/sa_opt.jpg"),
    }
    


    # Create a dropdown menu with image names as options
    selected_image = st.selectbox("Select a Feature:", list(images.keys()))

 

    st.image(images[selected_image], use_column_width=True, caption='Optbinning details for '+selected_image)


    #image_path = "images/AGE BINNING.jpeg"
    
    # Open the image using Pillow library
    #image = Image.open(image_path)
    
    # Display the image with an optional caption
    #st.image(image)

  