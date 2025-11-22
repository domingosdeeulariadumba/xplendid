# Dependencies
from plotly.graph_objects import Figure
from collections.abc import Iterator
import plotly.io as pio
import streamlit as st
import numpy as np
import time
import io


# Functions for experiment design
def stream_design_recommendation(divider: str, message: str) -> Iterator[str]: # Display streamed info about sample size
    st.markdown(divider, unsafe_allow_html = True)
    for w in message.split(' '):
         yield w + ' '  
         time.sleep(.09)
         
# Analysis Functions
def create_plot(figure : Figure) -> io.BytesIO:  # Converts plots to bytes             
    buf = io.BytesIO()
    pio.write_image(figure, buf, format = 'png')
    buf.seek(0)
    return buf

def stream_experiment_recommendations(sum_1: str, sum_2: str) -> Iterator[str]: # Streams recommendations info
     yield sum_1
     for w in sum_2.split(' '):
         yield w + ' '  
         time.sleep(.08)
               
def print_experiment_summary(sum_0: str, stream_words_xp: Iterator[str]) -> None: # Prints results summary 
    st.write('💡')
    st.text(sum_0)            
    st.write_stream(stream_words_xp)


# Function for presenting experiment results summary in portuguese
def pt_recommendation(en_results_summary: tuple[str, str, str]) -> tuple[str, str, str]:
    recomendacoes_pt = st.secrets['pt_recommendation']['analytics']
    _, results_df, text1_en = en_results_summary
    idx = np.argmax(['Given' in text1_en, 'Keep' in text1_en, 'There' in text1_en])
    recomendacao = recomendacoes_pt[idx]
    text0 = (
        f"\n\n[2] Recomendação:\n{recomendacao}"
        "\n\n\n\n*Nota: Esta recomendação não assume que a experiência tenha sido desenhada corretamente."
          )
    text1 = "\n\n\n\n*Nota: Esta recomendação não assume que a experiência tenha sido desenhada corretamente."
    return text0, results_df, text1