"""here, you'll create exploratory visualizations of your data and then display them with streamlit."""

import streamlit as st
import pandas as pd
import altair as alt
import joblib
import sklearn
import re

# we're unpickling our pickles here so that we don't unpickle every time the page is loaded.
# we'll want to use our vectorizer here so our exploratory visualizations can be a little more interesting.

process_pipe = joblib.load('pickles/process_pipe')
feature_list = joblib.load('pickles/feature_list')

# same story with my helper function for cleaning my tweets
def clean_text(text): 
    """Clean our tweets using regex. Remove weird characters and links."""
    cleanedup = text.lower()
    return re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", cleanedup)


def exploration_page():
    """generates the exploration page for the streamlit app."""

    st.title('exploration')

    st.write("""here, you might display some exploratory visualizations of your data to familiarize 
                your user with it.""")

    st.write("let's start by letting our user see exactly what our data looks like.")

    # load in your data, precisely as you'd expect.
    tweets = pd.read_csv('https://raw.githubusercontent.com/crsanderford/Animal-Spirits/master/btc-data/data/btc_tweets_daily_example.csv', chunksize=1000)
    tweets = next(tweets)

    st.write("st.write() can do a lot more than you'd think.")
    # This'll display the dataframe as a table.
    st.write(tweets)

    st.write("there's the data we'll be working with.")
    st.write("let's put it through our processing pipeline, and then display it again.")

    X = tweets['tweet'].apply(clean_text)
    y = tweets['sent_score']

    X_processed = process_pipe.transform(X)

    X_vectorized = pd.DataFrame(X_processed.toarray(), columns=feature_list)

    # if we ask streamlit to render all 5000 rows, things will get ugly.
    # let's show only the first fifty.

    df_to_show = X_vectorized.iloc[:,:50]
    st.write(df_to_show)

    st.write("alright, that's cool. let's get a density plot of the actual sentiment values.")

    density_chart = alt.Chart(tweets).transform_density(
                                                    'sent_score',
                                                    as_=['sent_score', 'density']
                                                    ).mark_area().encode(
                                                    x="sent_score:Q",
                                                    y='density:Q',
                                                )

    st.altair_chart(density_chart)

    st.write("lastly, maybe some correlations of the features to the target?")

    corrframe = X_vectorized.corrwith(y).dropna()
    corrframe = corrframe.iloc[corrframe.abs().argsort()]
    corrs_to_show = corrframe.tail(20).reset_index()
    corrs_to_show.columns = ['feature','correlation']

    corr_chart = alt.Chart(corrs_to_show).mark_bar().encode(
                                                    x=alt.X('correlation'),
                                                    y=alt.Y('feature')
    )

    st.altair_chart(corr_chart)

