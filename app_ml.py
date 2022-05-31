import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
from PIL import Image

def run_ml():
    df = pd.read_csv('data/airline.csv',encoding ='ISO-8859-1').dropna()
    st.subheader('유사한 항공사 추천')
    df1 = df.pivot_table(values = 'overall',index = 'author',columns = 'airline' ,aggfunc='mean')
    all_corr = df1.corr(min_periods=5)
    airlines = df['airline'].unique()
    airlines_name = st.selectbox('항공사 선택',airlines)
    all_corr[airlines]
    recom_airlines=all_corr[airlines_name].dropna()
    recom_airlines.columns=['correlation']
    recom_airlines = recom_airlines.sort_values(ascending=False).to_frame()
    st.dataframe(recom_airlines)