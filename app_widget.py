import streamlit as st
import time

# Widgets:

# Checkbox:
st.checkbox("Attend")

# Button
st.button("Click here")

# Radio
st.radio("Pick your Gender", ["Male", "Female", "Other"])

# Select box:
st.selectbox("Select courses", ["Machine Learning", "DSA", "Cyber Security"])

# Multi select:
st.multiselect("Select department", ["AI","Sales","Finance"])

#select slide:
st.select_slider("Rating", ["Good", "Bad", "Worst"])

# Slider:
st.slider("Select number", 0,90)

# Number input
st.number_input("Enter the number", 0,100)

# Text Input:
st.text_input("Enter you name")

#Date Input:
st.date_input("Enter the date")

#Time Input:
st.time_input("Whats the time?")

# Textarea:
st.text_area("Enter in this text area")

# file upload:
st.file_uploader("Upload the file")

# Color picker:
st.color_picker("Choose the color")

#Progess bar:
st.progress(90)

#Spinner:
# with st.spinner("Just wait"):
#     time.sleep(2)

# Ballons:
st.balloons()

# Sidebar:
st.sidebar.title("Organization")
st.sidebar.text_input("Enter your org name")
st.sidebar.text_input("Enter Your role")
st.sidebar.button("Submit")