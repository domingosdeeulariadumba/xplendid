# Dependencies
from dotenv import load_dotenv
import os

def load_credentials(): 
    # Environment variables   
    load_dotenv()
    api_keys = [os.getenv(f'API_KEY{1 + i}') for i in range(4)]
    base_urls = sorted([os.getenv(f'BASE_URL{1 + i}') for i in range(2)] * 2)
    models = sorted(
        [os.getenv(f'MODEL{1 + i}') for i in range(2)] * 2,
        reverse = True
        )
    return zip(api_keys, base_urls, models)