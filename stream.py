import pandas as pd
import streamlit as st
import os
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn import preprocessing

def clickedb():
    st.session_state.count=1
    
def clickedb2():
    st.session_state.count=2
    
def clickedb3():
    st.session_state.count=3

dir_name = os.path.abspath(os.path.dirname('TB_Burden_Country.csv'))
DATA = os.path.join(dir_name, 'TB_Burden_Country.csv')
DATA2=pd.read_csv(DATA)
st.title("The Tuberculosis Dataset")
st.dataframe(DATA2)
st.subheader("Simulating Features using Year and Region Values")
user_input = st.slider("Enter Year",1990,2013)
st.write("Key: EMR: Eastern Mediterranean Region, EUR: Europe, AFR: Africa, WPR: West Pacific Region, AMR: America, SEA: South East Asia")
user_input2=st.selectbox("Enter Region",('EMR','EUR','AFR','WPR','AMR','SEA'))
user_input3=st.selectbox("Enter Feature",(DATA2.columns[7],DATA2.columns[27],DATA2.columns[37],DATA2.columns[14],DATA2.columns[20]))
                       


if 'count' not in st.session_state:
    st.session_state.count =0
st.button('Click me',on_click=clickedb)

if st.session_state.count==1:
    fig, ax = plt.subplots()
    if ((user_input!='') & (user_input2!='')):
        DATA3=DATA2[(DATA2['Year']==int(user_input)) & (DATA2['Region']==user_input2)]
    elif ((user_input!='') & (user_input2=='')):
        DATA3=DATA2[(DATA2['Year']==int(user_input))]
    elif ((user_input=='') & (user_input2!='')):
        DATA3=DATA2[(DATA2['Region']==user_input2)]
    ax.set_ylabel('Count')
    ax.set_xlabel(user_input3)
    DATA3.replace('', np.nan, inplace=True)
    DATA3x=DATA3.dropna(subset=[user_input3])
    ax.hist(DATA3x.loc[:,user_input3], bins=30)
    st.pyplot(fig)

st.markdown("""---""")
st.subheader("Simulating Features for a particular Country")
user_input4=st.text_input("Enter Country")
user_input5=st.selectbox("Enter Feature2",(DATA2.columns[7],DATA2.columns[27],DATA2.columns[37],DATA2.columns[14],DATA2.columns[20]))
st.button('Click me2',on_click=clickedb2)

if st.session_state.count==2:
    DATA4=DATA2[DATA2['Country or territory name']==user_input4]
    DATA4.replace('', np.nan, inplace=True)
    DATA4x=DATA4.dropna(subset=[user_input5])
    MEAN=(pd.DataFrame(DATA4x.loc[:,user_input5]).apply(np.mean, axis=0)).iloc[0]
    SD=(pd.DataFrame(DATA4x.loc[:,user_input5]).apply(np.std, axis=0)).iloc[0]
    VAR=(pd.DataFrame(DATA4x.loc[:,user_input5]).apply(np.var, axis=0)).iloc[0]
    st.write('Mean of feature=', MEAN)
    st.write('Standard Deviation of feature=', SD)
    st.write('Variance of feature=',VAR)
    st.line_chart(DATA4x,x='Year',y=user_input5)

st.markdown("""---""")
st.subheader("Feature Scatter Plots for a Particular Year (for all countries in dataset)")
user_input6=st.selectbox("Enter Feature on x axis",\
                         (DATA2.columns[7],DATA2.columns[27],DATA2.columns[37],DATA2.columns[14],DATA2.columns[20]))
user_input7=st.selectbox("Enter Feature on y axis",\
                         (DATA2.columns[7],DATA2.columns[27],DATA2.columns[37],DATA2.columns[14],DATA2.columns[20]))
user_input8=st.slider("Enter Year2",1990,2013)

st.button('Click me3',on_click=clickedb3)
if st.session_state.count==3:
    DATA5=DATA2[DATA2['Year']==int(user_input8)]
    DATA5.replace('', np.nan,inplace=True)
    DATA5x=DATA5.dropna(subset=[user_input6,user_input7])
    std_scale=preprocessing.StandardScaler().fit(DATA5x[[user_input6,user_input7]])
    std_scale2=std_scale.transform(DATA5x[[user_input6, user_input7]])
    std_scale3=pd.DataFrame(std_scale2)
    std_scale3.rename(columns = {0:user_input6,1:user_input7}, inplace = True)
    st.write("Standardized Data")
    st.scatter_chart(std_scale3,x=user_input6,y=user_input7)
    st.write("Raw Data")
    st.scatter_chart(DATA5x,x=user_input6,y=user_input7)
st.markdown("""-""")

    
      
    
    

    
    
    
    
