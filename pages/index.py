"""the base page for our streamlit app."""

import streamlit as st

def index_page():
    """generates the base page for the streamlit app."""

    st.title("index page")

    st.image('https://camo.githubusercontent.com/5ae1dcfd188be26bbb0648fb62e9d6d593dbb6f5/68747470733a2f2f617773312e646973636f757273652d63646e2e636f6d2f7374616e6461726431302f75706c6f6164732f73747265616d6c69742f6f726967696e616c2f31582f323932653938356637663735656637626566386332376235383939663731663736636435373765302e676966')

    st.write("""this app is both a demonstration of streamlit as a dashboarding tool, and a 
                template for a unit 2 streamlit application. If you'd like to use streamlit for
                your unit 2 project, you might fork the repo for this application and simply 
                make changes to it in order to build your own application, or otherwise just 
                use this application to get you started. that being said, it's worth noting that 
                the structure of this application (creating page-generating functions in separate modules
                and then importing them into the main app.py script to be selected by a dropdown menu) may 
                be more complex than you'll need for your application. It's entirely possible that all you'll 
                need is to take some of your code from your notebook, put it in a script, and then use some 
                streamlit calls on what you'd like to display.""")

    st.write("""in the sidebar to the left, you'll see a dropdown menu. each option is a page. 
                if you're considering using streamlit, you might take a look at "why streamlit?". 
                the other pages are largely meant as templates for the kind of content or functionality 
                you'd consider adding to your application.""")

    st.write("""the "exploration" and "prediction" pages are where the fun stuff happens - in "exploration", 
                I'll show you some ways to serve exploratory visualizations using streamlit on top of pandas 
                and altair. in "prediction", I'll demonstrate taking user input, unpickling a trained model, and 
                then passing the user input to the model to serve predictions, as well as insights coming from
                the model itself.""")

    st.write("""learn more about streamlit through the [docs](https://docs.streamlit.io/), or at streamlit's 
                [discussion page](https://discuss.streamlit.io/).""")