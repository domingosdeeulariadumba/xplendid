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