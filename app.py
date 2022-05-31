import streamlit as st
import numpy as np
from app_home import run_home
from app_search import run_search
from app_data import run_data
from app_chart import run_chart
from app_ml import run_ml

def message_cleaning(sentence) :
  # 1. 구두점 제거
  Test_punc_removed = [char for char in sentence if char not in string.punctuation ]
  # 2. 각 글자들을 하나의 문자열로 합친다.
  Test_punc_removed_join = ''.join(Test_punc_removed)
  # 3. 문자열에 불용어가 포함되어있는지 확인해서, 불용어 제거한다.
  Test_punc_removed_join_clean = [word for word in Test_punc_removed_join.split() if word.lower() not in my_stopwords ]
  # 4. 결과로 남은 단어들만 리턴한다.
  return Test_punc_removed_join_clean


def main () :


    menu = ['Home','Search','Data','Chart','recommend']
    choice = st.sidebar.selectbox('MENU',menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] : 
        run_search()   
    elif choice == menu[2] :
        run_data()
    elif choice == menu[3] :
        run_chart()
    elif choice == menu[4] :
        run_ml()


if __name__ == '__main__' : 
    main()