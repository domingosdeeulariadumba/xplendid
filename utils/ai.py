# Dependencies
import streamlit as st
from utils.credentials import load_credentials
from openai import OpenAI, RateLimitError, APIConnectionError


# A function to provide AI responses 
def ask_xplendid(session_state, lang = 'en'):       
    # Prompt setup
        ## Design data
    bcr_sp = session_state.get('bcr_sp', 'Not Defined')
    mde_sp = session_state.get('mde_sp', 'Not Defined')
    alpha_sp = session_state.get('alpha_sp', 'Not Defined')
    power_sp = session_state.get('power_sp', 'Not Defined')
    is_absolute_variation_sp = session_state.get('var_sp', 'Not Defined')
    is_two_tailed_sp = session_state.get('tail_sp', 'Not Defined')
    min_sample_size = session_state.get('min_sample_size', 'Not Defined')
    message_sp = session_state.get('message_sp', 'Not Defined')
        
        ## Experiment data
    bcr_xp = session_state.get('bcr_xp', 'Not Defined')
    mde_xp = session_state.get('mde_xp', 'Not Defined')
    alpha_xp = session_state.get('alpha_xp', 'Not Defined')
    power_xp = session_state.get('power_xp', 'Not Defined')
    is_absolute_variation_xp = session_state.get('var_xp', 'Not Defined')
    is_two_tailed_xp = session_state.get('tail_xp', 'Not Defined')
    n_ctrl_xp = session_state.get('nctrl', 'Not Defined')
    p_ctrl_xp = session_state.get('pctrl', 'Not Defined')
    n_trmt_xp = session_state.get('ntrmt', 'Not Defined')
    p_trmt_xp = session_state.get('ptrmt', 'Not Defined')
    results_summary = session_state.get('results_summary', 'Not Defined')
    results_and_recommendation = ''.join(str(i) for i in results_summary)
    text = st.secrets['prompt']['en'] if lang == 'en' else st.secrets['prompt']['pt'] 
    prompt= text.format(
        # Inputs and outputs of design section
        bcr_sp, mde_sp, alpha_sp, power_sp, is_absolute_variation_sp,
        is_two_tailed_sp, min_sample_size, message_sp,
        
        # Inputs and outputs of experiment results section        
        bcr_xp, mde_xp, power_xp, alpha_xp, is_absolute_variation_xp,
        is_two_tailed_xp, n_ctrl_xp, p_ctrl_xp, n_trmt_xp, p_trmt_xp, 
        results_and_recommendation, min_sample_size
        )
      
    # Conversation setup
    credentials = load_credentials()
    messages = session_state.chat_history 
    conversation = [{'role': 'system', 'content': prompt}] + messages 
    exceptions = get_exception_responses(lang)
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
                return exceptions[0]
        except APIConnectionError:
               continue
        except:
             return exceptions[-1]        
    return exceptions[1]


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