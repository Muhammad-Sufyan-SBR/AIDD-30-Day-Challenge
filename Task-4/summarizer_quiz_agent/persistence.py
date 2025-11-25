import os
import json
from datetime import datetime

SESSION_FILE = "user_session.json"

def save_session(data: dict):
    """Saves the user session data to a JSON file."""
    try:
        # Add timestamp
        data["last_updated"] = datetime.now().isoformat()
        with open(SESSION_FILE, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving session: {e}")
        return False

def load_session():
    """Loads the user session data from a JSON file."""
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading session: {e}")
            return {}
    return {}

def clear_session():
    """Clears the stored session file."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
