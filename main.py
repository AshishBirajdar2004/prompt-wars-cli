# main.py
import argparse
import sys
from validator import validate_prompt
from core import generate_output
from logger import save_as_html # <-- Import our save as html function

def main():
    """Main function to run the CLI tool."""

    print("--- Welcome to the Prompt Wars Submission Tool ---")

    # --- GET PARTICIPANT INFO ---
    participant_name = input("👤 Please enter the participant's name: ").strip()
    if not participant_name:
        print("Error: Name cannot be empty. Exiting.")
        return

    assigned_keyword = input(f"🔑 Please enter the keyword assigned to {participant_name}: ").strip()
    if not assigned_keyword:
        print("Error: Keyword cannot be empty. Exiting.")
        return
    
    print("-" * 20)
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