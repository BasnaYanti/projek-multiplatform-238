from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(name)

def get_db():
    return sqlite3.connect("identitas.db")

def init_db():
    con = get_db()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS identitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            nim TEXT,
            prodi TEXT,
            fakultas TEXT
        )
    """)
    con.commit()
    con.close()

init_db()

@app.route("/")
def index():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM identitas")
    data = cur.fetchall()
    con.close()
    return render_template("index.html", data=data)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nama = request.form["nama"]
        nim = request.form["nim"]
        prodi = request.form["prodi"]
        fakultas = request.form["fakultas"]

        con = get_db()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO identitas (nama, nim, prodi, fakultas) VALUES (?,?,?,?)",
            (nama, nim, prodi, fakultas)
        )
        con.commit()
        con.close()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    con = get_db()
    cur = con.cursor()

    if request.method == "POST":
        nama = request.form["nama"]
        nim = request.form["nim"]
        prodi = request.form["prodi"]
        fakultas = request.form["fakultas"]

        cur.execute(
            "UPDATE identitas SET nama=?, nim=?, prodi=?, fakultas=? WHERE id=?",
            (nama, nim, prodi, fakultas, id)
        )
        con.commit()
        con.close()
        return redirect("/")

    cur.execute("SELECT * FROM identitas WHERE id=?", (id,))
    data = cur.fetchone()
    con.close()
    return render_template("edit.html", data=data)

@app.route("/delete/<int:id>")
def delete(id):
    con = get_db()
    cur = con.cursor()
    cur.execute("DELETE FROM identitas WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect("/")

if name == "main":
    app.run(host="0.0.0.0", port=1912, debug=True)