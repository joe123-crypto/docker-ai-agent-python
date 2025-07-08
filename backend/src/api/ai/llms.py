import os

from langchain_google_genai import ChatGoogleGenerativeAI


GEMNI_BASE_URL = os.environ.get('GEMNI_BASE_URL') or None
GEMNI_MODEL_NAME = os.environ.get('GEMNI_MODEL_NAME') or 'gemini-2.0-flash'
GEMNI_API_KEY = os.environ.get('GEMNI_API_KEY')
if not GEMNI_API_KEY:
	raise NotImplementedError("`GEMNI_API_KEY` is required!")
 

def get_gemni_llm():
    gemni_params = {
	    "model":GEMNI_MODEL_NAME,
        "api_key":GEMNI_API_KEY,
    }
    if GEMNI_BASE_URL:
        gemni_params["base_url"] = GEMNI_BASE_URL
    
    return ChatGoogleGenerativeAI(**gemni_params)


