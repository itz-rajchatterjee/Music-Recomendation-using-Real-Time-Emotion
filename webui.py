import streamlit as st
import webbrowser
webbrowser.open("http://streamlit.io")

lang=st.text_input("Language")
singer=st.text_input("Singer")

bn=st.button("Recomend Songs")