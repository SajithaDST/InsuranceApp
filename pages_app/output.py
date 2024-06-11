# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
import pandas as pd

def show_output():
    st.header("Model Predictive Analysis", divider='red')
    st.write(
        """
        The prediction phase is where the trained model is used to make predictions on new and unseen data, after the model learns from historical / training data.
        
        """
    )
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Final Model Output Summary</u></h5>", unsafe_allow_html=True)
    
    col_content = [
        "Total No. of Policies = 55135",
        "Total No. of Risky Policies = 1435",
        "Total No. of Claims = 48",
        "Total No. of Claims Captured = 30",
        "Percentage of Claims Captured = 62.5 %",
        "Percentage of Risky Policies captured in the top 5 % = 2.6%",
        "Percentage of Risky Annual Premuim captured in the top 5 % = 5%"
    ]

    
    col1, col2 , col3= st.columns([0.5,1.5,2.3])
    
    with col2:
        html_string = "<b style='background-color:#FAF0DC; color:#A94064; padding: 15px;padding-right: 30px; text-align: center;'>Total No. of Policies = 55135</b>"
        st.markdown("\n")
        st.markdown("\n")
        # Display the HTML with unsafe_allow_html (use with caution)
        st.markdown(html_string, unsafe_allow_html=True)
        
    with col3:
        html_string = "<b style='background-color:#FAF0DC; color:#A94064; padding: 15px;padding-right: 30px; text-align: center;'>Total No. of Claims = 48</b>"
        st.markdown("\n")
        st.markdown("\n")
        # Display the HTML with unsafe_allow_html (use with caution)
        st.markdown(html_string, unsafe_allow_html=True)

    col1, col2 , col3= st.columns([0.43,2,2.78])
    
    with col2:
        html_string = "<b style='background-color:#CDEBCD; color:#658354; padding: 15px;padding-right: 22px; text-align: center;'>Total No. of Risky Policies = 1435</b>"
        st.markdown("\n")
        st.markdown("\n")
        # Display the HTML with unsafe_allow_html (use with caution)
        st.markdown(html_string, unsafe_allow_html=True)
        
    with col3:
        html_string = "<b style='background-color:#CDEBCD; color:#658354; padding: 15px;padding-right: 20px; text-align: center;'>Total No. of Claims Captured = 30</b>"
        st.markdown("\n")
        st.markdown("\n")
        # Display the HTML with unsafe_allow_html (use with caution)
        st.markdown(html_string, unsafe_allow_html=True)
        
    col1, col2 , col3= st.columns([3.57,3.63,3.8])
        
    with col1:
        html_string = "<b style='background-color:#ADD8E6; color:#241571; padding: 13px; text-align: center;'>% Claims Captured = 62.5 %</b>"
        st.markdown("\n")
        st.markdown("\n")
        # Display the HTML with unsafe_allow_html (use with caution)
        st.markdown(html_string, unsafe_allow_html=True)
        
        
    with col2:
        html_string = "<b style='background-color:#ADD8E6; color:#241571; padding: 13px;text-align: center;'>Risk Bucket Size NOP = 2.6%</b>"
        st.markdown("\n")
        st.markdown("\n")
        # Display the HTML with unsafe_allow_html (use with caution)
        st.markdown(html_string, unsafe_allow_html=True)  
        
    with col3:
        html_string = "<b style='background-color:#ADD8E6; color:#241571; padding: 13px; text-align: center;'>Risk Bucket Size ANP = 5.09%</b>"
        st.markdown("\n")
        st.markdown("\n")
        # Display the HTML with unsafe_allow_html (use with caution)
        st.markdown(html_string, unsafe_allow_html=True) 
            
        
        
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Model Forecast Calculator</u></h5>", unsafe_allow_html=True)
    
    data = {'Policy No': ['P2378AH', 'P6689GD', 'P0089TU','P5567BU','P9545VZ'], 'Risk Probability': [0.92, 0.54, 0.12,0.62,0.84], 'Risk Bucket': ['Bucket 1', 'Bucket 29', 'Bucket 46','Bucket 33','Bucket 2'], 'Risk Category': ['High Risk', 'Moderate Risk', 'Low Risk', 'Moderate Risk','High Risk']}
    df = pd.DataFrame(data)
    
    # Options for dropdown selection
    dropdown_options = list(df['Policy No'].unique())  
    
    # Create two columns with equal width

        # Create a dropdown menu
    selected_col2_value = st.selectbox("Select Policy No:", dropdown_options)
    

     
    st.write("Policy Risk Details")
    if selected_col2_value:
      filtered_df = df[df['Policy No'] == selected_col2_value]
      st.dataframe(filtered_df, hide_index=True,use_container_width=True)
    else:
      st.write("Select a value from the dropdown to filter the table.")