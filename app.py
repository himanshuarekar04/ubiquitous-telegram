import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')
Upload_file = st.file_uploader('upload a file containing earthquake data')
if Upload_file is not None:
    df = pd.read_csv(Upload_file)
st.header('Statistic of dataframe')
st.write(df.describe())
st.header('Header of dataframe')
st.write(df.head())
fig, ax= plt.subplots(1,1)
ax.scatter(x=df['Depth'], y=df['Magnitude'])
ax.set_xlabel('Depth')
ax.set_ylabel('Magnitude')
st.pyplot(fig)