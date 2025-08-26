# Dependencies
import plotly.io as pio
import streamlit as st
import time
import io


# Functions for experiment design
def stream_design_recommendation(divider, message): # Display streamed info about sample size
    st.markdown(divider, unsafe_allow_html = True)
    for w in message.split(' '):
         yield w + ' '  
         time.sleep(.09)
         
# Analysis Functions
def create_plot(figure):  # Converts plots to bytes             
    buf = io.BytesIO()
    pio.write_image(figure, buf, format = 'png')
    buf.seek(0)
    return buf

def stream_experiment_recommendations(sum_1, sum_2): # Streams recommendations info
     yield sum_1
     for w in sum_2.split(' '):
         yield w + ' '  
         time.sleep(.08)
               
def print_experiment_summary(sum_0, stream_words_xp): # Prints results summary 
    st.write('💡')
    st.text(sum_0)            
    st.write_stream(stream_words_xp)


# A function for getting prompts according to the language
def get_prompt_text(lang = 'en'):
    if lang == 'en':
        with open('prompts/prompt_en.txt', mode = 'r', encoding = 'utf-8') as f:
            text = f.read()
            f.close()
    else:
        with open('prompts/prompt_pt.txt', mode = 'r', encoding = 'utf-8') as f:
            text = f.read()
            f.close()
    return text


# Exception response from AI assistant
def get_exception_responses(lang):  
    if lang == 'en':          
        exceptions = '⚠️ You are out of credits! Please, try again later.', \
        '🌐 Connection error. Please, check your internet.',\
            'An unexpected error occurred! :('
    else:
        exceptions = '⚠️ Ficaste sem créditos! Por favor, tenta mais tarde!', \
            '🌐 Erro de conexão. Por favor, Verifique a sua internet.',\
                'Ocorreu um erro inesperado! :('
    return exceptions