import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# time library seems to be inbuilt so, no 
st.title('⏳ Pomodoro Timer')