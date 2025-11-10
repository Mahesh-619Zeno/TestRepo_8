import os
import csv
import threading
import time
import logging
import sqlite3
from contextlib import closing

# Configure logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

DATA_FILE = "records.csv"
DB_FILE = "records.db"


def create_db():
    """Create a SQLite database and table if not already present."""
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                value REAL NOT NULL
            )
            """
        )
        conn.commit()
    logger.info("Database and table initialized.")


def read_csv():
    """Read CSV file and return a list of record dictionaries."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("id,name,value\n1,Sample,10.5\n")
        logger.warning(f"{DATA_FILE} not found — created a sample file.")

    rows = []
    try:
        with open(DATA_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    rows.append(
                        {
                            "name": row["name"].strip(),
                            "value": float(row["value"]),
                        }
                    )
                except (ValueError, KeyError) as e:
                    logger.warning(f"Skipping invalid row {row}: {e}")
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")

    logger.info(f"Loaded {len(rows)} records from {DATA_FILE}.")
    return rows


def save_to_db(rows):
    """Insert records into the SQLite database."""
    if not rows:
        logger.warning("No rows to insert into the database.")
        return

    with sqlite3.connect(DB_FILE) as conn, closing(conn.cursor()) as cur:
        for record in rows:
            cur.execute(
                "INSERT INTO records (name, value) VALUES (?, ?)",
                (record["name"], record["value"]),
            )
        conn.commit()
    logger.info(f"Inserted {len(rows)} records into {DB_FILE}.")


def cleanup_temp(delay=2):
    """Remove the temporary CSV file after a short delay."""
    time.sleep(delay)
    try:
        os.remove(DATA_FILE)
        logger.info(f"Temporary file {DATA_FILE} deleted.")
    except FileNotFoundError:
        logger.warning(f"File {DATA_FILE} already removed.")
    except Exception as e:
        logger.error(f"Error deleting {DATA_FILE}: {e}")


def background_cleanup():
    """Run cleanup in a background daemon thread."""
    thread = threading.Thread(target=cleanup_temp, daemon=True)
    thread.start()


def main():
    """Main execution flow."""
    try:
        create_db()
        rows = read_csv()
        save_to_db(rows)
        background_cleanup()
        logger.info("Data processing completed successfully.")
        input("Press Enter to exit...")
    except Exception as e:
        logger.exception(f"Unhandled error during execution: {e}")


if __name__ == "__main__":
    main()
