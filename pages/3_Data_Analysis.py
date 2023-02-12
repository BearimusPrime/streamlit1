import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime

st.title("Data Analysis")
df_agg = pd.read_csv('assets/Aggregated_Metrics_By_Video.csv').iloc[1:,:]
df_agg.columns = ['Video','Video title','Video publish time','Comments added','Shares','Dislikes','Likes','Subscribers lost','Subscribers gained','RPM (USD)','CPM (USD)','Average percentage viewed (%)','Average view duration','Views','Watch time (hours)','Subscribers','Your estimated revenue (USD)','Impressions','Impressions click-through rate (%)']
df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time'])
