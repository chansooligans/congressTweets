from congresstweets import twitter, locs
import glob
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Assume you load the DataFrame from a CSV file
files=glob.glob(f"{locs.DATA_LOC}/senators/*") + glob.glob(f"{locs.DATA_LOC}/representatives/*") 
tweets = twitter.tweets.TweetsTable(files=files, loc=locs.DATA_LOC)

# Function to search the DataFrame based on the user's input
def search_tweets(keyword):
    return tweets.df[
        tweets.df['text'].str.contains(keyword, case=False, na=False)
    ][['text', 'created_at', 'id', 'handle']]

# Create a text input for the user to enter a keyword
keyword = st.text_input("Enter a keyword to search for:", "health")

# When the user enters a keyword and hits Enter, update the display
if keyword:
    results = search_tweets(keyword)

    if results.empty:
        st.write("No tweets found.")
    else:
        st.dataframe(
            results, 
            width=1400, 
            height=800,
            column_config={
                "text":st.column_config.TextColumn(
                    label=None,
                    width="large"
                )
            }
        )
