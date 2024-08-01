import streamlit as st
import time

st.title('⏳ Pomodoro Timer')

curr = time.time()
curr

curr_real = time.ctime(curr)
curr_real