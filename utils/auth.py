# Dependencies
import streamlit as st
from collections.abc import Iterator
from utils.exceptions import ai_exceptions


# Function for loading AI-related credentials
def load_credentials(api: str = 'llm') -> Iterator[tuple[str, str, str]] | tuple[str, str, str]: 
    if api == 'llm':
        api_keys, base_urls, models = tuple(
            [st.secrets['llm'][i] for i in ['keys','base_urls','models']]
        )
        return zip(api_keys, base_urls, models)
    elif api == 'milvus':
         return tuple(st.secrets['milvus'].values())
    else:
         return tuple(st.secrets['embeddings'].values())