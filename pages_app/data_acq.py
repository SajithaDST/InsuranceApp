# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:10:05 2024

@author: sajit
"""

import streamlit as st
from PIL import Image

def show_data():
    
    st.header("System Architecture", divider='red')
    
    st.write(
        """
        A machine learning model system architecture involves a series of interconnected components that work together to leverage machine learning for various insurance tasks.

        """
    )
    
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>High-level Architecture</u></h5>", unsafe_allow_html=True)
     
    col1, col2,col3 = st.columns([1,4,1])
     
    with col2:     
            # Load the image
            image = Image.open("images/sys-arch.jpg")
            st.image(image, use_column_width=True)