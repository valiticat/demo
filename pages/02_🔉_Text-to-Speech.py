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
st.text_area(
    label="Input your text (max 250 chars)", 
    value="", 
    max_chars=250
)

# Select gTTS parameters
lang, speed = st.columns([0.3,1.0])

with lang:
    select_lang = st.selectbox(
        label="Select your language",
        options=['en', 'de', 'uk']
    )

with speed:
    select_slow = st.radio(
        label="",
        options=['Normal', 'Slow'],
        horizontal=True
    )

# play_soundDe = BytesIO()
# soundDe = gTTS(text=wordAndEg, lang='de', slow=False)
# soundDe.write_to_fp(play_soundDe)
# st.audio(play_soundDe)