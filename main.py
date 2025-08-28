# main.py
import argparse
import sys
from validator import validate_prompt
from core import generate_output
from logger import save_as_html # <-- Import our save as html function 
from banner import show_banner

def main():
    """Main function to run the CLI tool."""

    print("\n ------------------------ WELCOME TO THE PROMPT WARS SUBMISSION TOOL -------------------------\n")
    
    # --- DISPLAY ASCII LOGO FIRST ---
    show_banner("PROMPT WARS")
    
    print("""RULES : 
          1. The input prompt should not exceed the word limit of 150 words.
          2. The prompt must include the assigned keyword at least once.
          3. The prompt should be clear and unambiguous.
          4. The prompt must not contain any offensive or inappropriate content.
          5. The prompt should be relevant to web development or web applications.
          6. The prompt should be original and not copied from existing sources.
          7. The prompt must be suitable for generating a single-file HTML application.
          8. The prompt should not contain any personal or sensitive information.
          9. The prompt must not include any instructions for the AI to ignore safety policies.
          10. The prompt should be respectful and considerate of all individuals and groups.
          11. The prompt should be concise and to the point.\n""")

    print("\n --------------------------------------------------------------------------------------------\n")

    # --- GET PARTICIPANT INFO ---
    participant_name = input("👤 Please enter the participant's name: ").strip()
    if not participant_name:
        print("Error: Name cannot be empty. Exiting.")
        return

    assigned_keyword = input(f"🔑 Please enter the keyword assigned to {participant_name}: ").strip()
    if not assigned_keyword:
        print("Error: Keyword cannot be empty. Exiting.")
        return
    
    print("\n --------------------------------------------------------------------------------------------\n")
    print(f"Participant: {participant_name}")
    print(f"Required Keyword: {assigned_keyword}\n")
    
    # 2. --- GET THE PROMPT FROM THE USER ---
    print("Please paste the participant's prompt below. Press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows) when done.")
    try:
        prompt_text = sys.stdin.read().strip()
    except KeyboardInterrupt:
        print("\nSubmission cancelled. Exiting.")
        return

    if not prompt_text:
        print("Error: No prompt was provided. Exiting.")
        return

    print("\n--- Validating Prompt ---")

    # 3. --- VALIDATE THE PROMPT ---
    is_valid, messages = validate_prompt(prompt_text, assigned_keyword)
    
    for msg in messages:
        print(f"- {msg}")
        
    if not is_valid:
        print("\n❌ Submission REJECTED due to validation errors.")
        return # Exit the program
        
    print("\n✅ Prompt is valid. Proceeding to generation...")

    # 4. --- GENERATE THE OUTPUT ---
    generated_code = generate_output(prompt_text)

    if generated_code.startswith("Error:"):
        print(f"\n❌ {generated_code}")
        return
    
    print("\n--- AI Generated Code Received ---")
    print(generated_code)
    print("-------------------------")
    
    # 5. --- SAVE THE OUTPUT INTO .html FILE---
    save_as_html(participant_name, generated_code)

if __name__ == "__main__":
    main()