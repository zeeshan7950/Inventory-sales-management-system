import sqlite3
import os

# -------------------------------
# 1️⃣ Database path setup
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # current folder
DB_PATH = os.path.join(BASE_DIR, "inventory.db")

# -------------------------------
# 2️⃣ Create / Connect to database
# -------------------------------
def get_connection():
    """Return a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)

# -------------------------------
# 3️⃣ Initialize database tables
# -------------------------------
def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    """)

    # Sales table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quantity_sold INTEGER NOT NULL,
        sale_date TEXT NOT NULL,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

# -------------------------------
# 4️⃣ Test run
# -------------------------------
if __name__ == "__main__":
    initialize_database()
