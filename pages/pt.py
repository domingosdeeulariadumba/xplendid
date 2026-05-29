## Dependências
import time, pandas as pd, joblib as jbl, streamlit as st
from ablisk.core import ABLisk
from ablisk.utils import load_from_dataset
from ai.assistant import ask_xplendid
from utils.exceptions import stats_exceptions
from utils.core import (
    stream_design_recommendation, create_plot, 
    stream_experiment_recommendations, print_experiment_summary, pt_recommendation
)
import sys
sys.path.append('..')
from styles import *


# Cor de Fundo e estilo da página
set_page(st)
st.markdown(background_style, unsafe_allow_html = True)

# A apagar a sessão da página em Inglês
if 'pt_initialized' not in st.session_state:
    st.session_state['chat_history'] = []
    st.session_state['pt_initialized'] = True
    
# Link para mudança de página
_, _, lang_col = st.columns([4, 4, .8])
lang_col.page_link('app.py', label = '', icon = '🇬🇧')
st.write('')

# Logo
st.markdown(f"<img src = '{st.secrets['urls']['logo']}'>", unsafe_allow_html = True)

# Divisor antes do corpo
st.markdown(f"<img src = '{st.secrets['urls']['left_div']}'>", unsafe_allow_html = True)

# Boas vindas e visão geral
st.markdown(welcome_text('pt'), unsafe_allow_html = True)

# Mais sobre xplendid
if st.button('↘'):
    st.markdown(overview_text(xplendid_font_style, 'pt'), unsafe_allow_html = True)
    _, _, less = st.columns([3, 3, .3])
    if less.button('↖'):
        st.rerun()

# Call-to-action para começar a explorar o xplendid
st.write(' ') 
st.write('Explore, analise e produza resultados hoje! 🚀')

# Barra divisora antes do corpo da página
st.markdown(f"<img src = {st.secrets['urls']['right_div']}>", unsafe_allow_html = True)
for _ in range(3):
    st.write('')

# Ícone para design de experimentos
st.markdown(f"<img src = '{st.secrets['urls']['design_icon']}'>", unsafe_allow_html = True)
st.write('')
            
# Tratamento de excepções relativos ao design e à análise do experimento
global_error_msg, design_error_msg, zero_conversions_warning, plot_error_msg = stats_exceptions('pt')

# Expansor da calculadora de dimensão amostral
with st.expander('Planeie o seu experimento ↴'):
    for _ in range(5):
        st.write('\n')
    ex_design_left, _, ex_design_right = st.columns([1.5, .5, 1.5])
    with ex_design_left.container():
        bcr_design = st.number_input(
            'Taxa de Conversão de Referência (%)', 
            help = 'Varia de 0 a 100.',
            key = 'bcr_design'
            )        
        st.write('\n')
        mde_design = st.number_input(
            'Mínimo Efeito Detectável (%)', 
            help = 'Deve ser positivo.',
            key = 'mde_design'
            )
        st.write('\n')
        is_absolute_variation_design = st.toggle('Variação Absoluta', True, key = 'var_design')
    
    with ex_design_right.container():
        alpha_design = st.slider('Nível de Significância (%)', 1, 10, 5, key = 'alpha_design')
        power_design = st.slider('Poder Estatístico (%)', 80, 99, key = 'power_design')
        is_two_tailed_design = st.toggle('Teste Bicaudal', True, key = 'tail_design')
        st.write('\n\n')
    _, sample_size, _ = st.columns(3)

    # A computar inputs para cálculo de tamanho de amostra ideal
    if sample_size.button('Calcular Tamanho Amostral'):
        try:  
            ab_test_design = ABLisk(
                bcr_design, 
                mde_design, 
                alpha = alpha_design,
                power = power_design,
                is_absolute_variation = is_absolute_variation_design,
                is_two_tailed = is_two_tailed_design
                )
            min_sample_size = ab_test_design.get_sample_size()
            
            # A apresentar a informação relativa ao tamanho amostral
            if isinstance(min_sample_size, int):
                formatted = f'{min_sample_size:,}'.replace(',', '.')
                msg_design = st.secrets['summary']['design']['pt'].format(formatted)
                st.write('')
                st.write_stream(
                    stream_design_recommendation(
                        xplendid_div_body,
                        msg_design
                        )
                    )
                st.session_state.update({
                    'min_sample_size': min_sample_size,
                    'msg_design': msg_design
                            })
            else:
                st.toast(design_error_msg)                
        except:
            st.toast(global_error_msg)
  
    

# Ícone para resultados do experimento
for _ in range(2):
    st.write('')
st.markdown(f"<img src = '{st.secrets['urls']['analysis_icon']}'>", unsafe_allow_html = True)
st.write('')


# Expansor para análise de resultados do experimento
with st.expander('Analise os seus resultados ↴'):
    # Design container      
    _, dataset_upload, _ = st.columns([1.5, .1, 1.5])
    with dataset_upload.container():
        st.markdown(upload_dataset_button_style, unsafe_allow_html = True)
        uploaded_file = st.file_uploader(
            label = ' ',
            type = 'csv', 
            key = 'upload_dataset',
            help = 'Carregeue a base de dados do seu experimento. Deve ser um ficheiro .csv.'
            )
    if uploaded_file is not None:
        experiment_dataset = pd.read_csv(uploaded_file).dropna()
        defaults = load_from_dataset(experiment_dataset)


    # Container dedicado ao design do experimento     
    ## Lado esquerdo
    for _ in range(2):
        st.write('\n')
    ex_analytics_upperleft, _, ex_analytics_upperright = st.columns([1.5, .5, 1.5])
    with ex_analytics_upperleft.container():
        bcr_analytics = st.number_input(
            'Taxa de Conversão de Referência (%)',
            None,
            key = 'bcr_analytics',
            help = 'Varia de 0 a 100.'
            )
        st.write('')
        mde_analytics = st.number_input(
            'Mínimo Efeito Detectável (%)',
            None,
            key = 'mde_analytics',
            help = 'Deve ser positivo.'
            )
        st.write('\n')
        is_absolute_variation_analytics = st.toggle(
            'Variação Absoluta',
            True,
            key = 'var_analytics'
            )    
    
    ## Lado direito
    with ex_analytics_upperright.container():
        alpha_analytics = st.slider(
            'Nível de Significância (%)',
            1,
            10,
            key = 'alpha_analytics',
            )
        power_analytics = st.slider(
            'Poder Estatístico (%)',
            80, 
            99, 
            key = 'power_analytics'
            )
        is_two_tailed_analytics = st.toggle(
            'Teste Bicaudal', 
            True,
            key = 'tail_analytics'
            )

    # Container dedicado aos resultados experimento       
    ## Lado esquerdo
    st.write('')
    ex_analytics_lowerleft, _, ex_analytics_lowermiddle, _, ex_analytics_lowerright = st.columns([1.5, .5, 1.5, .5, 2])
    with ex_analytics_lowerleft.container():
        st.markdown(
            xplendid_font_style.replace('xplendid', 'Controlo'), 
            unsafe_allow_html = True
            )
        nctrl = st.number_input(
            '_Tamanho da Amostra_',
            0 if uploaded_file is None else defaults[0],
            key = 'nctrl',
            help = 'Deve ser um inteiro positivo.'
            )
        pctrl = st.number_input(
            '_Convertidos_', 
            .0 if uploaded_file is None else defaults[1],
            key = 'pctrl',
            help = 'Varia de 0 a 1.'
            )
        
    ## Centro do container
    with ex_analytics_lowermiddle.container():
           st.markdown(
               xplendid_font_style.replace('xplendid', 'Efeito'), 
               unsafe_allow_html = True
               )
           ntrmt = st.number_input(
               'Tamanho da Amostra',
                0 if uploaded_file is None else defaults[2],
                key = 'ntrmt',
                label_visibility = 'hidden'
               )
           ptrmt = st.number_input(
               'Convertidos', 
               .0 if uploaded_file is None else defaults[-1],
               key = 'ptrmt',
               label_visibility = 'hidden'
               )
           
    ## Container direito
    with ex_analytics_lowerright.container():
        for _ in range(2):
            st.write('')
        plot_analytics_pt = st.radio('Gráfico', ['KDE', 'Barras de Erro']) 
        plot_analytics = 'Error Bars' if plot_analytics_pt == 'Barras de Erro' else plot_analytics_pt         
     
    # Inicialização da sessão para visualização de resultados
    if 'experiment_results_button' not in st.session_state:
        st.session_state.experiment_results_button = False
        
    ## Botão para visualização de resultados
    experiment_results, _, _ = st.columns([.3, 1.5, 1.5])    
    
    ## Etapas a executar caso o botão seja premido
    if experiment_results.button('▷', help = 'Ver resultados!'):  
        st.session_state.experiment_results_button = True
        
    ## A manter a sessão aberta
    if st.session_state.experiment_results_button:  
        success = True
        try:
            ## A computar resultados
            ab_test_analytics = ABLisk(
                bcr_analytics, 
                mde_analytics,
                alpha = alpha_analytics,
                power = power_analytics,
                is_absolute_variation = is_absolute_variation_analytics,
                is_two_tailed = is_two_tailed_analytics
                )                 
        except:
            if not st.session_state.get('design_error_shown', False):
                st.toast(design_error_msg)
                st.session_state['design_error_shown'] = True
            success = False
        
        ## Spinner para processar a apresentação de resultados       
        with st.spinner('A processar...'):
            time.sleep(1)
        
        # A tentar mostrar resultados após inserção de parâmetros de design
        if success:            
            try:
                ## A criar gráfico com o título e legendas em português
                fig = ab_test_analytics.get_experiment_results(
                    nctrl,
                    pctrl, 
                    ntrmt,
                    ptrmt, 
                    plot_ = plot_analytics
                    )
                if plot_analytics == 'KDE':
                    fig.data[0].name = 'Controlo'
                    fig.data[2].name = 'Efeito'
                    fig.data[4].name = 'MED'
                else:
                    fig.data[0].name = 'Controlo'
                    fig.data[1].name = 'Efeito'
                    fig.data[3].name = 'MED'
                fig.update_layout(title = dict(text = 'Resultados do Experimento'))
                                
                ## A gerar recomendação
                results_summary_en = ab_test_analytics.get_experiment_results(
                                nctrl, 
                                pctrl, 
                                ntrmt,
                                ptrmt, 
                                plot_ = None,
                                full_summary = False
                                )
                results_summary = pt_recommendation(results_summary_en)
                
                # Notificação para o caso de se ter 0 convertidos
                if 0 in [pctrl, ptrmt] and not st.session_state.get('zero_warning_shown', False):
                    st.toast(zero_conversions_warning)
                    st.session_state['zero_warning_shown'] = True
                    
                ## Divisor e spinner para apresentar resultados 
                st.write('')
                st.markdown(xplendid_div_body, unsafe_allow_html = True)
                
                ## A apresentar o gráfico
                st.plotly_chart(fig, config = {'displayModeBar': False})
                
                ## Secção de download e visualização de recomendações
                _, download_col, summary_col, _ = st.columns([4, 1.5, 1.5, 4])
                
                # Tornando o gráfico descarregável
                img_buf = create_plot(fig)        
                filename = f"resultados_experimento_{plot_analytics.lower().replace(' ', '')}.png"
                
                ## Injecção do botão de download
                download_col.download_button('📥', data = img_buf, file_name = filename)
                
                ## Injecting view recommendation button
                if summary_col.button('💬', help = 'Ver resultados e recomendação'):
                    
                    ## Divisor para apresentação de recomendações
                    st.markdown(xplendid_div_body, unsafe_allow_html = True)
                    
                    ## A apresentar resultados e recomendações
                    print_experiment_summary(
                        results_summary[0], 
                        stream_experiment_recommendations(results_summary[1], results_summary[2])
                        )
                    
                    # A salvar o resumo na sessão
                    st.session_state.update({'results_summary': results_summary})
                
                    ## A fechar a secção de resultados
                    _, _, close_col, _ = st.columns([4, 4, .3, .2])
                    if close_col.button('↖'):
                                 st.rerun()
            except Exception as e:
                st.write(e)
                #st.write(plot_error_msg)
        else:
            pass
    

    
# Secção de feedback
chat_col, open_chat_col, _, feedback_col = st.columns([.6, .2, 2.1, 1.7])
with feedback_col.container():
    for _ in range(4):
        st.write('')
    st.markdown(f'Avalie o **{xplendid_font_style}** agora!', unsafe_allow_html = True) 
    feedback_series = jbl.load('feedbacks.joblib')
    sentiment_mapping = ['uma', 'duas', 'três', 'quatro', 'cinco']
    selected = st.feedback('stars')
    st.markdown(xplendid_div_fb, unsafe_allow_html = True)
    if selected is not None:
        if sentiment_mapping[selected] == 'uma':
            st.markdown(f'Você deu **{sentiment_mapping[selected]}** estrela ao **xplendid**! Obrigado pelo seu feedback. 😉')
        else:
            st.markdown(f'Você deu **{sentiment_mapping[selected]}** estrelas ao **xplendid**! Obrigado pelo seu feedback. 😉')
        feedback_series[len(feedback_series)] = sentiment_mapping[selected]
        jbl.dump(feedback_series, 'feedbacks.joblib')
    else:
        pass


# Chat e seus elementos
@st.dialog(' ')
def show_dialog(session_state):
      
    # Initialização do chat
    messages = st.container()
    messages.info(
        '''
        Olá! 👋🏾\n
        Alguma questão sobre o **_xplendid_**, teus resultados, ou experimentos A/B?
        '''
        )
    if 'chat_history' not in session_state:
        session_state.chat_history = []  
        
    # Accionando a resposta do assistente           
    if user_query := st.chat_input('Exponha a sua questão!'):
        session_state.chat_history.append(
            {'role': 'user', 'content': user_query}
            )
        response = ask_xplendid(session_state, lang = 'pt')  
        session_state.chat_history.append(
            {'role': 'assistant', 'content': response}
            )         
        
    # Renderização da conversa
    for msg in session_state.chat_history:
        with messages.chat_message(msg['role']):
            st.markdown(msg['content'])                     

chat_col.markdown(askai_style('pt'), unsafe_allow_html = True)
if open_chat_col.button('⭹'):
    show_dialog(st.session_state)


# Secção de links    
for i in range(8):
    st.write('')
st.markdown(lets_connect_style('pt'), unsafe_allow_html=True)
_, middle, _ = st.columns([.5, .5, .5])
with middle.container(border = False):
    st.markdown(social_icons_markdown, unsafe_allow_html = True)

# Rodapé
st.markdown(footer_style, unsafe_allow_html = True)