import streamlit as st
import pandas as pd
import io
from io import BytesIO
from gtts import gTTS

# Configure the page
st.set_page_config(
   page_title="Demo",
   page_icon="📈",
   layout="centered",
   initial_sidebar_state="expanded",
)

# Input text
input_text = st.text_area(
    label="Input your text (max 250 chars)", 
    value="", 
    max_chars=250
)

# Select the library and parameters
libraryCol, langCol, otherCol = st.columns([0.3, 0.3, 1.0])

with libraryCol:
    select_lib = st.selectbox(
        label="Select library",
        options=['gTTS']
    )

with langCol:
    select_lang = st.selectbox(
        label="Select your language",
        options=['en', 'de', 'uk']
    )

with otherCol:

    if select_lib == 'gTTS':
        select_slow = st.radio(
            label="",
            options=['Normal', 'Slow'],
            horizontal=True
        )

if input_text != '':
    speech = BytesIO()
    speech_ = gTTS(
        text=input_text, 
        lang=select_lang, 
        slow=False if select_slow == "Normal" else True
    )
    speech_.write_to_fp(speech)
    
    playCol, emptyCol = st.columns([0.7, 1.0])
    
    with playCol:
        st.audio(speech)