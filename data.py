import streamlit as st
import pandas as pd
import numpy as np
import time



data = pd.read_csv("data//Salary_Data.csv")

st.dataframe(data,width=500,height= 500)

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))