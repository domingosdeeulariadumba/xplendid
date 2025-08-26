import streamlit as st

# Inject CSS
st.markdown("""
<style>
/* First button only: circular */
div.stButton:nth-child(1) > button {
    border-radius: 50%;           /* circular */
    width: 60px; height: 60px;
    background-color: transparent;
    border: 2px solid #4CAF50;
    color: #4CAF50;
    font-size: 16px;
}

/* Hover effect */
div.stButton:nth-child(1) > button:hover {
    background-color: #4CAF50;
    color: white;
}

/* Second button stays normal */
div.stButton:nth-child(2) > button {
    border-radius: 4px;           /* default */
    background-color: #f0f0f0;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Buttons
if st.button("Go"):  # First button (circular)
    st.write("Circular button clicked!")

if st.button("Normal"):  # Second button
    st.write("Normal button clicked!")
