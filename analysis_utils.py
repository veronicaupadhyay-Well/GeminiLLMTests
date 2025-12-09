import pandas as pd
from google.genai.errors import APIError 
from typing import Any, Dict

def get_followup_analysis(
    client: Any, 
    chat_transcript: str, 
    model_name: str,
    user_question: str, 
    system_prompt: str
) -> str:
    """
    Calls the Gemini API to analyze a single chat transcript.
    Parameters are dynamic based on user input.
    """
    user_content = f"{user_question}\nChat Messages:\n{chat_transcript}"
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=user_content, 
            config=dict(
                temperature=0.0,
                system_instruction=system_prompt
            )
        )
        
        # --- ROBUST RESPONSE HANDLING ---
        if response.text is not None and response.text.strip():
            return response.text.strip().upper()
        
        # Handle cases where the response is blocked or empty
        reason = 'NO_CANDIDATES'
        block_reason = getattr(getattr(response, 'prompt_feedback', None), 'block_reason', None)
        
        if block_reason and block_reason.name != "BLOCK_REASON_UNSPECIFIED":
            reason = block_reason.name
        elif response.candidates and response.candidates[0].finish_reason.name:
            reason = response.candidates[0].finish_reason.name

        return f"BLOCKED/{reason}" 

    except APIError as e:
        # print(f"API Error: Status {e.status_code}") # Moved printing to main loop
        return f'API_ERROR_{e.status_code}'
    except Exception as e:
        # print(f"General/Unexpected Error: {e}") # Moved printing to main loop
        return 'UNEXPECTED_ERROR'

# NOTE: The separate load_data function is removed as config_input.py handles loading.