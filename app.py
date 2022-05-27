from turtle import home
import streamlit as st
import numpy as np
from app_home import run_home
from app_search import run_search
from app_data import run_data
from app_chart import run_chart


def main () :
    st.title('Airline reviews for most popular airlines.')

    menu = ['Home','Search','Data','Chart']
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] : 
        run_search()   
    elif choice == menu[2] :
        run_data()
    elif choice == menu[3] :
        run_chart()


if __name__ == '__main__' : 
    main()