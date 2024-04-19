import streamlit as st
import pandas as pd



try:
    employee_data = pd.read_csv('employee_data.csv')
except FileNotFoundError:
    employee_data = pd.DataFrame(columns= ["Employee Number", "Employee Name", "Job", "Department Number"])


def save_data():
    employee_data.to_csv('employee_data.csv', index=False)


st.set_page_config(
    page_title="Data Entry Application",
    page_icon="",
)


st.title("Employee Data Entry")
empno = st.text_input("Employee Number:")
ename = st.text_input("Employee Name:")
job = st.text_input("Job:")
deptno = st.text_input("Department Number:")

submit_button = st.button("Submit")

if submit_button :
    #print(employee_data["Employee Number"].values)
    if not empno or not ename or not job or not deptno:
        st.error("Please fill all the details!")
   
    elif int(empno) in employee_data["Employee Number"].values: #Duplicatea?
        st.error("Employee Number already exists")
    
    else:
        try:
            employee_data.loc[len(employee_data)] = [int(empno), ename, job, int(deptno)]
            st.success("Employee data submitted successfully.")
            save_data()
        except ValueError:
            st.error("The date type is not matched")
        

st.dataframe(employee_data, width = 800)

#st.header(len(employee_data))