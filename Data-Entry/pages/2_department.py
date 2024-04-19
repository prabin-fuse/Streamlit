import streamlit as st
import pandas as pd



try:
    department_data = pd.read_csv('department_data.csv')
except FileNotFoundError:
    department_data = pd.DataFrame(columns= ["Department Number", "Department Name", "Location"])


def save_data():
    department_data.to_csv('department_data.csv', index=False)


st.set_page_config(
    page_title="Department Entry",
    page_icon="",
)


st.title("Department Entry")
deptno = st.text_input("Department Number:")
dname = st.text_input("Department Name:")
loc = st.text_input("Location:")


submit_button = st.button("Submit")

if submit_button :
    if not deptno or not dname or not loc :
        st.error("Please fill all the details!")
    
    elif int(deptno) in department_data["Department Number"].values: #Duplicatea?
        st.error("Department Number already exists")

    else:
        try:
            department_data.loc[len(department_data)] = [int(deptno), dname, loc]
            st.success("Department data submitted successfully.")
            save_data()
        except ValueError:
            st.error("The date type is not matched")
        

st.dataframe(department_data, width= 8000)

#st.header(len(department_data))