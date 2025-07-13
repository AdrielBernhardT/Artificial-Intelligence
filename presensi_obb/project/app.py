from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    # Ambil daftar anak
    daftar_anak = ["Adriel Bernhard T", "Jonea Kristiawan", "Kevin Tanwiputra", "Kevin Jiovanni Kuslin"]

    # Ambil dari DB
    conn = sqlite3.connect("/home/abe-tanu/Documents/Code/Python/Artificial-Intelligence/presensi_obb/presensi.db")
    c = conn.cursor()
    c.execute("SELECT nama, waktu FROM presensi WHERE status='Hadir'")
    hasil = c.fetchall()
    conn.close()

    # Pisahkan
    nama_hadir = set(nama for nama, _ in hasil)
    tidak_hadir = [nama for nama in daftar_anak if nama not in nama_hadir]

    return render_template("index.html", hadir=hasil, tidak_hadir=tidak_hadir)

if __name__ == "__main__":
    app.run(debug=True)
