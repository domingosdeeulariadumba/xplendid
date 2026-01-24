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


def overview_text(brand:str, lang: str = 'en'):
    text = '''
        <div style='text-align: justify;'>
        <strong>What Makes this Tool Exceptional?</strong>
        
        - <em><strong>Effortless Experimentation: {brand}</strong> simplifies the complexities of analyzing A/B tests with tools that are accurate, intuitive, and built for speed. Calculate sample sizes, compare results, and uncover insights without missing a beat.</em>
        
        - <em><strong>Insightful Visualizations:</em></strong> dive deep into your data with dynamic charts and graphs that tell the full story. From confidence intervals to clear comparisons, {brand} transforms numbers into visuals that drive action.</em>
        
        - <em><strong>Smart Recommendations:</strong> get more than just results — receive actionable guidance to understand the “what,” “why,” and “what’s next” for your experiments.</em>
        
        - <em><strong>Streamlined User Experience:</em></strong> with a clean and intuitive interface, {brand} ensures that every feature is just a click away. It’s easy to use, no matter your experience level.</em>
        
        - <em><strong>Built for the Innovators:</em></strong> ideal for marketers, product managers, data analysts, and anyone who values data-driven decisions. With {brand} your data becomes a superpower.</em>
        </div>
        ''' \
        if lang == 'en' else \
        '''
        <div style='text-align: justify;'>
        <strong>O que faz este serviço excepcional?</strong>
        
        - <em><strong>Experimentação Simplificada: {brand}</strong> remove as complexidades do processo de análise the experimentos A/B com precisão, intuição e rapidez. Calcule tamanho de amostras, compare resultados e desvende os insights ao detalhe.</em>
        
        - <em><strong>Relatórios Informativos:</em></strong> aprofunde a análise dos seus dados como nunca através de visualizaçoes interativas. Desde gráficos de erros, para efeitos comparativos, o {brand} transforma simples números em visuais sugestivos para tomada de decisão em ambientes dinâmicos.</em>
        
        - <em><strong>Recomendações Inteligentes:</strong> vá além dos números — receba oriantações para compreender os "porquês" e as próximas etapas de implementação dos seus experimentos.</em>
        
        - <em><strong>Óptima Experiência de Utilizador:</em></strong> com uma simples e prática, no {brand} tudo o que é para o seu experimento está a um click.</em>
        
        - <em><strong>Feita para Inovadores:</em></strong> ideal para profissionais de marketing, product managers, analistas e cientistas de dados, e demais interessados em tomar decisões com uma abordagem data-driven. Com {brand} seus dados se tornam superpoderes.</em>
        </div>
        '''.format(brand=brand)
    return text



# Ícones da secção de links
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
icons_markdown = f'''
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