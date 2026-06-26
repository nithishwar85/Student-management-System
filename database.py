import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(

roll_no INTEGER PRIMARY KEY,
name TEXT,
department TEXT,
cgpa REAL

)
""")

connection.commit()
