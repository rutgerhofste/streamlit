import streamlit as st
import pandas as pd
import numpy as np

st.title('Update forms')
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

