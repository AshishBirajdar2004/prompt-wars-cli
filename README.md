# Prompt Wars CLI Tool

A secure, configurable CLI tool designed to run a "Prompt Wars" competition. Participants submit prompts to an LLM to generate self-contained HTML/CSS/JS web applications based on a given theme. The tool validates submissions against a set of rules and logs the results for judging.

---

## Features

-   **Interactive Submission:** Asks for participant name and a unique keyword to prevent cheating.
-   **Robust Validation:** Enforces rules before calling the API:
    -   Word Count Limit
    -   Required Keyword Inclusion
    -   Restricted Phrase Detection (prevents meta-prompting)
-   **Secure API Key Handling:** Uses environment variables to keep API keys safe.
-   **Code Generation:** Instructs the Gemini LLM to generate a single, self-contained HTML file.
-   **Automatic Logging:** Saves the participant's prompt and the generated code to a `submissions/submission_username.html` file for auditing and judging.

---

## How to Get the Application

This repository uses **GitHub Actions** to automatically build and package the application for Windows, macOS, and Linux.

1.  Navigate to the **Actions** tab of this repository.
2.  In the left sidebar, click on the **"Build and Package Application"** workflow.
3.  Click the **"Run workflow"** dropdown button.
4.  Enter your **Gemini API Key** in the provided text field.
5.  Click the green **"Run workflow"** button.

Once the workflow is complete, you can download the packaged application (executable + runner script) from the **Artifacts** section of the workflow summary page.

---

## How to Use

The downloaded package contains the main executable (`prompt-wars.exe` or `prompt-wars`) and a runner script (`run.bat` or `run.sh`).

1.  Extract the downloaded zip file.
2.  On **Windows**, double-click `run.bat`.
3.  On **macOS or Linux**, open a terminal in the folder and run `./run.sh`.

The script will launch the tool, and you can follow the on-screen instructions to submit a prompt.

---

## Local Development Setup

If you wish to run the tool from the source code:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/prompt-wars-cli.git](https://github.com/your-username/prompt-wars-cli.git)
    cd prompt-wars-cli
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root directory and add your API key:
    ```
    GEMINI_API_KEY="your_api_key_here"
    ```

5.  **Run the application:**
    ```bash
    python main.py
    ```
