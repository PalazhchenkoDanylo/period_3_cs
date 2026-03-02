from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ---------- Validation logic ----------
def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    number_started = False

    for c in s:
        if not c.isalnum():
            return False

        if c.isdigit():
            if not number_started:
                number_started = True
                if c == "0":
                    return False
        else:
            if number_started:
                return False

    return True


# ---------- Database helpers ----------
def get_db_connection():
    conn = sqlite3.connect("plates.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate TEXT UNIQUE NOT NULL
        );
    """)
    conn.commit()
    conn.close()


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def index():
    message = None

    if request.method == "POST":
        plate = request.form["plate"].upper()

        if is_valid(plate):
            try:
                conn = get_db_connection()
                conn.execute("INSERT INTO plates (plate) VALUES (?)", (plate,))
                conn.commit()
                conn.close()
                message = f"✅ Plate {plate} added!"
            except sqlite3.IntegrityError:
                message = f"⚠️ Plate {plate} already exists!"
        else:
            message = "❌ Invalid plate format!"

    conn = get_db_connection()
    plates = conn.execute("SELECT plate FROM plates").fetchall()
    conn.close()

    return render_template("index.html", plates=plates, message=message)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)