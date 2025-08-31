# Dependency
import streamlit as st

def load_credentials(): 
    api_keys = st.secrets['api']['keys']
    base_urls = st.secrets['api']['base_urls']
    models = st.secrets['api']['models']
    return zip(api_keys, base_urls, models)