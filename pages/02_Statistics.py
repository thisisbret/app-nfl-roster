import streamlit as st
import pandas as pd
import plotly.express as px

df = st.session_state['df']

st.subheader("Let's explore some basic statistics")

st.write("We don't have much to work with in this dataset, however we can derive some metrics.s")

position = st.selectbox('First we choose a position', df.position.unique().tolist(), index=0)

col1, col2 = st.columns(2)

mean_by_position = df.groupby('position').mean()[['height_in_inches', 'weight_in_lbs']].reset_index()
avg_height = mean_by_position[mean_by_position.position == position]['height_in_inches'].values[0].round(2)
avg_weight = mean_by_position[mean_by_position.position == position]['weight_in_lbs'].values[0].round(2)
col1.metric('Avg. Height in Inches', avg_height)
col2.metric('Avg. Weight in Pounds', avg_weight)

team = st.selectbox("Then we select a team", df.team.unique().tolist(), index=0)

mean_by_team = df.groupby('team').mean()[['experience']].reset_index()
avg_experience = mean_by_team[mean_by_team.team == team]['experience'].values[0].round(2)
st.metric('Avg. Player Experience of Team', avg_experience)

#fig = px.histogram(mean_by_team, x='team', y='experience')
#fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
#fig.update_layout(yaxis_title='avg experience')
#st.plotly_chart(fig)