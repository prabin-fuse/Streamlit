import streamlit as st
import plotly.graph_objects as go
import pandas as pd



try:
    employee_data = pd.read_csv('employee_data.csv')
except FileNotFoundError:
    employee_data = pd.DataFrame(columns= ["Employee Number", "Employee Name", "Job", "Department Number"])

try:
    department_data = pd.read_csv('department_data.csv')
except FileNotFoundError:
    department_data = pd.DataFrame(columns= ["Department Number", "Department Name", "Location"])


st.set_page_config(
    page_title="Data Entry Application",
    page_icon="",
)


st.title("Data Entry Application")
st.header("Visualization of Combining Employee and Department Data")

st.sidebar.title("Data Entry Application")

try:
    joined_data = pd.merge(employee_data, department_data, on='Department Number')
    st.dataframe(joined_data)
except:
    st.error("No data available")


# fig = go.Figure(data=[go.Table(
#     header=dict(values=list(joined_data.columns),
#                 fill_color='paleturquoise',
#                 align='left'),
#     cells=dict(values=[joined_data["Employee Number"], joined_data["Employee Name"], joined_data["Job"], joined_data["Department Number"]],
#                fill_color='lavender',
#                align='left'))
# ])

# fig.show()


