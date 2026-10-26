
from flask import Flask, render_template, abort
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return """
    <h2>Student Information System</h2>
    <p>To view student details, open:</p>
    <a href="/student/1">View Student 1</a>
    """


@app.route("/student/<int:student_id>")
def get_student(student_id):
    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:
        abort(404)

    return render_template("student.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)
