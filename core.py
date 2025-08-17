# core.py

import os
import sys
from dotenv import load_dotenv
from google import genai
from validator import validate_prompt # <-- Import our validator function

# --- Securely Load API Key ---
load_dotenv() # Load variables from the .env file
API_KEY = os.getenv("GEMINI_API_KEY") # Get the key from the environment
if not API_KEY:
    print("❌ Error: GEMINI_API_KEY not found.")
    print("Please create a .env file and add your API key to it.")
    sys.exit(1) # Exit the program if the key is missing

# --- Configuration ---
try:
    client = genai.Client(api_key=API_KEY)  # unified client object
except Exception as e:
    print(f"Error configuring API: {e}")
    sys.exit(1)

def generate_output(prompt: str) -> str:
    """
    Sends a user's prompt, prefixed with a system instruction for code generation,
    to the LLM and returns the generated code.
    """
    
    # A primer to instruct the AI to generate a single, self-contained HTML file.
    code_generation_primer = (
        "You are an expert web developer. Your task is to generate a complete, single-file HTML application. "
        "The HTML file must include all necessary CSS in a <style> tag and all JavaScript in a <script> tag. "
        "Do not use any external libraries or assets unless specifically asked. "
        "Your response should be ONLY the raw HTML code. Do not include any explanations, comments, or markdown ticks like '```html'. "
        "Just provide the code itself, starting with <!DOCTYPE html>."
        "\n\nHere is the user's request:\n---\n"
    )
    
    full_prompt = code_generation_primer + prompt

    try:
        print("\n⏳ Instructing the AI to generate the web application code...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
            config={
                "temperature": 0.4,
                "top_p": 1,
                "top_k": 32,
                "max_output_tokens": 8192,
            },
        )

        if not response or not response.candidates:
            return "Error: Model response was empty or blocked. The prompt might violate safety policies."

        return response.text
    except Exception as e:
        return f"An error occurred during generation: {e}"