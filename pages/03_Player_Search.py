import streamlit as st
import pandas as pd

df = st.session_state['df']

def validate(df, col, string):
  if df.loc[df[col].str.contains(string, na=False)].empty:
    return False
  else:
    return True

st.subheader("Then, search for a player")
st.write("""
Here you're able to enter any name, even a partial one, to get a list
showing their information. Don't forget to press Enter when you're ready to
run your search.
""")

with st.sidebar:
  st.subheader("First, let's choose your columns")
  st.write("Here you're able to select which columns appear in the search results to the right.")
  checkboxes = {
    'name': st.checkbox('Name', value=True),
    'team': st.checkbox('Team', value=True),
    'role': st.checkbox('Role', value=True),
    'position': st.checkbox('Position', value=True),
    'age': st.checkbox('Age', value=False),
    'college': st.checkbox('College', value=False),
    'profile_url': st.checkbox('Profile URL', value=False)
  }

col1, col2 = st.columns(2)
search_by = col2.radio('Search by', options=['name', 'team', 'position'], horizontal=True)
input = col1.text_input("Enter your search here")

if validate(df, search_by, input):
  selected_options = []
  for key, value in checkboxes.items():
    if value:
      selected_options.append(key)
  
  st.dataframe(df[df[search_by].str.contains(input, na=False)][selected_options], use_container_width=True)
else:
  st.info('Sorry, there is no {} that contains "{}"'.format(search_by, input))