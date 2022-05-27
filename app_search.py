import streamlit as st
import pandas as pd
import os
import openpyxl

def run_search():

    df = pd.read_excel('data/airline.xlsx').dropna()

    radio_menu = ['항공사 검색','항공기 검색']
    selected = st.radio('검색할 선택하세요',radio_menu)

    if selected == radio_menu[0] :
         word = st.text_input('검색할 단어를 입력하세요')
         df.loc [df['airline'].str.lower().str.contains(word.lower()) , ]
    elif selected == radio_menu[1] :
        st.dataframe(df)
