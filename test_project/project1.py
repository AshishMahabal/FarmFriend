import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.title("Farm Friend - Indian Produce (2011-2018")
st.subheader("An aid to data driven farming")

"Data from http://mospi.nic.in/download-reports. "\
"Make selections from the sidebar to view."

cereals = ['cereals', 'paddy', 'wheat', 'jowar', 'bajra', 'barley', 'maize',
       'ragi', 'small millets', 'other cereals', 'pulses', 'gram',
       'arhar', 'urd', 'moong', 'masoor', 'horse gram', 'moth', 'val',
       'rajma', 'cowpea', 'chola', 'lakh/khesri', 'peas/chawali', 'batna',
       'other pulses'] 

#producetypes = []

#@st.cache
df = pd.read_csv("GOV_NAS2020.csv")
colnames = df.columns.tolist()
varnames = df.item.unique().tolist()
regions = df['State/ UT'].unique().tolist()
years = df.columns[3:10]

# if st.sidebar.checkbox('Column names'):
# 	'Available columns are: ',colnames
	
if st.sidebar.checkbox('Produce list'):
    'Available produce are: ',varnames

if st.sidebar.checkbox('Regions'):
    'Available regions are: ',regions

# if st.sidebar.checkbox('Show years'):
#     'Available years are: ',colnames[3:11]

region = st.sidebar.selectbox(
    'Select by Region',
    regions)

produce = st.sidebar.selectbox(
    'Select by Produce',
    varnames)

year = st.sidebar.selectbox(
    'Select by Year',
    years)

# producetype = st.sidebar.selectbox(
# 	'Select by Produce type',
#     producetypes)

if st.sidebar.checkbox('Show Region-Produce plot'):
	"Barchart for Region: ", region, " Item: ", produce
	thisdata = df[(df['State/ UT']==region) & (df['item']==produce)].iloc[:,3:10]
	thisdata
	st.bar_chart(thisdata.T)

if st.sidebar.checkbox('Show Produce plot for regions'):
	"Barchart for Region: ", region, " Year: ", year
	thisdata = df[(df['State/ UT']==region) & (df['item'].isin(cereals))][['item',year]]	
	st.altair_chart(alt.Chart(thisdata).mark_bar().encode(x='item',y=year))
	thisdata

#df[(df['State/ UT']==region) & (df['item'].isin(cereals))][['item',year]]

# if st.checkbox('Show top topics'):
# 	fig, ax = plt.subplots()
# 	lamalarts['Topic'].value_counts()[:10].plot.bar()
# 	st.pyplot(fig)

# author = st.sidebar.selectbox(
#     'Select by Author',
#      lamalarts['Author'].unique())

# 'You selected Author:',author 
# lamalarts[lamalarts['Author']==author][['Topic','Title','Host']]

# topic = st.sidebar.selectbox(
#     'Select by Topic',
#      lamalarts['Topic'].unique())

# 'You selected Topic:', topic, '(Host: ', lamalarts[lamalarts['Topic']==topic]['Host'].iloc[0],')'
# lamalarts[lamalarts['Topic']==topic][['Author','Title','Host']]

