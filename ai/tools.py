# Dependencies
import streamlit as st
from ai.rag import RAG
from langchain_core.tools import Tool


# RAG retriever
def fetch_answers(query: str) -> str:
    '''Fetch answers from xplendid's knowledge base'''
    rag_ = RAG()
    retriever = rag_.get_retriever()
    docs = retriever.invoke(query)
    return '\n\n'.join([doc.page_content for doc in docs])

# Curated A/B testing sources
def fetch_evan_miller(query: str) -> str:
    '''Fetch answers from Evan Miller's site'''
    return fetch_answers(f'site:evanmiller.org/ab-testing {query}')

def fetch_optimizely(query: str) -> str:
    '''Fetch answers from Optimizely's site'''
    return fetch_answers(f'site:optimizely.com {query}')

def fetch_cxl(query: str) -> str:
    '''Fetch answers from CXL's blog'''
    return fetch_answers(f'site:cxl.com/blog {query}')

def fetch_vwo(query: str) -> str:
    '''Fetch answers from VWO's site'''
    return fetch_answers(f'site:vwo.com {query}')

# Function for getting the list of tools
def get_tools() -> list[Tool]:
    '''Returns the list of available tools'''
    rag_description = st.secrets['rag_description']
    tools = [
        Tool(name = 'RAG_KnowledgeBase', func = fetch_answers, description = rag_description),
        Tool(name = 'EvanMiller', func = fetch_evan_miller, description = 'Statistical A/B testing guidance from Evan Miller.'),
        Tool(name = 'Optimizely', func = fetch_optimizely, description = 'Enterprise-level A/B testing tutorials from Optimizely.'),
        Tool(name = 'CXL', func = fetch_cxl, description = 'Experimentation methodology, sample size calculations, and growth insights.'),
        Tool(name = 'VWO', func = fetch_vwo, description = 'Conversion optimization and testing frameworks guidance.'),
        ]
    return tools