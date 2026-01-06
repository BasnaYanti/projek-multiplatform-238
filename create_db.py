import sqlite3

# Koneksi ke database
conn = sqlite3.connect('books.db')

# Membuat cursor
c = conn.cursor()

# Membuat tabel
c.execute('''
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul VARCHAR(100),
        penulis VARCHAR(100)
    )
''')

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()