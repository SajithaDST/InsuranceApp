# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:10:05 2024

@author: sajit
"""

import streamlit as st
from PIL import Image

def show_data():
    
    st.header("Data Acquisition", divider='red')
    
    st.write(
        """
        Machine learning models predictions depend on the quality and relevance of the data they are trained on. 
        
        This data can come from various sources, including historical historical claims data, customer demographics and health information.

        """
    )
    
    st.subheader("Overview of the data used in the project:")
       
       
    col_content = [
        "Total No. of Records = 521300",
        "Total No. of Columns = 20",
        "Total No. of Targets (No of Claims) = 1084"
    ]

     

    for item in col_content:
        st.markdown(f"- {item}")  # Use f-string for dynamic formatting
    
            
            
    st.subheader("Snapshot of the input data")     
            # Load the image
    image = Image.open("images/dataset.jpg")
    st.image(image, use_column_width=True)