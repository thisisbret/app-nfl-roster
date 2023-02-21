import pandas as pd
import streamlit as st
import plotly.express as px

df = st.session_state['df']

st.subheader("Let's start with a simple chart")
st.write("""
This is a histogram, your choice is tracked along the x axis
with the counts of each item along the y axis. It simply tracks the frequency
of each item within the dataset.
""")

options = {
  'Position': 'position',
  'Age': 'age',
  'Height in Inches': 'height_in_inches',
  'Weight in Pounds': 'weight_in_lbs'
}

sidebar = st.sidebar

choice = sidebar.selectbox("Select a frequency to view", options.keys(), index=1)

fig = px.histogram(df, x=options[choice], title='Frequency of {}'.format(choice))
if choice == 'Position':
  fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)

st.subheader("Then discover something interesting...")
st.write("""
Here's a breakdown of the number of players that attended each colleges. Keep in mind
that None was substituted in where no college was provided. There clearly appears to be
certain colleges that provide the majority of players in the NFL. If you're interested in
being drafted, you'll likely have better odds by attending one of these schools.
  """)

number = sidebar.number_input('Number of colleges to display', min_value=1, max_value=df.college.nunique(), value=10)
result = df.groupby('college').count().name.sort_values(ascending=True).tail(number)
colleges = result.index.tolist()
count = result.values.tolist()
fig = px.histogram(x=count, y=colleges, title='Top {} Colleges by Players Attended'.format(number))
fig.update_layout(xaxis_title='count', yaxis_title='college')
st.plotly_chart(fig)