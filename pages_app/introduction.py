# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
from PIL import Image
import pandas as pd

def show_home():

  
    st.header("Risk Propensity Modelling System", divider='red')
    st.markdown("\n")
    st.write(
        """
       Dive into the world of Risk Modelling with this demo that explores the data used, the data preparation process, the machine learning algorithms employed, and the valuable insights it generates!
        
        """
    )
    
    # Set the banner text and background color
    banner_text = "Model Definition : Predict the likelihood of risk (claims) within the first 3 years of policy initiation."

    col1,col2,col3 = st.columns([1,6,1])
    with col2:
        # Use markdown with HTML formatting to style the banner
        st.markdown(f'<p style="background-color: #CDEBCD; color: #333;  padding: 20px; border: 2px solid grey;font-size:18px;display: flex;justify-content: center;align-items: center;"><b>{banner_text}</b></p>', unsafe_allow_html=True)


    st.markdown("\n")
    # # Text to display
    # text = "&nbsp;Model Definition : Predict the likelihood of risk (claims) within the first 3 years of policy initiation.&nbsp;"
    
    # # Define HTML with inline CSS (replace with desired color)
    # html_string = f"<span style='display: flex;justify-content: center;align-items: center;'><b style='background-color:#CDEBCD; color:#333; padding: 20px;padding-right: 30px; text-align: center;'>{text}</b></span>"
    # st.markdown("\n")
    # st.markdown("\n")
    # # Display the HTML with unsafe_allow_html (use with caution)
    # st.markdown(html_string, unsafe_allow_html=True)
    # st.markdown("\n")
    # st.markdown("\n")
        
    
    # Display the HTML content
    st.markdown("<h6 style='text-align: center; color: black;'>&ensp; &ensp; <u>Risk Propensity Modelling System</u></h6>", unsafe_allow_html=True)
    
    # Define border width and color (adjust values as needed)
    border_width = 5
    border_color = (220, 220, 220)  # Light gray border
    image = Image.open("images/introds.jpg")
    # Display the selected image
    bordered_image = Image.new("RGB", (image.width + 2 * border_width, 
                                image.height + 2 * border_width), border_color)
    # Paste the original image onto the new image with border2
    bordered_image.paste(image, (border_width, border_width))
    
    col1, col2,col3 = st.columns([1,2,1])
    
    with col2:
        st.image(bordered_image,use_column_width =True)
    
    st.markdown("\n")
            
    st.markdown("<h6 style='text-align: center; color: black;'>&ensp; &ensp; Types of Inputs</h6>", unsafe_allow_html=True)
    # Create a sample DataFrame (replace with your data)
    data = {
        'Profile Data': ['Age, Gender, Occupation etc.'],
        'Medical Data': ['Medical history and current health status'],
        'Insurance Policy Data': ['Policy number, Annual premium, Agent information etc.']
    }
    df = pd.DataFrame(data)
    
    
    # Display the DataFrame using st.dataframe
    st.dataframe(df,use_container_width=True,hide_index=True)
  
 
    st.markdown("<h6 style='text-align: center; color: black;'>&ensp; &ensp; Outputs generated by the model</h6>", unsafe_allow_html=True)
    data = {
        'Risk Probability': ['Probability of risk predicted by the model'],
        'Risk Bucket': ['Predicted probability divided into quantiles'],
        'Risk Category': ['High, Moderate, Low ']
    }
    df = pd.DataFrame(data)
    
    # Display the DataFrame using st.dataframe
    st.dataframe(df,use_container_width=True,hide_index=True)        
            
        
        
