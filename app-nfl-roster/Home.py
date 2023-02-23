import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    return pd.read_parquet('./assets/datasets/nfl-roster-2022-season.parquet')

if 'df' not in st.session_state:
    st.session_state['df'] = get_data()

with st.container():
    st.header('NFL Roster of the 2022 Season')

    st.write("""
    This dataset includes the NFL rosters of all teams from the 2022 season.
    There are 12 columns spanning 2483 rows. This data was scraped from ESPN.com on February 18th, 2023
    following the conclusion of the Super Bowl.

    I've included this data as both a CSV and Parquet file. It's recommended to download the parquet
    file due to the significant reduction in file size and the added benefit of being able to load a
    subset of the columns into memory, rather than all 12 at once. This filetype also
    preserves the type conversions that I've performed in pandas, which alone cut the memory usage
    from 233KB's to 80.7KB's. Please keep in mind though that you'll require Apache Arrow support to be able
    to read in the parquet filetype (conda/pip install pyarrow for support in Python).
    """)

    total_players = int(st.session_state.df.name.count())
    total_teams = st.session_state.df.team.nunique()
    avg_players_per_team = st.session_state.df.groupby('team').count().name.mean().round(1)

    col1, col2, col3 = st.columns(3)

    col1.metric('Total Players', total_players)
    col2.metric('Total Teams', total_teams)
    col3.metric('Avg. Players per Team', avg_players_per_team)

    st.subheader("View the raw data")

    expander = st.expander('Expand this view to explore the dataset', expanded=True)
    expander.dataframe(st.session_state.df)

    with st.sidebar:
        st.write("""
        As you explore other pages this is where you're able to select certain
        options to modify what information is shown in the charts
        """)