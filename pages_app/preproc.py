# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
from PIL import Image

def show_preproc():
    
   
    st.header("Exploratory Data Analysis", divider='red')
    
    
    st.write(
         """
         Exploratory Data Analysis (EDA) is the initial step in analyzing a dataset. It involves investigating the characteristics of the data to uncover patterns, trends, and potential relationships between variables.  
         
         Through techniques like data visualization, calculating summary statistics, and identifying outliers, EDA helps understand the structure of the data, assess its quality, and gain valuable insights to inform further analysis or machine learning modelling.
         """)
     
    st.subheader("Optbinnning")
    
    st.write(
         """
         Optbinning is a powerful EDA technique for preparing continuous data  for machine learning models. Optbinning employs an optimization algorithm that finds the best cut points within the data. 
        
         """)
         
    st.markdown("**Examples of optbinning for some features in the data set:**") 
         
    # Create two columns with equal width
    col1, col2 = st.columns(2)
    

    # Define image dictionary with filenames as keys and image objects as values
    images = {
        "Affluence Score": Image.open("images/aff_opt.jpg"),
        "Age": Image.open("images/age_opt.jpg"),
        "Gender": Image.open("images/gender_opt.jpg"),
        "Income": Image.open("images/income_opt.jpg"),
        "Sum Assured": Image.open("images/sa_opt.jpg"),
    }
    
    # Define border width and color (adjust values as needed)
    border_width = 10
    border_color = (220, 220, 220)  # Light gray border

    with col1:
        # Create a dropdown menu with image names as options
        selected_image = st.selectbox("Select a Feature:", list(images.keys()))
    
    with col2:
        # Display the selected image
        bordered_image = Image.new("RGB", (images[selected_image].width + 2 * border_width, 
                                    images[selected_image].height + 2 * border_width), border_color)
        # Paste the original image onto the new image with border2
        bordered_image.paste(images[selected_image], (border_width, border_width))
        st.image(bordered_image, use_column_width=True, caption='Optbinning details for '+selected_image)


    #image_path = "images/AGE BINNING.jpeg"
    
    # Open the image using Pillow library
    #image = Image.open(image_path)
    
    # Display the image with an optional caption
    #st.image(image)

  