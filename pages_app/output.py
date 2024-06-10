# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
import pandas as pd

def show_output():
    st.header("Model Predictions", divider='red')
    st.write(
        """
        The prediction phase is where the trained model is used to make predictions on new and unseen data, after the model learns from historical / training data.
        
        """
    )
    
    st.subheader("**Final Output Summary**") 
    
    col_content = [
        "Total No. of Policies = 55135",
        "Total No. of Risky Policies = 1435",
        "Total No. of Claims = 48",
        "Total No. of Claims Captured = 30",
        "Percentage of Claims Captured = 62.5 %",
        "Percentage of Risky Policies captured in the top 5 % = 2.6%",
        "Percentage of Risky Annual Premuim captured in the top 5 % = 5%"
    ]

     

    for item in col_content:
        st.markdown(f"- {item}")  # Use f-string for dynamic formatting
        
    
    st.subheader("**Examples of risk predictions for some policies**") 
     
    
    data = {'Policy No': ['P2378AH', 'P6689GD', 'P0089TU'], 'Risk Probability': [0.92, 0.54, 0.12], 'Risk Bucket': ['Bucket 1', 'Bucket 29', 'Bucket 46'], 'Risk Category': ['High Risk', 'Moderate Risk', 'Low Risk']}
    df = pd.DataFrame(data)
    
    # Options for dropdown selection
    dropdown_options = list(df['Policy No'].unique())  
    
    # Create two columns with equal width
    col1, col2 = st.columns([1,4])
    
    with col1:
        # Create a dropdown menu
        selected_col2_value = st.selectbox("Select Policy No:", dropdown_options)
    
    # Filter DataFrame based on selection
    with col2:
       st.write("")
     
    st.write("Policy Risk Details")
    if selected_col2_value:
      filtered_df = df[df['Policy No'] == selected_col2_value]
      st.dataframe(filtered_df, hide_index=True,use_container_width=True)
    else:
      st.write("Select a value from the dropdown to filter the table.")