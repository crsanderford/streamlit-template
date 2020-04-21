"""here, you'll unpickle your pickled model, write the functions you need use it,
    and incorporate it into the predict_page function which creates the page."""
import altair as alt
import streamlit as st
import sklearn
import joblib
import pandas as pd
import re

# we're unpickling our pickles here so that we don't unpickle every time the page is loaded.

process_pipe = joblib.load('pickles/process_pipe')
feature_list = joblib.load('pickles/feature_list')
clf = joblib.load('pickles/clf')

def clean_text(text): 
    """Clean our tweets using regex. Remove weird characters and links."""
    cleanedup = text.lower()
    return re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", cleanedup)


def predict_page():
    """generates the prediction page."""

    st.title('predictions')
    st.write("on this page, you might display your model in action.")

    st.write("""you might choose to take input from the user and feed it to the model, like a text field:""")
    userinput = st.text_input("what is your quest?", "to find the holy grail!")
    st.write("your quest is - "+userinput+"?")

    st.write("""or a slider:""")
    userinput2 = st.slider(label="on a scale of 1 to 10, how cool is this app?", min_value=0.0, max_value=10.0, value=0.1)
    response = (lambda x: 'harsh.' if x < 3.33 else ("_awwwright awright awright!_" if x > 6.66 else "that's more like it."))(userinput2)
    st.write(str(userinput2) + "? " + response)

    st.write('')
    st.write("""alright, let's try it with an actual pickled model. We'll get text input from the user:""")
    modelinput = st.text_input("how do you feel about bitcoin? tell me *everything*.", "uhhh...")

    st.write("""then we'll pass that input through the processing pipeline:""")
    vectorized_input = process_pipe.transform([clean_text(modelinput)])
    vectorized_input = pd.DataFrame(vectorized_input.toarray(), columns=feature_list)
    st.write(vectorized_input)

    st.write("""and then pass the processed input to our model for inference:""")
    inference = clf.predict(vectorized_input)
    st.write("""survey says... """ + str(inference[0]))

    st.write("""okay, that's pretty neat. but what about interpreting the model?""")
    st.write("""let's plot some feature importances.""")

    def headsandtails(df, x=10): 
        """get the first and last values of a dataframe."""
        return df.head(x).append(df.tail(x))

    positive_coefficients = pd.DataFrame({
        'features': feature_list,
        'coefs': (clf.coef_[2]),
    })

    positive_importance = headsandtails(positive_coefficients.sort_values('coefs'))

    positive_importance_chart = alt.Chart(
        positive_importance,
        title='20 Most Important Words for Positive Class'
    ).mark_bar().encode(
        x=alt.X('coefs', title = 'Importance', sort = None),
        y=alt.Y(
            'features',
            title = 'Word',
            sort=alt.EncodingSortField(
                field="coefs",  # The field to use for the sort
                order="descending"  # The order to sort in
            )
        ),
        color=alt.Color('coefs', title=None, scale=alt.Scale(scheme="blueorange")),
        tooltip=[
            alt.Tooltip('coefs', title='Importance'),
        ]
    ).properties(width=550)

    st.altair_chart(positive_importance_chart)

    st.write('')
    st.write("paint's still drying, don't touch anything!")