import os
import sqlite3
import json
import threading
import time
import logging

# --------------------------------------
# System Logging Configuration (NEW FEATURE)
# --------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("inventory.log"),  # Logs also stored in file
        logging.StreamHandler()                # Also visible in console
    ]
)
logger = logging.getLogger("inventory_manager")

# --------------------------------------
# File and Database Configuration
# --------------------------------------
DB_FILE = "inventory.db"
DATA_FILE = "items.json"

# --------------------------------------
# Database Initialization
# --------------------------------------
def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)"
    )
    conn.commit()
    conn.close()
    logger.info("Database initialized successfully.")

# --------------------------------------
# Product Data Management (NEW FEATURE)
# Load product data from a JSON file
# --------------------------------------
def load_items():
    """
    Loads product data from a JSON file.
    If the file doesn't exist, creates one with sample data.
    """
    if not os.path.exists(DATA_FILE):
        sample_data = {
            "items": [
                {"name": "Apple", "quantity": 10},
                {"name": "Banana", "quantity": 20}
            ]
        }
        with open(DATA_FILE, "w") as f:
            json.dump(sample_data, f, indent=4)
        logger.info(f"Sample product data file '{DATA_FILE}' created.")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        logger.info(f"Loaded product data from '{DATA_FILE}' successfully.")
    return data["items"]

# --------------------------------------
# Save Data to Database
# --------------------------------------
def save_to_db(items):
    """Saves product items into the database."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    for item in items:
        cur.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (item['name'], item['quantity']))
        logger.info(f"Inserted item into DB: {item['name']} (Qty: {item['quantity']})")
    conn.commit()
    conn.close()
    logger.info(f"{len(items)} items successfully saved to the database.")

# --------------------------------------
# Stock Update
# --------------------------------------
def update_stock():
    """Decreases the quantity of 'Apple' by 1 in the database."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("UPDATE items SET quantity = quantity - 1 WHERE name = 'Apple'")
    conn.commit()
    conn.close()
    logger.info("Stock updated for 'Apple'.")

# --------------------------------------
# Background Stock Monitor
# --------------------------------------
def background_stock_monitor():
    """Continuously updates stock in a background thread."""
    def monitor():
        while True:
            try:
                update_stock()
                logger.info("Background stock update completed.")
                time.sleep(2)
            except Exception as e:
                logger.warning(f"Stock update failed: {e}")
                time.sleep(3)

    t = threading.Thread(target=monitor, daemon=True)
    t.start()
    logger.info("Background stock monitoring thread started.")

# --------------------------------------
# Main Entry Point
# --------------------------------------
def main():
    logger.info("=== Starting Inventory Management System ===")

    init_db()
    items = load_items()  # Product Data Management feature
    save_to_db(items)
    background_stock_monitor()

    logger.info("Inventory system started and running.")
    time.sleep(8)
    logger.info("Inventory monitoring finished.")

if __name__ == "__main__":
    main()
