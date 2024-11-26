import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close()


def createTable():
    conn = sql.connect("autoconcimiento.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE strategic_plan (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP,
    status TEXT DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
    """)
    print("Tabla creada")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    createTable()