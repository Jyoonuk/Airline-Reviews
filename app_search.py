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
    df = df[['aircraft','overall','author','customer_review','cabin']]
        
    

    
    radio_menu = ['항공사 검색','항공기 검색']
    selected = st.radio('검색할 선택하세요',radio_menu)

    if selected == radio_menu[0] :
         word = st.text_input('검색할 단어를 입력하세요, ex) korean air, Asiana Airlines')
         result = df.loc [df.index.str.lower().str.contains(word.lower()) , ]
         st.dataframe(result)

         st.subheader('비슷한 항공사 추천')

         df_mean = df.groupby('airline')['overall'].mean()
         rating_df_mean = df_mean.to_frame()
         ratings_df_count = df.groupby('airline')['overall'].count()
         ratings_df_count.to_frame()
         ratings_df_count1 = ratings_df_count.to_frame()
         ratings_df_count1.columns = ['count']
         ratings_mean_count_df = rating_df_mean.join(ratings_df_count1)
    
         df = df.pivot_table(values = 'overall',index = 'author',columns = 'airline' ,aggfunc='mean')
         ANA_corr = df.corrwith('word')
         ANA_corr = ANA_corr.to_frame()
         ANA_corr.columns = ['correlation']
         ANA_corr = ANA_corr.join(ratings_mean_count_df['count'])
         ANA_corr.dropna(inplace = True)
         ANA_corr.sort_values('correlation',ascending = False)
         ANA_corr = ANA_corr.loc[ANA_corr['count'] > 50, ] 
         ANA_corr.sort_values('correlation',ascending = False)
         st.dataframe(ANA_corr)


         
    elif selected == radio_menu[1] :
        word = st.text_input('검색할 단어를 입력하세요, ex) A330, Boeing 767')
        result1 = df.loc [df['aircraft'].str.lower().str.contains(word.lower()) , ]
        st.dataframe(result1)
    
    
    