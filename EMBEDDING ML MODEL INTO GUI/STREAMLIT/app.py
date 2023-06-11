# Import Streamlit
import streamlit as st

# import pandas
import pandas as pd

# import numpy 
import numpy as np

# import matplotlib.pyplot as plt
# import seaborn as sns

# Enter the title and sub-header of app
st.title("STORE FAVORITA SALES FORECAST")
st.subheader("Peroidic Sales Predictions")

# Enter info with streamlit form
with st.form("prediction_form") as form:
    name = st.text_input(label="Please enter you full name")
    role = st.text_input(label="Please enter your role")
    staff_id = st.number_input(label="Please enter your staff ID")
    submit = st.form_submit_button()
  

print(f"[info] My name is : {name}")






