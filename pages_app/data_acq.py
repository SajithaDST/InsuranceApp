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
    st.markdown("Key Components :")
    points = ["Data Connector - Involves acquiring and preparing the data needed to train the model.", "Modelling Workbench - Environment to develop, experiment, and train the model.", "Model Validation - Evaluates the model's performance on unseen data to assess its generalization ability.","Model Deployment - Involves releasing the model to a production environment where it can be used to make predictions on real-world data.","Model Tracking - To identify performance degradation over time or changing data patterns that require retraining."]
    st.markdown(f"<ul>{''.join([f'<li>{point}</li>' for point in points])}</ul>", unsafe_allow_html=True)