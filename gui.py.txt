import tkinter as tk
from tkinter import messagebox
from crud import add_doctor, add_patient, add_appointment, view_appointments

def start_gui():
    """Start the main GUI window"""
    window = tk.Tk()
    window.title("Doctor Appointment System")
    window.geometry("500x400")

    # Welcome Label
    label = tk.Label(window, text="Welcome to Doctor Appointment System", font=("Arial", 14))
    label.pack(pady=20)

    # ======= Functions for Buttons =======

    def add_doctor_gui():
        """Popup to add a doctor"""
        popup = tk.Toplevel()
        popup.title("Add Doctor")
        tk.Label(popup, text="Doctor Name:").pack()
        name_entry = tk.Entry(popup)
        name_entry.pack()
        tk.Label(popup, text="Specialization:").pack()
        spec_entry = tk.Entry(popup)
        spec_entry.pack()

        def submit_doctor():
            name = name_entry.get()
            spec = spec_entry.get()
            if name and spec:
                add_doctor(name, spec)
                messagebox.showinfo("Success", f"Doctor {name} added!")
                popup.destroy()
            else:
                messagebox.showerror("Error", "Please fill all fields")

        tk.Button(popup, text="Submit", command=submit_doctor).pack(pady=10)

    def add_patient_gui():
        """Popup to add a patient"""
        popup = tk.Toplevel()
        popup.title("Add Patient")
        tk.Label(popup, text="Patient Name:").pack()
        name_entry = tk.Entry(popup)
        name_entry.pack()
        tk.Label(popup, text="Email:").pack()
        email_entry = tk.Entry(popup)
        email_entry.pack()

        def submit_patient():
            name = name_entry.get()
            email = email_entry.get()
            if name and email:
                add_patient(name, email)
                messagebox.showinfo("Success", f"Patient {name} added!")
                popup.destroy()
            else:
                messagebox.showerror("Error", "Please fill all fields")

        tk.Button(popup, text="Submit", command=submit_patient).pack(pady=10)

    def add_appointment_gui():
        """Popup to add an appointment"""
        popup = tk.Toplevel()
        popup.title("Add Appointment")
        tk.Label(popup, text="Patient ID:").pack()
        patient_entry = tk.Entry(popup)
        patient_entry.pack()
        tk.Label(popup, text="Doctor ID:").pack()
        doctor_entry = tk.Entry(popup)
        doctor_entry.pack()
        tk.Label(popup, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(popup)
        date_entry.pack()
        tk.Label(popup, text="Time (HH:MM):").pack()
        time_entry = tk.Entry(popup)
        time_entry.pack()

        def submit_appointment():
            pid = patient_entry.get()
            did = doctor_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            if pid and did and date and time:
                add_appointment(pid, did, date, time)
                messagebox.showinfo("Success", "Appointment added!")
                popup.destroy()
            else:
                messagebox.showerror("Error", "Please fill all fields")

        tk.Button(popup, text="Submit", command=submit_appointment).pack(pady=10)

    def view_appointments_gui():
        """Popup to view all appointments"""
        popup = tk.Toplevel()
        popup.title("View Appointments")
        appointments = view_appointments()
        if not appointments:
            tk.Label(popup, text="No appointments found").pack()
        else:
            for appt in appointments:
                text = f"ID:{appt[0]} | Patient:{appt[1]} | Doctor:{appt[2]} | Date:{appt[3]} | Time:{appt[4]}"
                tk.Label(popup, text=text).pack()

    # ======= Buttons on Main Window =======
    tk.Button(window, text="Add Doctor", width=25, command=add_doctor_gui).pack(pady=5)
    tk.Button(window, text="Add Patient", width=25, command=add_patient_gui).pack(pady=5)
    tk.Button(window, text="Add Appointment", width=25, command=add_appointment_gui).pack(pady=5)
    tk.Button(window, text="View Appointments", width=25, command=view_appointments_gui).pack(pady=5)
    tk.Button(window, text="Exit", width=25, command=window.destroy).pack(pady=20)

    window.mainloop()

