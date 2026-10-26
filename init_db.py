
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")

cursor.execute("""
INSERT OR IGNORE INTO students
(id, name, age, course, marks)
VALUES
(1, 'Amulya', 19, 'CSE', 95.5)
""")

conn.commit()
conn.close()

print("Database created successfully!")
