from datetime import datetime
import sqlite3
from pathlib import Path

# Database configuration
DB_PATH = Path(__file__).parent.parent / 'data' / 'usage.db'
DB_PATH.parent.mkdir(exist_ok=True)  # Ensure directory exists

def track_usage(user_id: str, model_used: str, token_count: int):
    """
    Logs API usage to SQLite database
    Args:
        user_id: Unique identifier for the user
        model_used: Which model processed the request
        token_count: Number of tokens consumed
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Create table if not exists
        c.execute('''CREATE TABLE IF NOT EXISTS usage 
                    (user_id TEXT, model TEXT, tokens INTEGER, 
                     timestamp TEXT)''')
        
        # Insert record
        c.execute('''INSERT INTO usage VALUES (?, ?, ?, ?)''',
                 (user_id, model_used, token_count, 
                  datetime.now().isoformat()))
        
        conn.commit()
    except Exception as e:
        # Consider adding error logging here
        raise Exception(f"Usage tracking failed: {str(e)}")
    finally:
        conn.close()