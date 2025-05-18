import sqlite3
from datetime import datetime
from pathlib import Path
import logging

# ----------------------------
# Setup Logging
# ----------------------------
LOG_DIR = Path(__file__).parent.parent / 'logs'
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR / 'usage_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ----------------------------
# Database Configuration
# ----------------------------
DB_PATH = Path(__file__).parent.parent / 'data' / 'usage.db'
DB_PATH.parent.mkdir(exist_ok=True)

# ----------------------------
# Main Usage Tracker Function
# ----------------------------
def track_usage(user_id: str, model_used: str, token_count: int) -> None:
    """
    Logs API usage into a SQLite database.

    Args:
        user_id (str): Unique user identifier (can be "anonymous" if unknown).
        model_used (str): Name of the AI model used (e.g., 'cohere').
        token_count (int): Number of tokens processed.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Ensure table exists
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usage (
                    user_id TEXT,
                    model TEXT,
                    tokens INTEGER,
                    timestamp TEXT
                )
            ''')

            # Insert usage log
            cursor.execute('''
                INSERT INTO usage (user_id, model, tokens, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (user_id, model_used, token_count, datetime.now().isoformat()))

            conn.commit()

    except Exception as e:
        logging.error(f"Failed to log usage: {str(e)}")
        raise RuntimeError("An error occurred while tracking usage.")
