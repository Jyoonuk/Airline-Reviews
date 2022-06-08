import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import platform
from matplotlib import font_manager, rc
import numpy as np
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

df = pd.read_csv('data/airline.csv',encoding ='ISO-8859-1').dropna()

def run_chart():
    st.subheader('Airline Chart')
 
    st.subheader('항공사별 리뷰수')
    my_order = df['airline'].value_counts().index

    fig1 = plt.figure(figsize=(6,13))
    sns.countplot(data = df, y= 'airline',order = my_order)
    st.pyplot(fig1)


    st.subheader('점수별 리뷰수')

    fig2 = plt.figure()
    plt.hist(data= df ,  x = 'overall', rwidth=0.8, bins =10)
    plt.xlabel('점수')
    plt.ylabel('리뷰 개수')
    st.pyplot(fig2)
   


    df.pie=df['overall'].value_counts()

    fig3=plt.figure()
    plt.pie(df.pie, autopct='%.1f', labels=df.pie.index, startangle=90, wedgeprops={'width' : 0.7})
    plt.title('점수 분포 표')
    plt.legend()     
    plt.show()
    st.pyplot(fig3)


    st.text("(좌석 편안함,객실 서비스,음식 만족도,엔터테이먼트,지상 서비스,가성비")
    st.text("overall은 1~10점 , 나머지는 1~5등급")
    df2 = df[['overall','seat_comfort','cabin_service','food_bev','entertainment','ground_service','value_for_money']]
    col_list = df2.columns
    selected_list1 =st.multiselect('상관계수가 궁금한 컬럼들 선택',col_list)
    if len(selected_list1) >= 2  :

        fig1 = sns.pairplot(data = df[selected_list1])
        st.pyplot(fig1)

        st.text('선택하신 컬럼끼리의 상관계수 입니다.')
        st.dataframe(df[selected_list1].corr())

        
        fig2 = plt.figure()
        sns.heatmap(data = df[selected_list1].corr(), annot =True, fmt = '.2f', vmin =-1 , vmax = 1, cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig2)
