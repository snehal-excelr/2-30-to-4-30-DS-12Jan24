# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 15:20:00 2023

@author: excel
"""

import streamlit as st

name = st.text_input("Enter your name","")

# st.markdown(f"How are you: {name}?")

job = st.text_area("What do you do?")

age = st.number_input("Enter a number value",min_value=0, max_value=80)

# st.markdown(f"How are you: {text_input}?")

if name!="":
    st.markdown(
                f"""
                * Name : {name}
                * JOb : {job}
                * Age : {age}
                """
                )
is_available_for_work = st.checkbox("Available for work")

st.write(is_available_for_work)
threshold = st.slider("Pick a threshold",min_value=1.0,max_value=100.0,value=50.0,step=0.5)
# threshold = st.slider("Pick a threshold",min_value=1,max_value=100,value=50,step=2)
st.write(threshold)


