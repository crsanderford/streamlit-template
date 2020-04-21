"""a page explaining why students might choose streamlit over plotly dash for their projects."""

import streamlit as st

def why_streamlit_page():
    """generates the "why streamlit?" page."""

    st.title("why streamlit?")

    st.write('')

    st.write('Adrien Treuille gives a quick overview of Streamlit here:')
    st.video('https://www.youtube.com/watch?v=B2iAodr0fOo')

    st.write('')
    
    st.write("""here's the gist though - streamlit applications are generated from a _script_, running it _in order_, from _top to bottom_. 
                any kind of input to the application - things like refreshing, or user input - reruns the script _in order_ from 
                _top to bottom_. this makes them very easy to reason about. Oftentimes, you can take the latter portion of a notebook where
                you trained a model (the part where you made inferences from a trained model), copypaste it into a script, add some streamlit
                code for taking user input and serving the visualizations you made, and have a functional demonstration of your model.""")

    st.write("""streamlit's API manages to be both very simple and have a lot of general utility. I just embedded a youtube video - that's as
                simple as _streamlit.video('yourvideourl')_. things like taking user input and displaying charts are similarly simple - 
                check the prediction page for a little more of that. altair charts especially play well in streamlit - you'll notice that
                altair is a dependency of streamlit, and that when you directly ask streamlit to make a chart for you (yes, you can do that!)
                it'll produce an altair chart. altair's interactivity options (hover tools and zooming) will also _just work_, 
                no bodging needed.""")

    st.write("""streamlit's greatest strength and weakness is the simplicity imposed by the _in order from top to bottom_ constraint. 
                you'll notice that streamlit applications almost always have the same layout, with _everything_ arranged vertically, the only 
                horizontal separation being the distinction between the main page and the sidebar. it's not too terribly hard to see how 
                this layout constraint would flow from streamlit's model for generating an application from a script. Rerunning upon
                all user input is also an important constraint - what if you have some backend that you want to save user input to?
                there isn't (yet!) any explicit way for you to control the default colors of the application. 
                There also isn't any true multi-page functionality.""")

    st.write("""that being said, there are workarounds to these constraints, and in a lot of cases either a, you won't run into them; or
                b, you'd be better served with multiple deployments and/or a more fully-fledged framework in the first place (Flask). 
                streamlit.cache() can fix a lot of the performance problems you might run into (you have some piece of code that is 
                resource-intensive, but only needs run once, not every time the user refreshes or makes input). There is a sneaky way 
                to change the colors of the application, if you insist upon it - though it's not intended functionality, and you can 
                fake multiple pages by writing several page-generating functions and then providing a drop-down box for the user to select 
                which runs.""")

    st.write("""Overall, I think for the expected scope of unit 2 build week projects, streamlit captures just about everything you'd need 
                and then some. If you insist upon true multi-page functionality, more complex layouts, and explicit control of the color scheme, 
                but do not want to touch Flask/work with html or css/et cetera, plotly dash is probably a reasonable choice. but streamlit 
                is probably 80 percent of the functionality for 20 percent of the bodging.""")
