import streamlit as st
import pandas as pd
import numpy as np

# Data Visualization:
st.title("Bar Chart")

data = pd.DataFrame(np.random.randn(50,2), columns=["x", "y"])

st.bar_chart(data)

st.title("Line chart")
st.line_chart(data)

st.title("Area chart")
st.area_chart(data)