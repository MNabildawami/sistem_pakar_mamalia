import tkinter as tk
from tkinter import ttk

# Basis pengetahuan dalam bentuk daftar aturan
basis_pengetahuan = [
    {"Nama": "Lumba-lumba Hidung Botol", "Klasifikasi": "Mamalia", "Habitat": "Pantai dan Lautan", "Jenis_Makanan": "Plankton dan Ikan", "Ciri_Bentuk_Tubuh": "Lonjong", "Tingkah_Laku": "Nocturnal", "Warna_Tubuh": "Abu-abu keputihan", "Tempat_Tinggal": "Air"},
    {"Nama": "Harimau Sumatera", "Klasifikasi": "Mamalia", "Habitat": "Hutan Hujan Besar", "Jenis_Makanan": "Karnivora", "Ciri_Bentuk_Tubuh": "Berat dengan Cakar Besar", "Tingkah_Laku": "Soliter", "Warna_Tubuh": "Orange dengan Garis Tiger", "Tempat_Tinggal": "Darat"},
    {"Nama": "Gajah Asia", "Klasifikasi": "Mamalia", "Habitat": "Hutan dan Padang Savana", "Jenis_Makanan": "Herbivora", "Ciri_Bentuk_Tubuh": "Besar dengan Belalai", "Tingkah_Laku": "Kepekaan Gerakan Tinggi", "Warna_Tubuh": "Abu-abu", "Tempat_Tinggal": "Darat"},
    {"Nama": "Orangutan", "Klasifikasi": "Mamalia", "Habitat": "Hutan Hujan", "Jenis_Makanan": "Omnivora", "Ciri_Bentuk_Tubuh": "Kekar dengan Tangan Panjang", "Tingkah_Laku": "Soliter", "Warna_Tubuh": "Orange dengan Rambut Panjang", "Tempat_Tinggal": "Darat"},
    {"Nama": "Kelelawar Buah", "Klasifikasi": "Mamalia", "Habitat": "Hutan dan Area Terbuka", "Jenis_Makanan": "Frugivora", "Ciri_Bentuk_Tubuh": "Berbulu", "Tingkah_Laku": "Nocturnal", "Warna_Tubuh": "Hitam dengan Bercak Kuning", "Tempat_Tinggal": "Darat"},
    {"Nama": "Badak Jawa", "Klasifikasi": "Mamalia", "Habitat": "Hutan Bakau dan Hutan", "Jenis_Makanan": "Herbivora", "Ciri_Bentuk_Tubuh": "Besar dengan Kulit Kasar", "Tingkah_Laku": "Soliter", "Warna_Tubuh": "Abu-abu Kelabu", "Tempat_Tinggal": "Darat"},
    {"Nama": "Beruang Madu", "Klasifikasi": "Mamalia", "Habitat": "Hutan Hujan", "Jenis_Makanan": "Omnivora", "Ciri_Bentuk_Tubuh": "Tegap dengan Cakar Panjang", "Tingkah_Laku": "Soliter", "Warna_Tubuh": "Hitam dengan Cincin Kuning", "Tempat_Tinggal": "Darat"},
    {"Nama": "Rusa Timor", "Klasifikasi": "Mamalia", "Habitat": "Hutan dan Padang Rumput", "Jenis_Makanan": "Herbivora", "Ciri_Bentuk_Tubuh": "Cepat dengan Tanduk", "Tingkah_Laku": "Nocturnal", "Warna_Tubuh": "Coklat Pudar dengan Putih di Perut", "Tempat_Tinggal": "Darat"},
    {"Nama": "Trenggiling Jawa", "Klasifikasi": "Mamalia", "Habitat": "Hutan dan Area Terbuka", "Jenis_Makanan": "Insektofag", "Ciri_Bentuk_Tubuh": "Kecil dengan Bulu Perisai", "Tingkah_Laku": "Nocturnal", "Warna_Tubuh": "Berlian Coklat", "Tempat_Tinggal": "Darat"},
    {"Nama": "Kuskus", "Klasifikasi": "Mamalia", "Habitat": "Hutan dan Area Bervegetasi", "Jenis_Makanan": "Herbivora", "Ciri_Bentuk_Tubuh": "Kecil dengan Ekor Panjang", "Tingkah_Laku": "Soliter", "Warna_Tubuh": "Abu-abu Coklat", "Tempat_Tinggal": "Darat"}
]

# Forward chaining dengan probabilistik (Bayesian)
def forward_chaining(input_facts):
    matches = []
    logs = []

    for mamalia in basis_pengetahuan:
        matched_attributes = []
        score = 0

        for key, value in input_facts.items():
            if mamalia.get(key) == value:
                matched_attributes.append(key)
                score += 1  # Tingkat kecocokan bertambah jika atribut cocok

        total_attributes = len(input_facts)
        probability = (score / total_attributes) if total_attributes > 0 else 0

        if score > 0:
            matches.append((mamalia, probability))
            logs.append((mamalia["Nama"], matched_attributes))

    matches.sort(key=lambda x: x[1], reverse=True)  # Urutkan berdasarkan probabilitas

    return matches, logs

# Fungsi untuk mencari mamalia berdasarkan input pengguna
def cari_mamalia():
    if not (habitat_var.get() and makanan_var.get() and tubuh_var.get() and tingkah_var.get() and warna_var.get() and tempat_var.get()):
        transparansi_text.delete(1.0, tk.END)
        transparansi_text.insert(tk.END, "Harap isi semua dropdown sebelum mencari mamalia.")
        return

    input_facts = {
        "Habitat": habitat_var.get(),
        "Jenis_Makanan": makanan_var.get(),
        "Ciri_Bentuk_Tubuh": tubuh_var.get(),
        "Tingkah_Laku": tingkah_var.get(),
        "Warna_Tubuh": warna_var.get(),
        "Tempat_Tinggal": tempat_var.get()
    }

    matches, logs = forward_chaining(input_facts)

    # Hapus hasil sebelumnya
    for widget in result_table.get_children():
        result_table.delete(widget)

    # Tampilkan hasil dengan probabilitas > 50%
    displayed = False
    transparansi_text.delete(1.0, tk.END)

    for mamalia, probability in matches:
        if probability > 0.3:
            result_table.insert("", "end", values=(
                mamalia["Nama"],
                mamalia["Klasifikasi"],
                mamalia["Habitat"],
                mamalia["Jenis_Makanan"],
                mamalia["Ciri_Bentuk_Tubuh"],
                mamalia["Tingkah_Laku"],
                mamalia["Warna_Tubuh"],
                mamalia["Tempat_Tinggal"],
                f"{probability * 100:.2f}%"
            ))
            displayed = True

    # Log transparansi aturan
    transparansi_text.insert(tk.END, "\n".join([f"{log[0]}: {', '.join(log[1])}" for log in logs]))

    if not displayed:
        result_table.insert("", "end", values=("Tidak ditemukan", "-", "-", "-", "-", "-", "-", "-", "0%"))
        transparansi_text.insert(tk.END, "Tidak ada kecocokan dengan probabilitas > 50%.")

# Setup GUI menggunakan Tkinter
root = tk.Tk()
root.title("Sistem Pakar Mamalia - Probabilistik dan Transparansi")

# Variabel untuk menyimpan input pengguna
habitat_var = tk.StringVar()
makanan_var = tk.StringVar()
tubuh_var = tk.StringVar()
tingkah_var = tk.StringVar()
warna_var = tk.StringVar()
tempat_var = tk.StringVar()

# Membuat label dan dropdown untuk setiap ciri-ciri
tk.Label(root, text="Habitat").grid(row=0, column=0, padx=10, pady=5)
habitat_menu = ttk.Combobox(root, textvariable=habitat_var, values=["Pantai dan Lautan", "Hutan Hujan Besar", "Hutan dan Padang Savana", "Hutan Hujan", "Hutan dan Area Terbuka", "Hutan Bakau dan Hutan", "Hutan dan Padang Rumput", "Hutan dan Area Bervegetasi"])
habitat_menu.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Jenis Makanan").grid(row=1, column=0, padx=10, pady=5)
makanan_menu = ttk.Combobox(root, textvariable=makanan_var, values=["Plankton dan Ikan", "Karnivora", "Herbivora", "Omnivora", "Frugivora", "Insektofag"])
makanan_menu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Ciri Bentuk Tubuh").grid(row=2, column=0, padx=10, pady=5)
tubuh_menu = ttk.Combobox(root, textvariable=tubuh_var, values=["Lonjong", "Berat dengan Cakar Besar", "Besar dengan Belalai", "Kekar dengan Tangan Panjang", "Berbulu", "Besar dengan Kulit Kasar", "Tegap dengan Cakar Panjang", "Cepat dengan Tanduk", "Kecil dengan Bulu Perisai", "Kecil dengan Ekor Panjang"])
tubuh_menu.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Tingkah Laku").grid(row=3, column=0, padx=10, pady=5)
tingkah_menu = ttk.Combobox(root, textvariable=tingkah_var, values=["Nocturnal", "Soliter", "Kepekaan Gerakan Tinggi"])
tingkah_menu.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Warna Tubuh").grid(row=4, column=0, padx=10, pady=5)
warna_menu = ttk.Combobox(root, textvariable=warna_var, values=["Abu-abu keputihan", "Orange dengan Garis Tiger", "Abu-abu", "Orange dengan Rambut Panjang", "Hitam dengan Bercak Kuning", "Abu-abu Kelabu", "Hitam dengan Cincin Kuning", "Coklat Pudar dengan Putih di Perut", "Berlian Coklat", "Abu-abu Coklat"])
warna_menu.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Tempat Tinggal").grid(row=5, column=0, padx=10, pady=5)
tempat_menu = ttk.Combobox(root, textvariable=tempat_var, values=["Air", "Darat"])
tempat_menu.grid(row=5, column=1, padx=10, pady=5)

# Tombol untuk mencari mamalia
cari_button = tk.Button(root, text="Cari Mamalia", command=cari_mamalia)
cari_button.grid(row=6, column=1, pady=10)

# Tabel hasil
columns = ("Nama", "Klasifikasi", "Habitat", "Jenis Makanan", "Ciri Bentuk Tubuh", "Tingkah Laku", "Warna Tubuh", "Tempat Tinggal", "Kemiripan")
result_table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    result_table.heading(col, text=col)
    result_table.column(col, width=120)
result_table.grid(row=7, column=0, columnspan=2, pady=10)

# Area untuk transparansi aturan
tk.Label(root, text="Transparansi Aturan yang Digunakan:").grid(row=8, column=0, columnspan=2)
transparansi_text = tk.Text(root, height=10, width=80)
transparansi_text.grid(row=9, column=0, columnspan=2, pady=5)

# Menjalankan GUI
root.mainloop()
