# Dependencies
import streamlit as st
from typing import Callable
from datetime import datetime



# xplendid's background color
background_style = '''
    <style>
        .stApp {
            background: #E1EBEE;
        }
    </style>
'''


# Welcome text in English and Portuguese
def welcome_text(lang: str = 'en') -> str:
    text = '''
            <div style='text-align: justify;'>
            Bem vindo ao <strong><em>xplendid</em></strong> — a plataforma ideal para design e análise dos seus experimentos A/B. Quer optimizar o seu website, refinar funcionalidades dos seus produtos ou  melhorar o desempenho das suas campanhas de marketing? Esta aplicação coloca à sua disposição as ferramentas necessárias chegar a estes resultados.
            </div>
            ''' \
            if lang == 'pt' else \
            '''
            <div style='text-align: justify;'>
            Welcome to <strong><em>xplendid</em></strong> — your go-to platform for seamless A/B testing and data-driven decision-making. Whether you're optimizing your website, refining product features, or improving marketing campaigns, <strong><em>xplendid</em></strong> empowers you with cutting-edge tools to ensure your experiments deliver actionable insights.
            </div>
        '''
    return text

# Outputs and feedback dividers
xplendid_div_body = '''
<hr style = 'border: none; border-top: 1.5px dotted #ff66c4; height: 1px; width: 100%;'>
'''
xplendid_div_fb = '''
<div style = 'width: 58%; height: 2px; background-color:  #ff66c4'></div>
'''


# Style for the file uploader component in Streamlit
upload_dataset_button_style = '''
<style>

    [data-testid="stFileUploader"] section {
        width: fit-content;
        font-size: 0;
        padding: 0;
        background-color: transparent;
    }
    
    [data-testid="stFileUploader"] section small {
        display: none;
    }

    [data-testid="stFileUploader"] section > div {
        padding: 0;
        margin: 0;
        width: fit-content;
    }
    
    [data-testid="stFileUploader"] button {
        display: none;
    }
    
    [data-testid="stFileUploader"] svg {
        color: #ff66c4;  
    }
</style>
'''


# Overview text in English and Portuguese
xplendid_font_style = "<span style = 'color: #ff66c4;'><strong><em>xplendid</strong></em></span>"
def overview_text(lang: str = 'en') -> str:
    global xplendid_font_style
    text = '''
        <div style='text-align: justify;'>
        <strong>What Makes this Tool Exceptional?</strong>
        
        - <em><strong>Effortless Experimentation: {style}</strong> simplifies the complexities of analyzing A/B tests with tools that are accurate, intuitive, and built for speed. Calculate sample sizes, compare results, and uncover insights without missing a beat.</em>
        
        - <em><strong>Insightful Visualizations:</em></strong> dive deep into your data with dynamic charts and graphs that tell the full story. From confidence intervals to clear comparisons, {style} transforms numbers into visuals that drive action.</em>
        
        - <em><strong>Smart Recommendations:</strong> get more than just results — receive actionable guidance to understand the “what,” “why,” and “what’s next” for your experiments.</em>
        
        - <em><strong>Streamlined User Experience:</em></strong> with a clean and intuitive interface, {style} ensures that every feature is just a click away. It’s easy to use, no matter your experience level.</em>
        
        - <em><strong>Built for the Innovators:</em></strong> ideal for marketers, product managers, data analysts, and anyone who values data-driven decisions. With {style} your data becomes a superpower.</em>
        </div>
        ''' \
        if lang == 'en' else \
        '''
        <div style='text-align: justify;'>
        <strong>O que faz este serviço excepcional?</strong>
        
        - <em><strong>Experimentação Simplificada: {style}</strong> remove as complexidades do processo de análise the experimentos A/B com precisão, intuição e rapidez. Calcule tamanho de amostras, compare resultados e desvende os insights ao detalhe.</em>
        
        - <em><strong>Relatórios Informativos:</em></strong> aprofunde a análise dos seus dados como nunca através de visualizaçoes interativas. Desde gráficos de erros, para efeitos comparativos, o {style} transforma simples números em visuais sugestivos para tomada de decisão em ambientes dinâmicos.</em>
        
        - <em><strong>Recomendações Inteligentes:</strong> vá além dos números — receba oriantações para compreender os "porquês" e as próximas etapas de implementação dos seus experimentos.</em>
        
        - <em><strong>Óptima Experiência de Utilizador:</em></strong> com uma simples e prática, no {style} tudo o que é para o seu experimento está a um click.</em>
        
        - <em><strong>Feita para Inovadores:</em></strong> ideal para profissionais de marketing, product managers, analistas e cientistas de dados, e demais interessados em tomar decisões com uma abordagem data-driven. Com {style} seus dados se tornam superpoderes.</em>
        </div>
        '''
    return text.format(style = xplendid_font_style)


# Social media icons and links
kofi_icon_url = 'https://i.postimg.cc/wj3w1mjG/kofi-icon.png'
linktree_icon_url = 'https://i.postimg.cc/t4vNmLB0/linktree-icon.png'
github_icon_url = 'https://i.postimg.cc/9FVb4PDk/github-icon.png'
linkedin_icon_url = 'https://i.postimg.cc/W1178266/linkedin-icon.png'
height_ = 35
container_style = '''
background-color: #E1EBEE;
border-radius: 14px;
padding: 10px;
margin: 10px;
height: 60px;
display: flex;
justify-content: center;
align-items: center;
gap: 15px;
'''
social_icons_markdown = f'''
<div style = '{container_style}'>
        </a>
        <a href = 'https://ko-fi.com/domingosdeeulariadumba' target = '_blank' style = 'text-decoration: none;'>
            <img src = '{kofi_icon_url}' alt = "Domingos' ko-fi" height = '{height_}' width = '{height_}'/>
        </a>
        </a>
        <a href = 'https://linktr.ee/domingosdeeulariadumba' target = '_blank' style = 'text-decoration: none;'>
            <img src = '{linktree_icon_url}' alt = "Domingos' Linktree" height = '{height_}' width = '{height_}'/>
        </a>
        <a href = 'https://github.com/domingosdeeulariadumba' target = '_blank' style = 'text-decoration: none;'>
            <img src = '{github_icon_url}' alt = "Domingos' GitHub" height = '{height_}' width = '{height_}'/>
        </a>
        <a href = 'https://linkedin.com/in/domingosdeeulariadumba/' target = '_blank' style = 'text-decoration: none;'>
            <img src = '{linkedin_icon_url}' alt = "Domingos' LinkedIn" height = '{height_}' width = '{height_}'/>
        </a>
</div>
'''


# AskAI gif style based on language
askai_style: Callable[['str'], str] = lambda lang = 'en': f"<img src='{st.secrets['urls']['askai_en_gif']}' style='max-width:80px; width:auto; height:auto;'>" if lang == 'en' \
                                    else f"<img src='{st.secrets['urls']['askai_pt_gif']}' style='max-width:80px; width:auto; height:auto;'>"


# Let's connect style based on language
lets_connect_style = Callable[[str], str] = lambda lang = 'en': "<div style = 'text-align: center; color: #040404'><b>Let's connect! 🗪</b></div>" if lang == 'en' \
                                    else "<div style = 'text-align: center; color: #040404'><b>Conecta-te comigo! 🗪</b></div>"


# Footer style with current year
footer_style = f"<div style = 'text-align: center; color: #040404'>© {datetime.now().year} <b>Domingos de Eulária Dumba</b>.</div>"