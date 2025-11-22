# Exception messages for the app
def stats_exceptions(lang: str = 'en') -> tuple[str, str, str, str]:
    if lang == 'en':
        global_error_msg = '❌ Input error! Hover the mouse over ❔ icon for help.'
        design_error_msg = '🚨 Invalid input(s)! Check your **BCR** or **MDE** values.'
        zero_conversions_warning = '🔔 Received **_:red[0]_** as input(s) for **Conversions**. _Is it ok?_'
        plot_error_msg = ':( No results to display! Insert valid inputs for **:red[Sample Size]** and :red[**Conversions**.]'
    else:
        global_error_msg = '❌ Input(s) incorrecto(s)! Passe o mouse sobre o ícone ❔ para mais detalhes.'
        design_error_msg = '🚨 Entrada(s) incorrecta(s)! Verifique os parâmetros **TCR** ou **MED**.'
        zero_conversions_warning = '🔔 Inseriu **_:red[0]_** como entrada em **Convertidos**. _Sem problemas?_'
        plot_error_msg = ':( Não é possível apresentar os resultados! Insira entradas válidas para **:red[Tamanho da Amostra]** e **:red[Convertidos:red]**.'    
    return global_error_msg, design_error_msg, zero_conversions_warning, plot_error_msg


# Exception responses from AI assistant
def ai_exceptions(lang: str) -> str:  
    if lang == 'en':          
        exceptions = '⚠️ You are out of credits! Please, try again later.', \
        '🌐 Connection error. Please, check your internet.',\
            'An unexpected error occurred! :('
    else:
        exceptions = '⚠️ Ficaste sem créditos! Por favor, tenta mais tarde!', \
            '🌐 Erro de conexão. Por favor, Verifique a sua internet.',\
                'Ocorreu um erro inesperado! :('
    return exceptions