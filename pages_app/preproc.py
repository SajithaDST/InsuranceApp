# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:12:21 2024

@author: sajit
"""

import streamlit as st
from PIL import Image
import pandas as pd
from plotly.graph_objs import Figure, Bar, Scatter

def show_preproc():
    
   
    st.header("Data Processing Pipeline", divider='red')
    
    
    st.write(
         """
         A data processing pipeline is a systematic approach to handling the flow of data from its raw state to a usable format for analysis. It's essentially a series of steps that transform and prepare the data for its intended use.
     """)
     
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Data Flow Diagram</u></h5>", unsafe_allow_html=True)
    
    col1, col2,col3 = st.columns([1,4,1])
     
    with col2:      
            # Load the image
        image = Image.open("images/dataflow.jpg")
        st.image(image, use_column_width=True)
    
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Train Data Snapshot</u></h5>", unsafe_allow_html=True)
          
            # Load the image
    col1, col2,col3 = st.columns([1,8,1])
         
    with col2:  
        image = Image.open("images/dataset.jpg")
        st.image(image, use_column_width=True)
        
    st.markdown("\n") 
    st.markdown("\n") 
    st.markdown("\n")
    st.markdown("<h5 style='text-align: center; color: black;'>&ensp; &ensp; <u>Feature Predictive Power Asessment:</u></h5>", unsafe_allow_html=True) 
         

    df = pd.read_csv('optbinning.csv')

    dropdown_options = list(df['Tag'].unique())  
    
    col1, col2,col3 = st.columns([1,3,1])
     
    with col2:     
        selected_col2_value = st.selectbox("Select Feature:", dropdown_options)
    
   
    st.markdown("\n")
    st.markdown("\n")
    columns = ['Index','Bin','Count','Count(%)','Non-Event','Event','WoE','IV','JS']
    st.markdown("<h6 style='text-align: center; color: black;'>&ensp; &ensp; Binning Details</h6>", unsafe_allow_html=True) 
  
    if selected_col2_value:
      filtered_df = df[df['Tag'] == selected_col2_value]
      st.dataframe(filtered_df[columns], hide_index=True,use_container_width=True)
      
      col1, col2,col3 = st.columns([1,2,1])
      
      with col2:
         
          # Define traces for bar and line charts
        # Define secondary y-axis for line chart
          y_axis2 = {'overlaying': 'y', 'anchor': 'x',"side": "right"}
        
        # Define traces with separate y-axes
          bar_trace = Bar(x=filtered_df['Bin'], y=filtered_df['Count'], name='Count', yaxis='y')
          line_trace = Scatter(x=filtered_df['Bin'], y=filtered_df['WoE'], name='WoE', yaxis='y2', line=dict(color='red'))
        
        # Combine traces and customize layout
          fig = Figure(data=[bar_trace, line_trace])
          fig.update_layout(
            title='WoE Chart',
            title_x=0.45,
            xaxis_title='Bins',
            yaxis_title='Bin Count',
            yaxis2=y_axis2,  # Define secondary y-axis for line chart
            yaxis2_title='WoE'  # Set title for right y-axis
          )
        
          fig.update_xaxes(showgrid=False)
          fig.update_yaxes(showgrid=False)
        # Display the Plotly chart in Streamlit
          st.plotly_chart(fig)
    else:
      st.write("Select a value from the dropdown to filter the table.")
     
        