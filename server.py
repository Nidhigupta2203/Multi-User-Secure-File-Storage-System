import os
import sqlite3
from datetime import timedelta

from flask import (
    Flask, render_template, request,
    redirect, url_for, session,
    send_from_directory
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

# ================== APP SETUP ==================

app = Flask(__name__)
app.secret_key = "supersecretkey"  # move to env variable in production

# Session timeout (auto logout)
app.permanent_session_lifetime = timedelta(minutes=15)

# ================== CONFIG ==================

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf", "txt"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================== DATABASE ==================

def get_db():
    return sqlite3.connect("users.db")

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ================== HELPERS ==================

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# ================== AUTH ROUTES ==================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            session.permanent = True
            session["user"] = username
            os.makedirs(os.path.join(UPLOAD_FOLDER, username), exist_ok=True)
            return redirect(url_for("index"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            conn.close()

            os.makedirs(os.path.join(UPLOAD_FOLDER, username), exist_ok=True)
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            return "Username already exists. <a href='/signup'>Try again</a>"

    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ================== FILE MANAGER ==================

@app.route("/")
def index():
    if "user" not in session:
        return redirect(url_for("login"))

    user_folder = os.path.join(UPLOAD_FOLDER, session["user"])
    os.makedirs(user_folder, exist_ok=True)

    files = os.listdir(user_folder)
    return render_template("index.html", files=files)


@app.route("/upload", methods=["POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("login"))

    if "file" not in request.files:
        return "No file selected <a href='/'>Back</a>"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected <a href='/'>Back</a>"

    if not allowed_file(file.filename):
        return "File type not allowed <a href='/'>Back</a>"

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, session["user"], filename)

    if os.path.exists(file_path):
        return "File already exists <a href='/'>Back</a>"

    file.save(file_path)
    return redirect(url_for("index"))


@app.route("/download/<filename>")
def download(filename):
    if "user" not in session:
        return redirect(url_for("login"))

    filename = secure_filename(filename)
    return send_from_directory(
        os.path.join(UPLOAD_FOLDER, session["user"]),
        filename,
        as_attachment=True
    )


@app.route("/delete/<filename>")
def delete(filename):
    if "user" not in session:
        return redirect(url_for("login"))

    filename = secure_filename(filename)
    file_path = os.path.join(UPLOAD_FOLDER, session["user"], filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for("index"))

# ================== RUN SERVER ==================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
