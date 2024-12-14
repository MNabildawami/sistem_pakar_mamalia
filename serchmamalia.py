import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Load data dari CSV
data_mamalia = pd.read_csv('mamalia.csv')

# Fungsi untuk mencari informasi berdasarkan input
def cari_informasi():
    # Mengambil nilai input dari form (input string gabungan)
    input_string = entry_input.get().strip().lower()

    # Jika input kosong, beri peringatan
    if not input_string:
        messagebox.showerror("Error", "Masukkan ciri-ciri untuk pencarian.")
        return

    # Menyaring data berdasarkan aturan
    hasil = []

    # Cari berdasarkan habitat
    habitat_results = data_mamalia[data_mamalia['Habitat'].str.lower().str.contains(input_string)]
    for _, row in habitat_results.iterrows():
        hasil.append([row['Nama_Mamalia'], row['Habitat'], row['Ciri_Bentuk_Tubuh'], row['Jenis_Makanan'],
                      row['Tingkah_Laku'], row['Warna_Tubuh'], row['Tempat_Tinggal']])

    # Cari berdasarkan bentuk tubuh
    bentuk_tubuh_results = data_mamalia[data_mamalia['Ciri_Bentuk_Tubuh'].str.lower().str.contains(input_string)]
    for _, row in bentuk_tubuh_results.iterrows():
        if [row['Nama_Mamalia'], row['Habitat'], row['Ciri_Bentuk_Tubuh'], row['Jenis_Makanan'],
            row['Tingkah_Laku'], row['Warna_Tubuh'], row['Tempat_Tinggal']] not in hasil:
            hasil.append([row['Nama_Mamalia'], row['Habitat'], row['Ciri_Bentuk_Tubuh'], row['Jenis_Makanan'],
                          row['Tingkah_Laku'], row['Warna_Tubuh'], row['Tempat_Tinggal']])

    # Cari berdasarkan jenis makanan
    makanan_results = data_mamalia[data_mamalia['Jenis_Makanan'].str.lower().str.contains(input_string)]
    for _, row in makanan_results.iterrows():
        for result in hasil:
            if result[0] == row['Nama_Mamalia']:
                result[3] = row['Jenis_Makanan']
                break
        else:
            hasil.append([row['Nama_Mamalia'], row['Habitat'], row['Ciri_Bentuk_Tubuh'], row['Jenis_Makanan'],
                          row['Tingkah_Laku'], row['Warna_Tubuh'], row['Tempat_Tinggal']])

    # Cari berdasarkan tingkah laku
    tingkah_laku_results = data_mamalia[data_mamalia['Tingkah_Laku'].str.lower().str.contains(input_string)]
    for _, row in tingkah_laku_results.iterrows():
        for result in hasil:
            if result[0] == row['Nama_Mamalia']:
                result[4] = row['Tingkah_Laku']
                break
        else:
            hasil.append([row['Nama_Mamalia'], row['Habitat'], row['Ciri_Bentuk_Tubuh'], row['Jenis_Makanan'],
                          row['Tingkah_Laku'], row['Warna_Tubuh'], row['Tempat_Tinggal']])

    # Cari berdasarkan warna tubuh
    warna_tubuh_results = data_mamalia[data_mamalia['Warna_Tubuh'].str.lower().str.contains(input_string)]
    for _, row in warna_tubuh_results.iterrows():
        for result in hasil:
            if result[0] == row['Nama_Mamalia']:
                result[5] = row['Warna_Tubuh']
                break
        else:
            hasil.append([row['Nama_Mamalia'], row['Habitat'], row['Ciri_Bentuk_Tubuh'], row['Jenis_Makanan'],
                          row['Tingkah_Laku'], row['Warna_Tubuh'], row['Tempat_Tinggal']])

    # Cari berdasarkan tempat tinggal
    tempat_tinggal_results = data_mamalia[data_mamalia['Tempat_Tinggal'].str.lower().str.contains(input_string)]
    for _, row in tempat_tinggal_results.iterrows():
        for result in hasil:
            if result[0] == row['Nama_Mamalia']:
                result[6] = row['Tempat_Tinggal']
                break
        else:
            hasil.append([row['Nama_Mamalia'], row['Habitat'], row['Ciri_Bentuk_Tubuh'], row['Jenis_Makanan'],
                          row['Tingkah_Laku'], row['Warna_Tubuh'], row['Tempat_Tinggal']])

    # Menampilkan hasil pencarian
    if not hasil:
        messagebox.showerror("Error", "Tidak ada mamalia yang sesuai dengan kriteria yang diberikan.")
    else:
        # Clear the previous results
        for row in treeview.get_children():
            treeview.delete(row)
        
        # Insert new results into the table
        for row in hasil:
            treeview.insert("", "end", values=row)

# Setup GUI menggunakan tkinter
root = tk.Tk()
root.title("Sistem Pakar Mamalia Berdasarkan Ciri-Ciri")

# Frame untuk form input
frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

# Label dan input untuk ciri-ciri gabungan
label_input = tk.Label(frame_input, text="Masukkan Ciri-Ciri Mamalia (misal: pantai besar herbivora):")
label_input.grid(row=0, column=0, pady=5, sticky="w")
entry_input = tk.Entry(frame_input, width=60)
entry_input.grid(row=0, column=1, pady=5)

# Tombol untuk mencari informasi
button_cari = tk.Button(root, text="Cari Mamalia", command=cari_informasi)
button_cari.pack(pady=10)

# Frame untuk tabel hasil
frame_table = tk.Frame(root)
frame_table.pack(padx=10, pady=10)

# Setup Treeview untuk tabel hasil
columns = ("Mamalia", "Habitat", "Ciri Bentuk Tubuh", "Jenis Makanan", "Tingkah Laku", "Warna Tubuh", "Tempat Tinggal")
treeview = ttk.Treeview(frame_table, columns=columns, show="headings")
treeview.heading("Mamalia", text="Nama Mamalia")
treeview.heading("Habitat", text="Habitat")
treeview.heading("Ciri Bentuk Tubuh", text="Ciri Bentuk Tubuh")
treeview.heading("Jenis Makanan", text="Jenis Makanan")
treeview.heading("Tingkah Laku", text="Tingkah Laku")
treeview.heading("Warna Tubuh", text="Warna Tubuh")
treeview.heading("Tempat Tinggal", text="Tempat Tinggal")

# Menyesuaikan lebar kolom
for col in columns:
    treeview.column(col, width=200)

treeview.pack()

# Mulai aplikasi
root.mainloop()
