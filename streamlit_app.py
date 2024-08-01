import streamlit as st
import datetime
import time
# time library seems to be inbuilt so, no need to intall dependencies
st.title('⏳ Pomodoro Timer')

t = st.time_input("Select a time", datetime.time(0, 1))

st.write("Time is set to", t)