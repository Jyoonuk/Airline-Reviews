import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import platform
import numpy as np

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

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
