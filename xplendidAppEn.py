# Dependencies
import streamlit as st
from xplendidLab import ABTesting
from xplendidFuncs import stream_words_sp, create_plot, \
print_summary_xp, stream_words_xp
import time
import joblib as jbl


# Title, icon, and layout
pictograph = 'https://i.postimg.cc/y6DbW1FL/xplendid-pictograph.png'
st.set_page_config(
    page_title = 'xplendid', page_icon = pictograph, layout = 'centered',
    initial_sidebar_state = 'collapsed'
) 

# Background color
st.markdown(
    '''
    <style>
        .stApp {
            background: #E1EBEE; /*Blue grey*/
        }
    </style>
''',
    unsafe_allow_html = True
)

# Language icon
_, _, lang_col = st.columns([4, 4, .8])
lang_col.page_link('pages/pt.py', label = '', icon = '🇵🇹')
st.write('')

# xplendid logo
st.image('https://i.postimg.cc/cCJg1kKz/xplendid-logo-body.png')

# Left divider before body
left_bar = 'https://i.postimg.cc/QMZnYCdf/left-bar-body.png'
st.image(left_bar)

# Welcome and overview
st.markdown('''
        <div style='text-align: justify;'>
         Welcome to <strong><em>xplendid</em></strong> — your go-to platform for seamless experiment analysis and data-driven decision-making. Whether you're optimizing your website, refining product features, or improving marketing campaigns, <strong><em>xplendid</em></strong> empowers you with cutting-edge tools to ensure your experiments deliver actionable insights.
         </div>
''', 
unsafe_allow_html = True
)

# xplendid font style
xplendid_bold_italic = "<span style = 'color: #ff66c4;'><strong><em>xplendid</strong></em></span>"

# More info about xplendid
if st.button('👁'):
    st.markdown(
        f'''
        <div style='text-align: justify;'>
        <strong>What Makes this Tool Exceptional?</strong>
        
        - <em><strong>Effortless Experimentation: {xplendid_bold_italic}</strong> simplifies the complexities of analyzing experiments with tools that are accurate, intuitive, and built for speed. Calculate sample sizes, compare results, and uncover insights without missing a beat.</em>
 
        - <em><strong>Insightful Visualizations:</em></strong> dive deep into your data with dynamic charts and graphs that tell the full story. From confidence intervals to clear comparisons, {xplendid_bold_italic} transforms numbers into visuals that drive action.</em>
        
        - <em><strong>Smart Recommendations:</strong> get more than just results — receive actionable guidance to understand the “what,” “why,” and “what’s next” for your experiments.</em>
        
        - <em><strong>Streamlined User Experience:</em></strong> with a clean and intuitive interface, {xplendid_bold_italic} ensures that every feature is just a click away. It’s easy to use, no matter your experience level.</em>
        
        - <em><strong>Built for the Innovators:</em></strong> ideal for marketers, product managers, data analysts, and anyone who values data-driven decisions. With {xplendid_bold_italic} your data becomes a superpower.</em>
        </div>
        ''',
        unsafe_allow_html = True
        )
    _, _, less = st.columns([3, 3, .3])
    if less.button('━'):
        st.rerun()

# A call-to-action for exploring xplendid
st.write(' ') 
st.write('Let **_xplendid_** be the key to your data-driven success. Start exploring, analyzing, and achieving today! 🚀')

# Right divider before body
right_bar = 'https://i.postimg.cc/QdTyq1hB/right-bar-body.png'
st.image(right_bar)
for _ in range(3):
    st.write('')

# Design Icon
design_icon = 'https://i.postimg.cc/3JmKkyVB/design-icon.png'
st.image(design_icon)

# Outputs divider
xplendid_div_body = '''
<hr style = 'border: none; border-top: 1.5px dotted #ff66c4; height: 1px; width: 100%;'>
'''

# Feedback divider
xplendid_div_fb = '''
<div style = 'width: 58%; height: 2px; background-color:  #ff66c4'></div>
'''
            
# Toast text for exception handling
hint = '❌ Input error! Hover the mouse over ❔ icon for help.'

# Toast for checking sample size inputs
inputs_sp = '🚨 Invalid input(s)! Check your **BCR** or **MDE** values.'

# Toast for conversions if it is 0
zero_conv_hint = '🔔 Received **_:red[0]_** as input(s) for **Conversions**. _Is it ok?_'

# Toast for notifying about analysis resuls unavailability
plot_error_hint = ':( No results to display! Insert valid inputs for **:red[Sample Size]** and :red[**Conversions**.]'

# Sample size calculator expander
with st.expander('Design your experiment ↴'):
    for _ in range(5):
        st.write('\n')
    left_sp, _, right_sp = st.columns([1.5, .5, 1.5])
    with left_sp.container():
        bcr_sp = st.number_input('Baseline Conversion Rate (%)', help = 'Spans from 0 to 100.')
        
        st.write('\n')
        mde_sp = st.number_input('Minimum Detectable Effect (%)', help = 'Must be positive.')
        st.write('\n')
        is_absolute_variation_sp = st.toggle('Absolute Variation', True)
    
    with right_sp.container():
        alpha_sp = st.slider('Significance Level (%)', 1, 10, 5)
        power_sp = st.slider('Power (%)', 80, 99)
        is_two_tailed_sp = st.toggle('Two-Tailed Test', True)
        st.write('\n\n')
    _, sample_size, _ = st.columns(3)

    # Computing the user inputs
    try:    
        if sample_size.button('Calculate sample size'):
            ab_exp_sp = ABTesting(bcr_sp, mde_sp, alpha = alpha_sp, 
                                            power = power_sp, is_absolute_variation = is_absolute_variation_sp,
                                           is_two_tailed = is_two_tailed_sp)
            min_sample_size = ab_exp_sp.evan_miller_sample_size()
            
            # Presenting the sample size info
            if type(min_sample_size) is int: 
                message_sp_1 = 'You should conduct your experiment with at least'
                message_sp_2 = f' **{min_sample_size}** '
                message_sp_3 = 'observations per variant.'
                message_sp = message_sp_1 + message_sp_2 + message_sp_3
                st.write('')
                st.write_stream(
                    stream_words_sp(xplendid_div_body, message_sp)
                    )
            else:
                st.toast(inputs_sp)                
    except:
        st.toast(hint)
  
    

# Experiment results icon
for _ in range(2):
    st.write('')
analysis_icon = 'https://i.postimg.cc/7h1Wkytg/analysis-icon.png'
st.image(analysis_icon)


# Experiment results expander
with st.expander('Analyse your results ↴'):
    for _ in range(4):
        st.write('\n')
        
    # Design container      
    ## Left Container
    left_xp_sp, _, right_xp_sp = st.columns([1.5, .5, 1.5])
    with left_xp_sp.container():
        bcr_xp = st.number_input(
            'Baseline Conversion Rate (%)', None, key = 'bcr_xp',
            help = 'Spans from 0 to 100.'
            )
        st.write('')
        mde_xp = st.number_input(
            'Minimum Detectable Effect (%)', None, key = 'mde_xp',
            help = 'Must be positive.'
            )
        st.write('\n')
        is_absolute_variation_xp = st.toggle(
            'Absolute Variation', True, key = 'var_xp'
            )    
    
    ## Right container
    with right_xp_sp.container():
        alpha_xp = st.slider(
            'Significance Level (%)', 1, 10, key = 'alpha_xp',
            )
        power_xp = st.slider(
            'Power (%)', 80, 99, key = 'power_xp'
            )
        is_two_tailed_xp = st.toggle(
            'Two-Tailed Test', True, key = 'tail_xp')

    # Experiment container        
    ## Left container
    st.write('')
    left_xp, _, middle_xp, _, right_xp = st.columns([1.5, .5, 1.5, .5, 2])
    with left_xp.container():
        st.markdown(
            xplendid_bold_italic.replace('xplendid', 'Control'), 
            unsafe_allow_html = True)
        n_ctrl_xp = st.number_input(
            '_Sample Size_', 0, key = 'nctrl', help = 'Must be positive integer.'
            )
        p_ctrl_xp = st.number_input(
            '_Conversions_', key = 'pctrl', help = 'Spans from 0 to 1.'
            )
        
    ## Middle container
    with middle_xp.container():
           st.markdown(
               xplendid_bold_italic.replace('xplendid', 'Treatment'), 
               unsafe_allow_html = True)
           n_trmt_xp = st.number_input(
               'Sample Size', 0, key = 'ntrmt', label_visibility = 'hidden'
               )
           p_trmt_xp = st.number_input(
               'Conversions', key = 'ptrmt', label_visibility = 'hidden'
               )
           
    ## Right container
    with right_xp.container():
        for _ in range(2):
            st.write('')
        plot_xp = st.radio(
            'Chart Type', ['KDE', 'Confidence Intervals']
            )  
    
    # Initializing the session state after viewing results
    if 'exp_results_button' not in st.session_state:
        st.session_state.exp_results_button = False
        
    ## Results button
    exp_results, _, _ = st.columns([.3, 1.5, 1.5])    
    
    # Tasks if option to get results is triggered
    if exp_results.button('▷', help = 'Get results!'):  
        st.session_state.exp_results_button = True

    ## Keeping the session open
    if st.session_state.exp_results_button:  
        success = True
        try:
            ## Compute design inputs
            ab_experiment_xp = ABTesting(bcr_xp, mde_xp, alpha = alpha_xp, 
                                        power = power_xp, is_absolute_variation = is_absolute_variation_xp,
                                        is_two_tailed = is_two_tailed_xp)           
        except Exception as e:
            st.toast(inputs_sp)
            st.write(f"Error in computing design inputs: {e}")
            success = False

        ## A spinner for processing the plot display       
        with st.spinner('Processing...'):
            time.sleep(1)        

        # Trying to show results after computing design parameters
        if success:            
            try:
                ## Computing results for plotting 
                fig = ab_experiment_xp.get_experiment_results(
                    n_ctrl_xp, p_ctrl_xp, n_trmt_xp, p_trmt_xp, plot_ = plot_xp)
                
                ## Computing recommendations
                results_summary = ab_experiment_xp.get_experiment_results(
                    n_ctrl_xp, p_ctrl_xp, n_trmt_xp, p_trmt_xp, plot_ = None)
                
                # Toast for notifying 0 as input of conversions
                if 0 in [p_ctrl_xp, p_trmt_xp]:
                    st.toast(zero_conv_hint)
                    
                ## Dotted divider and spinner for processing the plot display 
                st.write('')
                st.markdown(xplendid_div_body, unsafe_allow_html = True)
                
                ## Plotting results
                st.plotly_chart(fig, config = {'displayModeBar': False})
                
                ## Download and view recommendation buttons
                _, download_col, sum_col, _ = st.columns([4, 1.5, 1.5, 4])
                
                ## Making the plot downloadable
                img_buf = create_plot(fig)        
                filename = f"experiment_results_{plot_xp.lower().replace(' ', '')}.png"
                
                ## Injecting download button
                download_col.download_button('📥', data = img_buf, file_name = filename)
                
                ## Injecting view recommendation button
                if sum_col.button('💬', help = 'View results and recommendation'):
                    
                    ## Dotted divider for presenting recommendations 
                    st.markdown(xplendid_div_body, unsafe_allow_html = True)
                    
                    ## Presenting results summary and recommendations
                    print_summary_xp(
                        results_summary[0], 
                        stream_words_xp(results_summary[1], results_summary[2])
                        )
                    
                    ## Close recommendation button 
                    _, _, close_col, _ = st.columns([4, 4, .3, .2])
                    if close_col.button('↖'):
                        st.rerun()
            except Exception as e:
                st.write(f"Error in showing results: {e}")
                st.write(plot_error_hint)
        else:
            st.write("Failed to compute design inputs.")
    

    
# Feedback section
_, _, fb_col = st.columns([1.5, 1.5, 1.8])
with fb_col.container():
    for _ in range(4):
        st.write('')
    st.markdown(f'Rate **{xplendid_bold_italic}** now!', unsafe_allow_html = True) 
    feedback_series = jbl.load('xplendidFeedbackSeries.joblib')
    sentiment_mapping = ['one', 'two', 'three', 'four', 'five']
    selected = st.feedback('stars')
    st.markdown(xplendid_div_fb, unsafe_allow_html = True)
    if selected is not None:
        if sentiment_mapping[selected] == 'one':
            st.markdown(f'You gave **{sentiment_mapping[selected]}** star to **xplendid**! Thank you for your feedback. 😉')
        else:
            st.markdown(f'You gave {sentiment_mapping[selected]} stars to **xplendid**! Thank you for your feedback. 😉')
        feedback_series[len(feedback_series)] = sentiment_mapping[selected]
        jbl.dump(feedback_series, 'xplendidFeedbackSeries.joblib')
    else:
        pass



# Links section    
for i in range(8):
    st.write('')

# Customized invite for connection
container_title = '''<div style = 'text-align: center; color: #040404'><b>Let's connect! 🗪</b></div>'''
st.markdown(container_title, unsafe_allow_html=True)

# Connection icons
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
            <img src = '{kofi_icon_url}' 
                 alt = 'Domingos' ko-fi' 
                 height = '{height_}' width = '{height_}'/>
        </a>
        </a>
        <a href = 'https://linktr.ee/domingosdeeulariadumba' target = '_blank' style = 'text-decoration: none;'>
            <img src = '{linktree_icon_url}' 
                 alt = 'Domingos' Linktree' 
                 height = '{height_}' width = '{height_}'/>
        </a>
        <a href = 'https://github.com/domingosdeeulariadumba' target = '_blank' style = 'text-decoration: none margin:;'>
            <img src = '{github_icon_url}' 
                 alt = "Domingos' GitHub" 
                 height = '{height_}' width = '{height_}' />
        </a>
        <a href = 'https://linkedin.com/in/domingosdeeulariadumba/' target = '_blank' style = 'text-decoration: none;'>
            <img src = '{linkedin_icon_url}' 
                 alt = "Domingos' LinkedIn" 
                 height = '{height_}' width = '{height_}' />
        </a>
</div>
'''

# Centralizing the connection icons
_, middle, _ = st.columns([0.5, .5, 0.5])
with middle.container(border = False):
    st.markdown(icons_markdown,
                unsafe_allow_html = True)
    
# Footer stuff
footer_markdown = '''<div style = 'text-align: center; color: #040404'>
Developed by <b>Domingos de Eulária Dumba</b>
 © 2025.
</div>'''
st.markdown(footer_markdown, unsafe_allow_html = True)