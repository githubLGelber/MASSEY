import pandas as pd
import streamlit as st
import os

dir_name = os.path.abspath(os.path.dirname('TB_Burden_Country.csv'))
DATA = os.path.join(dir_name, 'TB_Burden_Country.csv')
DATA2=pd.read_csv(DATA)
st.dataframe(DATA2)

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)

#DATA3=DATA2[(DATA2['Year']==2005) & (DATA2['Region']=='EUR')]
#plt.hist(DATA3['Estimated prevalence of TB (all forms)'])






