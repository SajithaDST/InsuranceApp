import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

from pages_app.introduction import show_home
from pages_app.data_acq import show_data
from pages_app.preproc import show_preproc
from pages_app.model import show_model
from pages_app.output import show_output

st.set_page_config(initial_sidebar_state="collapsed")

        
pages = ["Introduction", "Data Acquisition", "Pre Processing", "Modelling", "Output"]

styles = {
    "nav": {
       "background-color": "rgb(2,106,129)",
    },
   "div": {
        "max-width": "40rem",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
       "background-color": "rgba(179,205,224)",
       "color": "black",
    },

    "hover": {
        "background-color": "rgba(179,205,224)",
         "color": "black",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    styles=styles,
    options=options
)

functions = {
    "Introduction": show_home,
    "Data Acquisition":show_data,
    "Pre Processing":show_preproc,
    "Modelling":show_model,
    "Output":show_output,
}
go_to = functions.get(page)
if go_to:
    go_to()