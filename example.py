import pandas as pd
import streamlit as st

DATA=pd.read_csv("../64226/TB_Burden_Country.csv")
st.dataframe(DATA)

st.title('My First Streamlit App')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)