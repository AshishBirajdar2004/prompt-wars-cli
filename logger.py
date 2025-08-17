# logger.py
import csv
import re
from datetime import datetime
import os

# --- Saves Generated Output To A CSV File ---
# !--- Dropped this idea ---
LOG_FILE = 'submissions.csv'
FIELDNAMES = ['timestamp', 'participant_name', 'assigned_keyword', 'prompt_text', 'generated_output']

def log_submission(name: str, keyword: str, prompt: str, output: str):
    """Appends a new submission to the CSV log file."""
    
    # Check if the file exists to write headers
    file_exists = os.path.isfile(LOG_FILE)
    
    try:
        with open(LOG_FILE, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            
            if not file_exists:
                writer.writeheader() # Write header only if file is new
                
            writer.writerow({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'participant_name': name,
                'assigned_keyword': keyword,
                'prompt_text': prompt,
                'generated_output': output
            })
        print(f"✅ Submission for '{name}' successfully logged to {LOG_FILE}.")
    except Exception as e:
        print(f"❌ Error: Could not write to log file. {e}")

# --- Saves Generated Output Directly Into HTML File ---
def save_as_html(participant_name: str, html_code: str):
    """Saves the generated code to a dedicated HTML file."""
    
    # Create a submissions directory if it doesn't exist
    if not os.path.exists('submissions'):
        os.makedirs('submissions')
    
    # Sanitize the participant's name to create a valid filename
    sane_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', participant_name).lower()
    filename = f"submissions/submission_{sane_name}.html"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_code)
        print(f"✅ Web app saved successfully as '{filename}'.")
    except Exception as e:
        print(f"❌ Error: Could not save the HTML file. {e}")