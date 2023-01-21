import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("Country wise Suicide Trend Over the years from 1985 to 2015 📈")

df=pd.read_csv("Sucide Data.csv")

tab1, tab2 =st.tabs(["Suicides per 100k", "Trend of each Country"])


with tab1:
        countries = df.groupby(['country'])['suicides/100k pop'].sum().reset_index(name = 'count')
        countries
        bar = alt.Chart(countries).mark_bar().encode(
        x=alt.X('country:N'),
        y=alt.Y('count:Q')
    ).interactive()
        st.altair_chart(bar, use_container_width=True)
    #bar=alt.Chart(df).mark_bar().encode(
     #   x='country:Q', y='suicides/100k pop:Q'
    #).interactive()

    #st.altair_chart(bar, use_container_width=True)

with tab2:
        st.write('Line chart by Countries')
        country = sorted(df.country.unique().tolist())
        country_selecter = st.selectbox("Country:",country)
        con = df.groupby(['country','year'])['suicides_no'].sum().reset_index(name='Suicide_count')
        df2=con[['year','Suicide_count']].loc[con['country'] == country_selecter] 
        df2
        line = alt.Chart(df2).mark_line().encode(
                   x= 'year:O',
                   y= 'Suicide_count:Q'
                )
        st.altair_chart(line, use_container_width=True)
   

    #st.line_chart(df,'year','suicides/100k pop', use_container_width=True)  

