import streamlit as st
import os
import pandas as pd
import random


@st.cache_data
def load_data():
    df = pd.read_csv(os.path.join(os.getcwd(), "deutch_dictionary.csv"))
    df = df[:30]
    df.drop(columns=["frequency"], inplace=True)
    return df.to_dict(orient="records")

df = load_data()

if "mode" not in st.session_state:
    st.session_state.mode = "Englisch auf Deutsch"
if "random_word" not in st.session_state:
    st.session_state.random_word = random.choice(df)
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False


st.header("Willkommen beim deutschen Kartenspiel!")
st.write("Erstellt von Nicholas für Neyda und vielleicht Marilyn.")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "mari.png"), width=100)

choice = st.radio("Wählen Sie ihre sprache", ["Englisch auf Deutsch", "Deutsch auf Englisch"])
print(choice)

# Next card resets both the word and hides the answer again
if st.button("Neues Wort", key="next"):
    st.session_state.random_word = random.choice(df)

if choice == "Englisch auf Deutsch":
    st.subheader(f"Englisch Wort: {st.session_state.random_word['translation']}")
else:
    st.subheader(f"Deutsches Wort: {st.session_state.random_word['german_word']}")

# Show answer button flips a flag—does NOT pick a new word
if st.button("Antwort anzeigen", key="show"):
    if choice == "Englisch auf Deutsch":
        st.subheader(f"Deutsch Wort: {st.session_state.random_word['german_word']}")
    else:
        st.subheader(f"Englisch Wort: {st.session_state.random_word['translation']}")





# Only render the translation if that flag is True
if st.session_state.show_answer:
    st.write(f"Englisches Wort: {st.session_state.random_word['translation']}")



st.session_state.show_answer = False



