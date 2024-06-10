# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st


def show_home():
    st.header("Insurance Claim Modelling System", divider='red')
    st.write(
        """
        Insurance claim machine learning models are powerful tools that analyze vast datasets to
        predict the likelihood and cost of future claims, by identifying
        patterns that traditional methods might miss. 
        
        This web page summarizes how machine learning tackles insurance claims, including the data used to train the model, the cleaning and preparation 
        steps it undergoes, the specific machine learning algorithm employed, and 
        the valuable outputs it generates.
        
        Utlizing machine learning in insurance industry allows insurers to make more informed decisions to improve the 
        efficiency and accuracy of the claims process.
        """
    )
    
    st.subheader("Steps in creating an Insurance claim model:")
    items = ["Data Collection", "Data Cleaning and Pre Processing", "Model Selection and Training", "Model Calibration and Validation","Model Deployment and Monitoring"]

    for i, item in enumerate(items):
        st.markdown(f"{i+1}. {item}")