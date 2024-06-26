# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
import pandas as pd
from PIL import Image

def show_output():
    st.header("Model Predictive Analysis", divider='red')
    st.write(
        """
        The prediction phase is where the trained model is used to make predictions on new and unseen data, after the model learns from historical / training data.
        
        """
    )

    col1, col2,col3 = st.columns([1,3.5,1])
                
    with col2:  
        image = Image.open("images/summ.jpg")
        st.image(image)
  
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Model Forecast Calculator</u></h5>", unsafe_allow_html=True)
    
    data = {'Policy No': ['P2378AH', 'P6689GD', 'P0089TU','P5567BU','P9545VZ'], 'Risk Probability': [0.92, 0.54, 0.12,0.62,0.84], 'Risk Bucket': ['Bucket 1', 'Bucket 29', 'Bucket 46','Bucket 33','Bucket 2'], 'Risk Category': ['High Risk', 'Moderate Risk', 'Low Risk', 'Moderate Risk','High Risk']}
    df = pd.DataFrame(data)
    
    # Options for dropdown selection
    dropdown_options = list(df['Policy No'].unique())  
    
  
        # Create a dropdown menu
    selected_col2_value = st.selectbox("Select Policy No:", dropdown_options)
    

     
    st.write("Policy Risk Details")
    if selected_col2_value:
      filtered_df = df[df['Policy No'] == selected_col2_value]
      st.dataframe(filtered_df, hide_index=True,use_container_width=True)
    else:
      st.write("Select a value from the dropdown to filter the table.")