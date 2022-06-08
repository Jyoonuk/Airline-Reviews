import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import cv2
from st_aggrid import AgGrid
import plotly.express as px
import io 
from app_home import run_home
from app_search import run_search
from app_data import run_data
from app_chart import run_chart
from app_ml import run_ml




def main () :


    menu = ['Home','Search','Data','Chart','recommend']
    
    with st.sidebar:
        url1 = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxODAxMDdfMTYw%2FMDAxNTE1MzM3MTM0NTQ4.Hdkww5vIE5h_mkKreEMdmb1zlPRnSfKp0jD_6fgRm-Ug.FXGePotff90kQGSnEQ3EVrOBZsrSk-7zrdQJMgFMPkYg.JPEG%2FIKi10gHmf5S6iK9S-verhxL5Jbh0.jpg&type=sc960_832'
        st.image(url1)
        choice = option_menu('MENU',menu)
        

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