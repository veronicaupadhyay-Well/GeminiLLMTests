import os
from google import genai
from google.genai.errors import APIError
from typing import Optional, Any # Add typing for clarity

MODEL_NAME = "gemini-2.5-flash" 

# --- CHANGE IS HERE ---
def get_client(api_key: str) -> Optional[genai.Client]:
    """
    Initializes and returns the Gemini client using the key passed to it.
    """
    
    API_KEY = api_key # Use the key passed in from main.py

    if not API_KEY:
        print("FATAL ERROR: API Key not provided.")
        return None

    try:
        client = genai.Client(api_key=API_KEY)
        # You can optionally run a quick test here if needed
        print("Gemini client initialized successfully.")
        return client
    except Exception as e:
        print(f"FATAL ERROR: Could not initialize Gemini client. Error: {e}")
        return None