# This module will handle all user interaction and return a single configuration dictionary.

import pandas as pd
import os
from typing import Dict, Any

def get_user_config() -> Dict[str, Any]:
    """Gathers all necessary configuration and parameters from the user."""
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("--- Gemini Analysis Parameters ---")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    # 1. API Key Input (Will be used to set environment variable)
    # NOTE: It's still generally better to use the OS environment variable, 
    # but we can take it as input if preferred.
    api_key_input = input("Please input your Gemini API Key: ")
    
    # 2. Dataset Path and Column Info
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    data_path = input("Please input the path-link to the dataset (e.g., /path/to/data.csv): ")
    try:
        df = pd.read_csv(data_path)
        print(" ")
        print(" ")
        print(f"\n✅ Dataset loaded successfully.")
        print(" ")
        print(f"Total Rows: {len(df)}")
        print(" ")
        print(f"Column Names:")
        print(f" {list(df.columns)}")
        print(" ")
        print("--------------------------- ")
        print(" ")
    except FileNotFoundError:
        print(f"FATAL ERROR: File not found at path: {data_path}")
        return None
    
    analysis_col = input("Please input the column that holds data that is to be analyzed: ")
    if analysis_col not in df.columns:
        print(f"FATAL ERROR: Column '{analysis_col}' not found in dataset.")
        return None

    # 3. Row Indices
    while True:
        try:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            start_index = int(input("What is the index of the first row you'd like analyzed?: "))
            end_index = int(input("What is the index of the last row you'd like analyzed?: "))
            if 0 <= start_index < end_index <= len(df):
                break
            else:
                print(f"Indices must be valid (0 <= start < end <= {len(df)}). Try again.")
        except ValueError:
            print("Please input valid integers for the indices.")

    # 4. Prompt and Output Column Name
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    user_question = input("\nPlease paste the USER_QUESTION (e.g., Analyze the following chat messages...): ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    system_prompt = input("Please paste the SYSTEM_PROMPT (e.g., You are a specialized text analysis system...): ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    new_col_name = input("Please pick a name for the new column that will hold Gemini's answers: ")

    # 5. Output Configuration
    output_dir = "/Users/veronica.upadhyay/welllabs/data/operations-analytics/Gemini_Usages/GeminiOuputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")    
    output_filename = input("What name would you like the output dataset to be? (e.g., analysis_results.csv): ")
    output_path = os.path.join(output_dir, output_filename)
    
    # 6. Final Review and Run Check
    print("----------------------------- ")
    print("----------------------------- ")
    print("----------------------------- ")
    print("✅ Configuration Summary ✅")
    print(f"Path Link: {data_path}")
    print(f"Column to be analyzed: {analysis_col}")
    print(f"USER_QUESTION: {user_question}")
    print(f"SYSTEM PROMPT: {system_prompt}")
    print(f"New Column Name: {new_col_name}")
    print(f"Output Path: {output_path}")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("----------------------------- ")
    print("----------------------------- ")
    print("----------------------------- ")


    ready = input("\nAre you ready to run? (Yes/No): ").lower().strip()
    if ready != 'yes':
        print("Run cancelled by user.")
        return None

    # Return the full configuration, including the pre-loaded DataFrame
    return {
        'api_key': api_key_input,
        'df': df,
        'analysis_col': analysis_col,
        'start_index': start_index,
        'end_index': end_index,
        'user_question': user_question,
        'system_prompt': system_prompt,
        'new_col_name': new_col_name,
        'output_path': output_path,
        'model_name': 'gemini-2.5-flash' # Fixed model for now
    }