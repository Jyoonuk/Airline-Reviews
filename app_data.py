import streamlit as st
import pandas as pd 


def run_data():


    df = pd.read_csv('data/airline.csv',encoding ='ISO-8859-1').dropna()
    df = df.set_index('airline')
    df = df[['aircraft','overall','author','customer_review','cabin']]
    df_mean = df.groupby('airline')['overall'].mean()
    rating_df_mean = df_mean.to_frame()         
    ratings_df_count = df.groupby('airline')['overall'].count()
    ratings_df_count.to_frame()
    ratings_df_count1 = ratings_df_count.to_frame()
    ratings_df_count1.columns = ['count']
    ratings_mean_count_df = rating_df_mean.join(ratings_df_count1)
    max_rating = ratings_mean_count_df.sort_values('overall',ascending= False).head(10)
    langth_rating = ratings_mean_count_df.sort_values('count',ascending= False).head(10)

    st.subheader('최고 평점을 받은 항공사')
    
    url1 = 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fimgproc.airliners.net%2Fphotos%2Fairliners%2F5%2F1%2F2%2F6448215.jpg%3Fv%3Dv482e83923a4&type=sc960_832'

    st.image(url1)
    st.text('평점이 가장 높은 10개의 항공사')
    st.dataframe(max_rating)
    

    st.subheader('가장 많은 리뷰가 있는 항공사')

    url2 = 'https://search.pstatic.net/sunny/?src=http%3A%2F%2Fimgproc.airliners.net%2Fphotos%2Fairliners%2F3%2F2%2F3%2F2596323.jpg%3Fv%3Dv40&type=sc960_832'
    st.image(url2)
    st.text('리뷰가 가장 많은 10개의 항공사')
    st.dataframe(langth_rating)
