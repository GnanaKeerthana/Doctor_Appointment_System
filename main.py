from database import create_tables
from gui import start_gui

def main():
    # Create database tables (runs only once, safe to run multiple times)
    create_tables()

    # Start the GUI
    start_gui()

if __name__ == "__main__":
    main()

