from operator import index
import streamlit as st
import pandas as pd
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')



def run_search():

    df = pd.read_csv('data/airline.csv',encoding ='ISO-8859-1').dropna()
    df = df.set_index('airline')
    df = df[['aircraft','overall','author','cabin','customer_review']]




    radio_menu = ['항공사 검색','항공기 검색']
    selected = st.radio('검색할 선택하세요',radio_menu)

    if selected == radio_menu[0] :
         word = st.text_input('검색할 단어를 입력하세요, ex) korean air, Asiana Airlines')
         result = df.loc [df.index.str.lower().str.contains(word.lower()) , ]
         st.dataframe(result)

 
    elif selected == radio_menu[1] :
        word = st.text_input('검색할 단어를 입력하세요, ex) A330, Boeing 767')
        result1 = df.loc [df['aircraft'].str.lower().str.contains(word.lower()) , ]
        st.dataframe(result1)
    
    
    