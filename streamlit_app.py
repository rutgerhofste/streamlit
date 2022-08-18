import streamlit as st
import pandas as pd
import numpy as np
import os
from pyairtable import Table

airtable_api = os.environ["AIRTABLE_API"]
BASE_ID ="ZkqEUVtVZFZB9K"
TABLE_NAME = "test"



st.title('Update forms')
option = st.selectbox(
     'Select the activity to update?',
     ('3.1-MIT', '3.1-ADA', '4.10-ADA'))

st.write('You selected:', option)

st.button('update')




#table = Table(airtable_api , BASE_ID , TABLE_NAME)

#foo = table.all()

