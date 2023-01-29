import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt
import squarify
import plotly.express as px

df= pd.read_csv("Sucide Data.csv")

st.header("Worldwide Suicide Data Analysis")

tab1, tab2, tab3= st.tabs(["Trend", "Gender", "Age"])

with tab1:
    bar=alt.Chart(df).mark_point().encode(
        x='year:O', y='suicides/100k pop:Q', color='sex'
    ).interactive()

    st.altair_chart(bar, use_container_width=True)
with tab2:
        st.title("Pie chart of Suicides based on Gender")
        #pie1=df[['sex','suicides/100k pop']]
        #a=pie1.groupby(['sex']).mean()
        pie_chart= df.groupby(["sex"])['suicides/100k pop'].mean().reset_index(name = 'mean')
        pie_chart
        #pie = alt.Chart(pie_chart).mark_arc(outerRadius=120).encode(
        #theta = alt.Theta("sex:N"), 
        #color=alt.Color("mean:Q")
    #)
        #pie
        #a=pd.DataFrame(pie_chart).to_numpy()
        y = np.array(pie_chart['mean'])

        labels = np.array(pie_chart['sex'])
        sizes = [5.39, 20.23]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(y, explode=explode, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)

with tab3:
        st.write("Top 10 Countries by Suicide_count")
        #year= sorted(df.year.unique().tolist())
        #country_unique= sorted(df.country.unique().tolist())
        
        #year_selecter = st.selectbox("Select Year:",year)
        


        #con = df.groupby(['country','year'])['suicides_no'].sum().reset_index(name='Suicide_count')
        #sorted_con=(con.sort_values(by=['Suicide_count'], ascending=False)).head(n=10)
        #sorted_con

        ##df2=sorted_con[['country','Suicide_count','year']].loc[sorted_con['year'] == year_selecter] 
        #f2

        #char=alt.Chart(df2).mark_line(point=True).encode(
        #x='country:N',
        #='Suicide_count:O',
        #color='age:N',
        #strokeDash='age:N')

        #st.altair_chart(char, use_container_width=True)

       



        #fig = px.treemap(con)
        #fig.update_traces(root_color="lightgrey")
        #fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        #fig.show()


        #fig= ex.treemap(con)
        #color_list = ['#0f7216', '#b2790c', '#ffe9a3',
         #           '#f9d4d4', '#d35158', '#ea3033']

        #plt.rc('font', size=14)
        #squarify.plot(sizes=suicides_no, label=labels,
         #           color=color_list, alpha=0.7)
        #plt.axis('off')
        #st.pyplot()

        #import streamlit as st
        #import matplotlib.pyplot as plt
        #import squarify

        #volume = [350, 220, 170, 150, 50]
        #labels = ['Liquid\n volume: 350k', 'Savoury\n volume: 220k',
         #       'Sugar\n volume: 170k', 'Frozen\n volume: 150k',
          #      'Non-food\n volume: 50k']
        #color_list = ['#0f7216', '#b2790c', '#ffe9a3',
         #           '#f9d4d4', '#d35158', '#ea3033']

        #plt.rc('font', size=14)
        ##        alpha=0.7)
        #plt.axis('off')
        #st.pyplot()
       
        year = sorted(df.year.unique().tolist())
        year_selecter = st.selectbox("Country:",year)
        con = df.groupby(['country','year'])['suicides_no'].sum().reset_index(name='Suicide_count')
        
        
        df2=con[['country','Suicide_count']].loc[con['year'] == year_selecter].sort_values(by=['Suicide_count'], ascending=False) 
        a=df2.head(n=10)
        a

        fig = px.treemap(a,
                 path=['country'],
                 values='Suicide_count')
        fig.update_layout(title="Top 10 countries by suicide count")
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        fig.show()
       

