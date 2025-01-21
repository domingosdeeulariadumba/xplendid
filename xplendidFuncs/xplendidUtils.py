# Dependencies
import streamlit as st
import time
import io
import plotly.io as pio


# Functions for experiment design
def stream_words_sp(divider, message): # Display streamed info about sample size
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

def stream_words_xp(sum_1, sum_2): # Streams recommendations info
     yield sum_1
     for w in sum_2.split(' '):
         yield w + ' '  
         time.sleep(.08)
               
def print_summary_xp(sum_0, stream_words_xp): # Prints results summary 
    st.write('💡')
    st.text(sum_0)            
    st.write_stream(stream_words_xp)

        
    
                       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    