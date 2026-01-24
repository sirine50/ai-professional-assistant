import sqlite3

DATABASE_NAME = "app.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)

    #this so the data in the shape of a dictenory
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # this one let's us write our sql request in clear way aka string
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            role TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    #to execute the sql requests
    conn.commit()
    #to cut the connection
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized!")