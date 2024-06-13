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
            image = Image.open("images/sysarch.png")
            st.image(image, use_column_width=True)
    
    st.markdown("\n")
    
    with st.container(border=True):
        st.markdown("Key Components :")
        points = ["<span style='color:orange'>Data Connector</span> - Involves acquiring and preparing the data needed to train the model.", "<span style='color:green'>Modelling Workbench</span> - Environment to develop, experiment, and train the model.", "<span style='color:blue'>Model Validation</span> - Evaluates the model's performance on unseen data to assess its generalization ability.","<span style='color:purple'>Model Deployment</span> - Involves releasing the model to a production environment where it can be used to make predictions on real-world data.","<span style='color:gray'>Model Tracking</span> - To identify performance degradation over time or changing data patterns that require retraining."]
        st.markdown(f"<ul>{''.join([f'<li>{point}</li>' for point in points])}</ul>", unsafe_allow_html=True)