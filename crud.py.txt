import sqlite3
from database import connect_db

# ======= Doctor Functions =======
def add_doctor(name, specialization):
    """Add a doctor to the database"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO doctor (name, specialization) VALUES (?, ?)",
        (name, specialization)
    )
    conn.commit()
    conn.close()
    print(f"Doctor {name} added successfully!")

# ======= Patient Functions =======
def add_patient(name, email):
    """Add a patient to the database"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO patient (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    conn.close()
    print(f"Patient {name} added successfully!")

# ======= Appointment Functions =======
def add_appointment(patient_id, doctor_id, date, time):
    """Add an appointment linking patient and doctor"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointment (patient_id, doctor_id, date, time) VALUES (?, ?, ?, ?)",
        (patient_id, doctor_id, date, time)
    )
    conn.commit()
    conn.close()
    print("Appointment added successfully!")

def view_appointments():
    """Return a list of all appointments with patient and doctor names"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT appointment.id, patient.name, doctor.name, appointment.date, appointment.time
        FROM appointment
        JOIN patient ON appointment.patient_id = patient.id
        JOIN doctor ON appointment.doctor_id = doctor.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

