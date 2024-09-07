import os
import json

import streamlit as st
import openai

# configuring openai - api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# configuring streamlit page settings
st.set_page_config(
    page_title="Personal Finance Advisor",
    page_icon="🔑💸",
    layout="centered",
)
