import streamlit as st
import pandas as pd
import numpy as np

st.title('Update forms')
option = st.selectbox(
     'Select the activity to update?',
     ('3.1-MIT', '3.1-ADA', '4.10-ADA'))

st.write('You selected:', option)

st.button('update',onClick=print("hello"))

