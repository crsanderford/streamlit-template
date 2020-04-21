# imports
import altair as alt
import requests
import streamlit as st
import urllib
import pandas as pd

# import the page-generating functions from your pages module.
from pages.predictions import predict_page
from pages.why_streamlit import why_streamlit_page
from pages.index import index_page
from pages.exploration import exploration_page

# create lists of the display names of pages, and the
# functions that generate those pages.
pagenames = ['index','exploration','prediction','why streamlit?']
pagefuncs = [index_page, exploration_page, predict_page, why_streamlit_page]

# zip those lists together into a dictionary.
pagedict = dict(zip(pagenames,pagefuncs))

def main():
    """The main function executes your app."""

    # this'll put a title in the sidebar.
    st.sidebar.title("streamlit app demo")

    # here we'll use our page lists and the dictionary to display
    # a dropdown menu of pages in the sidebar, and allow the user to pick one.
    page_to_load = st.sidebar.selectbox("choose a page.", pagenames)
    
    # get the corresponding function out of the dictionary. Call it.
    pagedict[page_to_load]()

    # this'll put text in the sidebar.
    bio = st.sidebar.markdown("""this sidebar is also a good place for you to summarize your project
                                and maybe write some things about yourself.""")









if __name__ == "__main__":
    # run the app
    main()