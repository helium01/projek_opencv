import mysql.connector
from PIL import Image, ImageTk
import tkinter as tk


# Fungsi untuk membuat koneksi ke database MySQL
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="nama_database"
    )
    return conn


# Fungsi untuk mengeksekusi query SQL dan mengambil data gambar dari tabel di database MySQL
def fetch_data():
    # Buat koneksi ke database MySQL
    conn = create_connection()

    # Buat cursor
    cursor = conn.cursor()

    # Eksekusi query SQL
    cursor.execute("SELECT nama, gambar FROM nama_tabel")

    # Ambil data dari cursor
    data = cursor.fetchall()

    # Tampilkan data di antarmuka pengguna
    for i, row in enumerate(data):
        # Menampilkan nama pada kolom pertama
        e1 = tk.Entry(root, width=20, fg='blue')
        e1.grid(row=i, column=0)
        e1.insert(tk.END, row[0])

        # Menampilkan gambar pada kolom kedua
        photo = ImageTk.PhotoImage(Image.open(row[1]))
        label = tk.Label(root, image=photo)
        label.image = photo
        label.grid(row=i, column=1)

    # Tutup koneksi ke database MySQL
    conn.close()


# Membuat antarmuka pengguna menggunakan tkinter
root = tk.Tk()

# Menambahkan label untuk judul
tk.Label(root, text="Data Gambar Dari Database MySQL").grid(row=0, column=0, columnspan=2)

# Menambahkan button untuk mengeksekusi query SQL dan menampilkan data
tk.Button(root, text="Tampilkan Data", command=fetch_data).grid(row=1, column=1)

# Menambahkan label untuk header kolom
tk.Label(root, text="Nama").grid(row=2, column=0)
tk.Label(root, text="Gambar").grid(row=2, column=1)

# Menjalankan antarmuka pengguna
root.mainloop()
