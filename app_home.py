import streamlit as st
from PIL import Image

def run_home():
    st.text('전 세계 인기 항공사에 대한 리뷰입니다.')
    
    url ='https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzAzMThfMjg3%2FMDAxNDg5ODIyMjQyMDM5.d387r5CkXRn8VtYrk24CZpYOdqDK_7WY7Ak8FX-1qwIg.QTnMwPAP8LnU6kYLqyGlKXG3P2KgG_K9l8HjxiFMtDIg.JPEG.drm1%2Ffsx_2017-03-18_16-24-41-512.jpg&type=sc960_832'

    st.image(url)
