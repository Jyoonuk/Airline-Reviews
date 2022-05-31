import streamlit as st
import pandas as pd 


def run_data():


    df = pd.read_csv('data/airline.csv',encoding ='ISO-8859-1').dropna()
    df = df.set_index('airline')
    df = df[['aircraft','overall','author','cabin','customer_review']]
    df_mean = df.groupby('airline')['overall'].mean()
    df1 = pd.read_csv('data/airline.csv',encoding ='ISO-8859-1').dropna()
    rating_df_mean = df_mean.to_frame()         
    ratings_df_count = df.groupby('airline')['overall'].count()
    ratings_df_count.to_frame()
    ratings_df_count1 = ratings_df_count.to_frame()
    ratings_df_count1.columns = ['count']
    ratings_mean_count_df = rating_df_mean.join(ratings_df_count1)
    max_rating = ratings_mean_count_df.sort_values('overall',ascending= False).head(10)
    min_rating = ratings_mean_count_df.sort_values('overall',ascending= True).head(10)
    langth_rating = ratings_mean_count_df.sort_values('count',ascending= False).head(10)

    st.subheader('최고 평점을 받은 항공사')
    
    url1 = 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fimgproc.airliners.net%2Fphotos%2Fairliners%2F5%2F1%2F2%2F6448215.jpg%3Fv%3Dv482e83923a4&type=sc960_832'

    st.image(url1)
    st.text('평점이 가장 높은 10개의 항공사')
    st.dataframe(max_rating)
    if st.checkbox('평점이 가장 높은 항공사 데이터 보기') :
        st.dataframe(df1.loc[df1['airline'] == 'Aegean Airlines',])
    

    st.subheader('가장 많은 리뷰가 있는 항공사')

    url2 = 'https://search.pstatic.net/sunny/?src=http%3A%2F%2Fimgproc.airliners.net%2Fphotos%2Fairliners%2F3%2F2%2F3%2F2596323.jpg%3Fv%3Dv40&type=sc960_832'
    st.image(url2)
    st.text('리뷰가 가장 많은 10개의 항공사')
    st.dataframe(langth_rating)
    if st.checkbox('리뷰가 가장 많은 항공사 데이터 보기') :
        st.dataframe(df1.loc[df1['airline'] == 'Cathay Pacific Airways',])

    
    
    st.subheader('최저 평점을 받은 항공사')
    
    url1 = 'https://search.pstatic.net/sunny/?src=http%3A%2F%2Fimgproc.airliners.net%2Fphotos%2Fairliners%2F8%2F7%2F9%2F1368978.jpg%3Fv%3Dv40&type=sc960_832'

    st.image(url1)
    st.text('평점이 가장 낮은 10개의 항공사')
    st.dataframe(min_rating)
    if st.checkbox('평점이 가장 낮은 항공사 데이터 보기') :
        st.dataframe(df1.loc[df1['airline'] == 'Frontier Airlines',])


    st.subheader('항공사의 리뷰개수, 통계')
    st.dataframe(df.groupby('airline')['overall'].describe())


    col_list = df1.columns

    selected_list =st.multiselect('데이터를 보고싶은 컬럼들 선택',col_list)
    if len(selected_list) >= 1  :
        
        st.dataframe(df1[selected_list])