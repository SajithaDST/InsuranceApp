# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st


def show_data():
    st.header("Important Data Features", divider='red')
    
    
    st.write(
         """
         Some of the features included in model creation include:
         """)
     

        # Define column headers (replace with your desired titles)
    col1_header = "Numeric Features"
    col2_header = "Categorical Features"
    
    # Define content as lists (replace with your actual content)
    col1_content = [
        "Age",
        "Annual Income",
        "Premium Amount",
        "Premium Frequency"
    ]
    
    col2_content = [
        "Occupation",
        "Affluence Score",
        "Gender",
        "Policy Type"
    ]
    
    # Create two columns with equal width
    col1, col2 = st.columns(2)
    
    
    # Display content as bullet points
    with col1:
        st.subheader("**" + col1_header + "**")  # Display header as bold markdown
        for item in col1_content:
            st.markdown(f"- {item}")  # Use f-string for dynamic formatting
    
    with col2:
        st.subheader("**" + col2_header + "**")
        for item in col2_content:
            st.markdown(f"- {item}")
     
    st.markdown("\n\n")
    st.write(
         """
         In addition, some features are generated manually, like SA - Premium Ratio, Agent - Claim Ratio, Salary Bands, Hazardous Occupation, Agent Employment Tenure etc.
         """)