import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from openpyxl import Workbook
from openpyxl import Workbook
# st.set_page_config(page_title='Survey Results')
# st.header('Survey Results 2021')
# st.subheader('Was the tutorial helpful?')
# import os
### --- LOAD DATAFRAME
# mydir = 'C:/report/fode-reporting-web-tutorial-main/'
# excel_file = 'Results.xlsx'
# training_images_labels_path = os.path.join(mydir, excel_file)

excel_file = 'C:/report/fode-reporting-web-tutorial-main/Results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)
df_participants.dropna(inplace=True)
st.dataframe(df)
st.dataframe(df_participants)