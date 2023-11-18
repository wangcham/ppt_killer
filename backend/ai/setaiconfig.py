import openai
import config
import os

def setconfig():
    
    # openai.proxy = "http://127.0.0.1:7890"
    # openai.api_key = config.openai_api_key

    
    
    if os.getenv('API_BASE') == '':
        openai.api_key = os.environ.get('API_KEY',"None")
        print("环境变量"+openai.api_key)
    else:
        openai.api_key = os.getenv('API_KEY')
        openai.api_base = os.getenv('API_BASE')