# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
import pandas as pd
from PIL import Image

def show_output():
    st.header("Model Deployment", divider='red')
    st.write(
        """
        Model Deployment involves operationalizing trained models for production use, enabling them to receive data and generate predictions. This can be achieved through APIs for low-latency, real-time scenarios, or batch engines for efficient processing of large datasets offline. 
        
        """
    )
 
    col1, col2,col3 = st.columns([1,3.5,1])
                
    with col2:  
        image = Image.open("images/deploy.jpg")
        st.image(image)
         
 
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Model Forecast Calculator</u></h5>", unsafe_allow_html=True)
   
    data = {'Policy Number': ['P2378AH', 'P6689GD', 'P0089TU','P5567BU','P9545VZ'], 'Risk Probability': [0.92, 0.54, 0.12,0.62,0.84], 'Risk Bucket': ['Bucket 1', 'Bucket 29', 'Bucket 46','Bucket 33','Bucket 2'], 'Risk Category': ['High Risk', 'Moderate Risk', 'Low Risk', 'Moderate Risk','High Risk']}
    df = pd.DataFrame(data)
    
    # Options for dropdown selection
    dropdown_options = list(df['Policy Number'].unique())  
    
    # Create two columns with equal width
    col1, col2,col3 = st.columns([1,3,1])
     
    with col2: 
        st.markdown("The deployed model outputs risk predictors for a given input set of policy details. Some examples are given below.")
        # Create a dropdown menu
        st.markdown("\n")
        selected_col2_value = st.selectbox("Select Policy Number:", dropdown_options)
    

     
    st.write("Policy Risk Details")
    if selected_col2_value:
      filtered_df = df[df['Policy Number'] == selected_col2_value]
      st.dataframe(filtered_df, hide_index=True,use_container_width=True)
    else:
      st.write("Select a value from the dropdown to filter the table.")
