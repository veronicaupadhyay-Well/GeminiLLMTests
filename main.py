import pandas as pd
# Use relative imports
from .client_setup import get_client # We will update get_client slightly
from .analysis_utils import get_followup_analysis
from .config_input import get_user_config # New module import

def test_api_connection(client, model_name):
    """A quick function to verify the client is working."""
    print("\n--- Testing API Connection ---")
    response = client.models.generate_content(
        model=model_name, contents="What is the capital of France? ")
    print(f"Test Response: {response.text.strip()}")
    print("------------------------------\n")

def run_analysis():
    """Main function to execute the data loading and analysis loop."""
    
    # 1. Get all configuration from user input
    config = get_user_config()
    if config is None:
        return

    # 2. Initialize Client

    client = get_client(api_key=config['api_key'])

    
    if client is None:
        print("Cannot run analysis without a valid client.")
        return

    test_api_connection(client, config['model_name'])
    
    # 3. Setup DataFrame and Loop Parameters
    df = config['df']
    analysis_col = config['analysis_col']
    new_col_name = config['new_col_name']
    
    df[new_col_name] = "" # Establish the new column 
    
    start = config['start_index']
    end = config['end_index']

    print(f"Starting analysis on rows {start} to {end}...")

    # 4. Iterate and Process 
    # Note: df.iloc[start:end] will select the desired range.
    for index in range(start, end):
        row = df.iloc[index]
        chat_transcript = row[analysis_col]
        
        answer = get_followup_analysis(
            client=client, 
            chat_transcript=chat_transcript, 
            model_name=config['model_name'],
            user_question=config['user_question'],
            system_prompt=config['system_prompt']
        )
        
        # Store the result
        df.at[index, new_col_name] = answer
        print(f"Index {index}: Result stored as '{answer}'")
        
        # Add error logging here if needed, based on the 'answer' string
        if answer.startswith('API_ERROR') or answer.startswith('BLOCKED'):
             print(f"!!! Error/Blocked response for Index {index}: {answer}")

    # 5. Final Output and Save
    print("\n--- Saving Results ---")
    df.to_csv(config['output_path'], index=False)
    print(f"Successfully saved output to: {config['output_path']}")

if __name__ == "__main__":
    run_analysis()