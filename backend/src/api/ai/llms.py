import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
 

def get_gemni_llm(model=None):
    GEMNI_BASE_URL = os.environ.get('GEMNI_BASE_URL') or None
    GEMNI_MODEL_NAME = os.environ.get('GEMNI_MODEL_NAME') or 'gemini-2.0-flash'
    GEMNI_API_KEY = os.environ.get('GEMNI_API_KEY')

    if not GEMNI_API_KEY:
        raise NotImplementedError("`GEMNI_API_KEY` is required!")

    gemni_params = {
	    "model":GEMNI_MODEL_NAME,
        "api_key":GEMNI_API_KEY,
    }
    if model:
        gemni_params["model"] = model
        
    if GEMNI_BASE_URL:
        gemni_params["base_url"] = GEMNI_BASE_URL
    
    return ChatGoogleGenerativeAI(**gemni_params)

def get_openai_llm():
    OPENAI_BASE_URL = os.environ.get('PENAI_BASE_URL') or None
    OPENAI_MODEL_NAME = os.environ.get('OPENAI_MODEL_NAME') or 'gpt-4o'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    if not OPENAI_API_KEY:
        raise NotImplementedError("`OPENAI_API_KEY` is required!")

    openai_params = {
        "model": OPENAI_MODEL_NAME,
        "api_key":OPENAI_API_KEY
      }
    if OPENAI_BASE_URL:
        openai_params["base_url"] = OPENAI_BASE_URL
    
    return ChatOpenAI(**openai_params)

