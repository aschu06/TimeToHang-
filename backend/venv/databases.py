import sqlite3

file = "app.db"

def get_database():
    database = sqlite3.connect(file)
    return database

def create_tables():
    database = get_database()
    database.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, title TEXT, start_date TEXT, end_date TEXT)")
    database.execute("CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY, event_id INTEGER, name TEXT)")
    database.execute("CREATE TABLE IF NOT EXISTS availability (person_id INTEGER, start_time TEXT, end_time TEXT)")
    database.commit()
    database.close()