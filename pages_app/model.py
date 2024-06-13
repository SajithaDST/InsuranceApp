# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


def show_model():
   
    st.header("Model Training and Evaluation", divider='red')
    
    
    st.write(
         """
         To identify the best model for the project, Extreme Gradient Boosting (XGBoost), Light Gradient Boosting Machine (LGBM) and Categorical Boosting (CatBoost) models were selected 
         and the performance of these models were evaluated on the provided data.
         """)
         
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Model Performance Summary</u></h5>", unsafe_allow_html=True)
  
    Evaluation_Results = pd.DataFrame(np.zeros((3,3)), columns=['Precision', 'Recall','F1 Score'])
    Evaluation_Results.index=['XGBoost','LGBM','CatBoost']
    Evaluation_Results.loc['XGBoost'] = pd.Series([93,95,94], index=Evaluation_Results.columns)
    Evaluation_Results.loc['LGBM'] = pd.Series([92,89,91], index=Evaluation_Results.columns)
    Evaluation_Results.loc['CatBoost'] = pd.Series([91,88,90], index=Evaluation_Results.columns)

    col1, col2,col3 = st.columns([1,8,1])
             
    with col2:  
        st.dataframe(Evaluation_Results,use_container_width=True)


    # Display the text centered within the column
    
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>ROC-AUC Curve model wise</u></h5>", unsafe_allow_html=True)
    
    col1, col2,col3 = st.columns([1,10,1])
                
    with col2:
        
        col1, col2,col3 = st.columns(3)
        
        with col1:
            st.image(Image.open("images/ROC Model 1.jpg"), use_column_width=True,caption='ROC Curve for XGBoost')
       
        with col2:
            st.image(Image.open("images/ROC Model 2.jpg"), use_column_width=True,caption='ROC Curve for LGBM')
        
        with col3:
            st.image(Image.open("images/ROC Model 3.jpg"), use_column_width=True,caption='ROC Curve for CatBoost')
        
        st.markdown("\n")
        st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Final selected model with hyperparameters</u></h5>", unsafe_allow_html=True)
        st.write(
             """
             Based on the performance characteristics, XGBoost model was selected as the final model with below hyperparameters:
             """)
             
    col1, col2,col3 = st.columns([1,1.5,1])
                
    with col2:  
        image = Image.open("images/modelhpm.jpg")
        st.image(image)
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Final Model Output Summary</u></h5>", unsafe_allow_html=True)
    
    col1, col2,col3 = st.columns([1,3.5,1])
                
    with col2:  
        image = Image.open("images/kpis.jpg")
        st.image(image)
 
   
    
    
    
    
