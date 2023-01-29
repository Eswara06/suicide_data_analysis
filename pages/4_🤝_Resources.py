import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
import altair as alt
import numpy as np
import streamlit as st
from PIL import Image

image = Image.open('Images/suicideprevention.jpg')

st.image(image)

st.header("Suicide Prevention Resources")

#st.set_page_config(page_title="Home", page_icon="🏰")

st.markdown('''
This wikipedia page lists suicide crisis lines by country:
https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines

* [Crisis text line](https://www.crisistextline.org): Text HOME to 741741
* [Lifeline web chat](https://suicidepreventionlifeline.org/chat/)

*North Carolina Suicide Prevention Helpline: https://www.sprc.org/states/north-carolina

*Find Help here: https://988lifeline.org/ ''' )
