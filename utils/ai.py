# Dependencies
import streamlit as st
from utils.exceptions import ai_exceptions
from openai import OpenAI, RateLimitError, APIConnectionError


# Function for loading AI-related credentials
def load_credentials(): 
    api_keys, base_urls, models = tuple(
        [st.secrets['api'][i] for i in ['keys','base_urls','models']]
    )
    return zip(api_keys, base_urls, models)


# A function to provide AI responses 
def ask_xplendid(session_state, lang = 'en'):       
    # Prompt setup
        ## Design data
    bcr_design = session_state.get('bcr_design', 'Not Defined')
    mde_design = session_state.get('mde_design', 'Not Defined')
    alpha_design = session_state.get('alpha_design', 'Not Defined')
    power_design = session_state.get('power_design', 'Not Defined')
    is_absolute_variation_design = session_state.get('var_design', 'Not Defined')
    is_two_tailed_design = session_state.get('tail_design', 'Not Defined')
    min_sample_size = session_state.get('min_sample_size', 'Not Defined')
    msg_design = session_state.get('msg_design', 'Not Defined')
        
        ## Experiment data
    bcr_analytics = session_state.get('bcr_analytics', 'Not Defined')
    mde_analytics = session_state.get('mde_analytics', 'Not Defined')
    alpha_analytics = session_state.get('alpha_analytics', 'Not Defined')
    power_analytics = session_state.get('power_analytics', 'Not Defined')
    is_absolute_variation_analytics = session_state.get('var_analytics', 'Not Defined')
    is_two_tailed_analytics = session_state.get('tail_analytics', 'Not Defined')
    nctrl = session_state.get('nctrl', 'Not Defined')
    pctrl = session_state.get('pctrl', 'Not Defined')
    ntrmt = session_state.get('ntrmt', 'Not Defined')
    ptrmt = session_state.get('ptrmt', 'Not Defined')
    results_summary = session_state.get('results_summary', 'Not Defined')
    results_and_recommendation = ''.join(str(i) for i in results_summary)
    text = st.secrets['prompt']['en'] if lang == 'en' else st.secrets['prompt']['pt'] 
    prompt= text.format(
        # Inputs and outputs of design section
        bcr_design, mde_design, alpha_design, power_design, 
        is_absolute_variation_design, is_two_tailed_design, 
        min_sample_size, msg_design,
        
        # Inputs and outputs of experiment results section        
        bcr_analytics, mde_analytics, power_analytics, alpha_analytics,
        is_absolute_variation_analytics, is_two_tailed_analytics, 
        nctrl, pctrl, ntrmt, ptrmt, 
        results_and_recommendation, min_sample_size
        )
      
    # Conversation setup
    credentials = load_credentials()
    messages = session_state.chat_history 
    conversation = [{'role': 'system', 'content': prompt}] + messages 
    ai_exception = ai_exceptions(lang)
    for api_key, base_url, model in credentials: 
        try:
            client = OpenAI(api_key = api_key, base_url = base_url) 
            completion = client.chat.completions.create(
                model = model,
                messages = conversation,
                temperature = .975
                )
            response = completion.choices[0].message.content
            return response
        except RateLimitError:
                return ai_exception[0]
        except APIConnectionError:
               continue
        except:
             return ai_exception[-1]        
    return ai_exception[1]