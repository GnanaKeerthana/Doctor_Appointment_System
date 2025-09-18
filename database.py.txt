import sqlite3

def connect_db():
    """Connect to SQLite database (creates file if not exists)."""
    conn = sqlite3.connect("appointments.db")
    return conn

def create_tables():
    """Create tables for doctors, patients, and appointments."""
    conn = connect_db()
    cursor = conn.cursor()

    # Doctor table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL
    )
    """)

    # Patient table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT
    )
    """)

    # Appointment table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        date TEXT,
        time TEXT,
        FOREIGN KEY(patient_id) REFERENCES patient(id),
        FOREIGN KEY(doctor_id) REFERENCES doctor(id)
    )
    """)

    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_tables()
