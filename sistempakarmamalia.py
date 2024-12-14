import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import joblib

# Memuat model dan encoder
model = joblib.load('model_mamalia.pkl')
encoder = joblib.load('encoder_mamalia.pkl')

# Memuat data mamalia
data_mamalia = pd.read_csv('mamalia.csv')

# Fungsi untuk menanyakan ciri-ciri kepada pengguna
def ask_question(question):
    response = messagebox.askquestion("Pertanyaan", question)
    return response.lower() == 'yes'

# Fungsi untuk menanyakan apakah pengguna ingin melanjutkan atau selesai
def ask_continue_or_done(step):
    response = messagebox.askquestion("Lanjutkan?", f"Apakah Anda ingin melanjutkan ke {step} berikutnya atau selesai?")
    return response.lower() == 'yes', response.lower() == 'no'

# Fungsi untuk mencari mamalia berdasarkan ciri-ciri pengguna
def cari_informasi():
    hasil = []

    # Pertanyaan pertama: habitat
    habitat_input = None
    if ask_question("Apakah mamalia ini hidup di pantai atau lautan?"):
        habitat_input = 'Pantai dan Lautan'
    elif ask_question("Apakah mamalia ini hidup di hutan hujan besar?"):
        habitat_input = 'Hutan Hujan Besar'
    elif ask_question("Apakah mamalia ini hidup di hutan dan padang savana?"):
        habitat_input = 'Hutan dan Padang Savana'
    elif ask_question("Apakah mamalia ini hidup di hutan bakau?"):
        habitat_input = 'Hutan Bakau dan Hutan'
    elif ask_question("Apakah mamalia ini hidup di hutan dan area terbuka?"):
        habitat_input = 'Hutan dan Area Terbuka'
    elif ask_question("Apakah mamalia ini hidup di hutan dan area bervegetasi?"):
        habitat_input = 'Hutan dan Area Bervegetasi'
    
    # Tanyakan apakah melanjutkan ke pertanyaan berikutnya atau selesai
    continue_choice, done_choice = ask_continue_or_done("pertanyaan jenis makanan")
    if done_choice:  # Jika memilih selesai
        show_results(habitat_input)
        return

    # Pertanyaan kedua: jenis makanan
    makanan_input = None
    if ask_question("Apakah mamalia ini herbivora?"):
        makanan_input = 'Herbivora'
    elif ask_question("Apakah mamalia ini karnivora?"):
        makanan_input = 'Karnivora'
    elif ask_question("Apakah mamalia ini omnivora?"):
        makanan_input = 'Omnivora'
    elif ask_question("Apakah mamalia ini frugivora?"):
        makanan_input = 'Frugivora'
    elif ask_question("Apakah mamalia ini insektofag?"):
        makanan_input = 'Insektofag'

    # Tanyakan apakah melanjutkan ke pertanyaan berikutnya atau selesai
    continue_choice, done_choice = ask_continue_or_done("pertanyaan tingkah laku")
    if done_choice:  # Jika memilih selesai
        show_results(habitat_input, makanan_input)
        return

    # Pertanyaan ketiga: tingkah laku
    tingkah_laku_input = None
    if ask_question("Apakah mamalia ini soliter?"):
        tingkah_laku_input = 'Soliter'
    elif ask_question("Apakah mamalia ini nocturnal?"):
        tingkah_laku_input = 'Nocturnal'
    elif ask_question("Apakah mamalia ini berkelompok?"):
        tingkah_laku_input = 'Berkelompok'
    
    # Tanyakan apakah melanjutkan ke pertanyaan berikutnya atau selesai
    continue_choice, done_choice = ask_continue_or_done("pertanyaan bentuk tubuh")
    if done_choice:  # Jika memilih selesai
        show_results(habitat_input, makanan_input, tingkah_laku_input)
        return

    # Pertanyaan keempat: Ciri bentuk tubuh
    bentuk_tubuh_input = None
    if ask_question("Apakah mamalia ini memiliki tubuh lonjong?"):
        bentuk_tubuh_input = 'Lonjong'
    elif ask_question("Apakah mamalia ini memiliki tubuh besar dengan belalai?"):
        bentuk_tubuh_input = 'Besar dengan Belalai'
    elif ask_question("Apakah mamalia ini memiliki tubuh besar dengan kulit kasar?"):
        bentuk_tubuh_input = 'Besar dengan Kulit Kasar'
    elif ask_question("Apakah mamalia ini memiliki tubuh kecil dengan ekor panjang?"):
        bentuk_tubuh_input = 'Kecil dengan Ekor Panjang'

    # Tanyakan apakah melanjutkan ke pertanyaan berikutnya atau selesai
    continue_choice, done_choice = ask_continue_or_done("pertanyaan warna tubuh")
    if done_choice:  # Jika memilih selesai
        show_results(habitat_input, makanan_input, tingkah_laku_input, bentuk_tubuh_input)
        return

    # Pertanyaan kelima: Warna tubuh
    warna_tubuh_input = None
    if ask_question("Apakah mamalia ini berwarna abu-abu?"):
        warna_tubuh_input = 'Abu-abu'
    elif ask_question("Apakah mamalia ini berwarna orange dengan garis tiger?"):
        warna_tubuh_input = 'Orange dengan Garis Tiger'
    elif ask_question("Apakah mamalia ini berwarna hitam dengan bercak kuning?"):
        warna_tubuh_input = 'Hitam dengan Bercak Kuning'
    elif ask_question("Apakah mamalia ini berwarna coklat pudar dengan putih di perut?"):
        warna_tubuh_input = 'Coklat Pudar dengan Putih di Perut'

    # Tanyakan apakah melanjutkan ke pertanyaan berikutnya atau selesai
    continue_choice, done_choice = ask_continue_or_done("pertanyaan tempat tinggal")
    if done_choice:  # Jika memilih selesai
        show_results(habitat_input, makanan_input, tingkah_laku_input, bentuk_tubuh_input, warna_tubuh_input)
        return

    # Pertanyaan keenam: Tempat tinggal
    tempat_tinggal_input = None
    if ask_question("Apakah mamalia ini tinggal di darat?"):
        tempat_tinggal_input = 'Darat'
    elif ask_question("Apakah mamalia ini tinggal di air?"):
        tempat_tinggal_input = 'Air'

    # Menampilkan hasil pencarian setelah selesai mengisi semua kriteria
    show_results(habitat_input, makanan_input, tingkah_laku_input, bentuk_tubuh_input, warna_tubuh_input, tempat_tinggal_input)

# Fungsi untuk menampilkan hasil berdasarkan input yang telah diisi
def show_results(habitat_input=None, makanan_input=None, tingkah_laku_input=None, bentuk_tubuh_input=None, warna_tubuh_input=None, tempat_tinggal_input=None):
    # Filter hasil berdasarkan pencocokan dengan data CSV
    filtered_data = data_mamalia

    if habitat_input:
        filtered_data = filtered_data[filtered_data['Habitat'] == habitat_input]
    if makanan_input:
        filtered_data = filtered_data[filtered_data['Jenis_Makanan'] == makanan_input]
    if tingkah_laku_input:
        filtered_data = filtered_data[filtered_data['Tingkah_Laku'] == tingkah_laku_input]
    if bentuk_tubuh_input:
        filtered_data = filtered_data[filtered_data['Ciri_Bentuk_Tubuh'] == bentuk_tubuh_input]
    if warna_tubuh_input:
        filtered_data = filtered_data[filtered_data['Warna_Tubuh'] == warna_tubuh_input]
    if tempat_tinggal_input:
        filtered_data = filtered_data[filtered_data['Tempat_Tinggal'] == tempat_tinggal_input]

    # Clear the treeview before displaying new results
    for row in treeview.get_children():
        treeview.delete(row)

    if filtered_data.empty:
        messagebox.showinfo("Hasil Pencarian", "Tidak ada data mamalia yang cocok.")
    else:
        # Menambahkan data ke dalam Treeview
        for idx, row in filtered_data.iterrows():
            treeview.insert("", "end", values=(
                row['Nama_Mamalia'],
                row['Habitat'],
                row['Jenis_Makanan'],
                row['Tingkah_Laku'],
                row['Ciri_Bentuk_Tubuh'],
                row['Warna_Tubuh'],
                row['Tempat_Tinggal']
            ))

# Setup tkinter window
root = tk.Tk()
root.title("Sistem Pakar Mamalia")

# Tombol untuk memulai pencarian
button = tk.Button(root, text="Cari Mamalia", command=cari_informasi)
button.pack(pady=20)

# Menambahkan Treeview untuk menampilkan hasil dalam bentuk tabel
columns = ['Nama Mamalia', 'Habitat', 'Jenis Makanan', 'Tingkah Laku', 'Bentuk Tubuh', 'Warna Tubuh', 'Tempat Tinggal']
treeview = ttk.Treeview(root, columns=columns, show="headings", height=10)

# Mengatur kolom-kolom
for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, width=150)

treeview.pack(padx=20, pady=20)

# Menjalankan GUI
root.mainloop()
