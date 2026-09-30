import sqlite3

file = "app.db"

def connection():
    connection = sqlite3.connect(file)
    return connection

def create_tables():
    connection = connectition()
    connection.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, title TEXT, start_date TEXT, end_date TEXT)")
    connection.execute("CREATE TABLE IF NOT EXISTS participants (id INTEGER PRIMARY KEY, event_id INTEGER, name TEXT)")
    connection.execute("CREATE TABLE IF NOT EXISTS availability (participant_id INTEGER, slot_start TEXT)")
    connection.commit()
    connection.close()