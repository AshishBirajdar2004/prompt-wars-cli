# validator.py

# --- Rule Definitions ---
# These can be easily modified to change the event rules.

WORD_LIMIT = 150

# A list of phrases that are not allowed (meta-prompting).
RESTRICTED_PHRASES = [
    "write a prompt", "create a prompt", "generate a prompt",
    "improve this prompt", "better prompt", "prompt for me",
    "rewrite this prompt", "give me a prompt"
]

# Keywords to check for theme relevance. The prompt must contain at least one.
THEME_KEYWORDS = [
    "defense", "military", "army", "naval", "warfare", "cybersecurity",
    "surveillance", "weapon", "soldier", "strategy", "tactics", "fortress",
    "logistics", "intelligence", "espionage", "armored", "artillery"
]


def check_word_count(prompt: str) -> (bool, str):
    """Checks if the prompt is within the word limit."""
    word_count = len(prompt.split())
    if word_count > WORD_LIMIT:
        return False, f"Validation FAILED: Prompt exceeds {WORD_LIMIT} words (found {word_count})."
    return True, f"Word count is OK ({word_count} words)."

def check_keyword_enforcement(prompt: str, keyword: str) -> (bool, str):
    """Checks if the required unique keyword is in the prompt."""
    # We check in lowercase to make it case-insensitive.
    if keyword.lower() not in prompt.lower():
        return False, f"Validation FAILED: Required keyword '{keyword}' is missing."
    return True, f"Required keyword '{keyword}' found."

def check_restricted_phrases(prompt: str) -> (bool, str):
    """Checks for forbidden meta-prompting phrases."""
    for phrase in RESTRICTED_PHRASES:
        if phrase in prompt.lower():
            return False, f"Validation FAILED: Prompt contains a restricted phrase: '{phrase}'."
    return True, "No restricted phrases found."

def check_theme_relevance(prompt: str) -> (bool, str):
    """Checks if the prompt seems relevant to the theme. This is a warning, not a failure."""
    for theme_word in THEME_KEYWORDS:
        if theme_word in prompt.lower():
            return True, "Theme relevance check passed."
    # This is a soft check, so we return True but with a warning message.
    return True, "WARNING: Prompt may not be relevant to the 'Defense' theme. Please review."

def validate_prompt(prompt: str, unique_keyword: str) -> (bool, list[str]):
    """
    Runs all validation checks on the prompt.
    Returns a boolean indicating overall validity and a list of messages.
    """
    messages = []
    is_valid = True

    # Run critical checks first. If any of these fail, we stop.
    checks = [
        (check_word_count, (prompt,)),
        (check_keyword_enforcement, (prompt, unique_keyword)),
        (check_restricted_phrases, (prompt,))
    ]

    for check_func, args in checks:
        success, msg = check_func(*args)
        messages.append(msg)
        if not success:
            is_valid = False
            return is_valid, messages # Stop on the first critical failure

    # Run non-critical checks (warnings)
    success, msg = check_theme_relevance(prompt)
    messages.append(msg)

    return is_valid, messages