import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
import altair as alt
import numpy as np


st.header("Suicide Data Analysis from 1985 to 2015")

#st.set_page_config(page_title="Home", page_icon="🏰")

st.markdown('''Welcome! This dashboard was created to provide an overview on 
            the suicide rate world wide based on various factors like Gender, Age group, Generation, 
            and Country.   
             **Goal:**
                It is our hope that suicide survilience will provide important data 
                to understand and develop strategies to reduce world wide suicides. 
                Through collaborative efforts, it is our mission to take action 
                against suicidal acts in our communities. ''' )
st.markdown("**Here is the dataset we used to perform analysis:**")

df= pd.read_csv("Sucide Data.csv")

df= df.drop(columns=['HDI for year'])
df

