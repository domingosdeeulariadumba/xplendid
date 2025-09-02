# Dependency
import streamlit as st

def load_credentials(): 
    api_keys, base_urls, models = tuple(
        [st.secrets['api'][i] for i in ['keys','base_urls','models']]
    )
    return zip(api_keys, base_urls, models)