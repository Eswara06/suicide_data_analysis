import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("Suicide Trend Over the years from 1985 to 2015 📈")

df=pd.read_csv("Sucide Data.csv")

tab1, tab2 =st.tabs(["Bar Chart", "Line Chart"])


with tab1:
    bar=alt.Chart(df).mark_bar().encode(
        x='year:O', y='suicides/100k pop:Q'
    ).interactive()

    st.altair_chart(bar, use_container_width=True)

with tab2:
    line=alt.Chart(df).mark_line().encode(
       x='year:O', 
       y='suicides_no:Q'
    ).interactive()

    st.altair_chart(line, use_container_width=True)

    #st.line_chart(df,'year','suicides/100k pop', use_container_width=True)

    

