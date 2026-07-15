from flask import Flask, request, redirect, render_template, jsonify
import sqlite3
import string
import random

app = Flask(__name__)
DATABASE = "urls.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten_url():
    original_url = request.form.get("url") or (
        request.json.get("url") if request.is_json else None
    )

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    if not original_url.startswith(("http://", "https://")):
        original_url = "https://" + original_url

    conn = sqlite3.connect(DATABASE)

    while True:
        short_code = generate_short_code()
        existing = conn.execute(
            "SELECT id FROM urls WHERE short_code = ?", (short_code,)
        ).fetchone()
        if not existing:
            break

    conn.execute(
        "INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
        (original_url, short_code)
    )
    conn.commit()
    conn.close()

    short_url = request.host_url + short_code

    if request.is_json:
        return jsonify({
            "original_url": original_url,
            "short_code": short_code,
            "short_url": short_url
        }), 201

    return render_template(
        "index.html",
        original_url=original_url,
        short_url=short_url
    )


@app.route("/<short_code>")
def redirect_url(short_code):
    conn = sqlite3.connect(DATABASE)
    result = conn.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()
    conn.close()

    if result:
        return redirect(result[0])

    return "Short URL not found", 404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
