# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from IPython.display import HTML

def show_model():
   
    st.header("Model Training and Evaluation", divider='red')
    
    
    st.write(
         """
         To identify the best model for the project, Extreme Gradient Boosting (XGBoost), Light Gradient Boosting Machine (LGBM) and Categorical Boosting (CatBoost) models were selected 
         and the performance of these models were evaluated on the provided data.
         """)
         
    st.subheader("**Summary of model performance metrics:**") 
  
    Evaluation_Results = pd.DataFrame(np.zeros((3,3)), columns=['Precision', 'Recall','F1 Score'])
    Evaluation_Results.index=['XGBoost','LGBM','CatBoost']
    Evaluation_Results.loc['XGBoost'] = pd.Series([93,95,94], index=Evaluation_Results.columns)
    Evaluation_Results.loc['LGBM'] = pd.Series([92,89,91], index=Evaluation_Results.columns)
    Evaluation_Results.loc['CatBoost'] = pd.Series([91,88,90], index=Evaluation_Results.columns)

    
    st.dataframe(Evaluation_Results,use_container_width=True)


    # Display the text centered within the column
    
    st.markdown("\n")
    st.subheader("**ROC-AUC Curve model wise**") 
    col1, col2,col3 = st.columns(3)
    
    with col1:
        st.image(Image.open("images/ROC Model 1.jpg"), use_column_width=True,caption='ROC Curve for XGBoost')
   
    with col2:
        st.image(Image.open("images/ROC Model 2.jpg"), use_column_width=True,caption='ROC Curve for LGBM')
    
    with col3:
        st.image(Image.open("images/ROC Model 3.jpg"), use_column_width=True,caption='ROC Curve for CatBoost')
    
    st.markdown("\n")
    st.write(
         """
         Based on the performance characteristics, XGBoost model was selected as the final model.
         """)
    
   
   
    
    
    
    

