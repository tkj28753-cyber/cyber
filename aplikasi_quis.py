import random

# ==============================
# DATABASE USER
# ==============================
users = {
    "admin": "1234"   # Akun default
}

# ==============================
# REGISTRASI
# ==============================
def register():
    print("\n=== REGISTRASI ===")
    while True:
        username = input("Buat username baru : ").strip()
        if not username:
            print("Username tidak boleh kosong.\n")
            continue
        if username in users:
            print("Username sudah dipakai, coba lagi.\n")
        else:
            break

    while True:
        password = input("Buat password : ").strip()
        if not password:
            print("Password tidak boleh kosong.\n")
            continue

        confirm = input("Konfirmasi password : ").strip()
        if password != confirm:
            print("Password tidak sama! Coba lagi.\n")
        else:
            break

    users[username] = password
    print("Registrasi berhasil! Silakan login.\n")

# ==============================
# LOGIN
# ==============================
def login():
    print("\n=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        print("Login berhasil!\n")
        return username
    else:
        print("Username atau password salah!\n")
        return None

# ==============================
# LOGOUT
# ==============================
def logout():
    print("\nAnda telah logout.\n")

# ==============================
# MATERI & KUIS TKJ
# ==============================
materi = {
    "pemula": "Materi: Pengenalan Perangkat Keras Komputer dan Dasar TKJ.",
    "menengah": "Materi: Pengenalan Jaringan Komputer dan Perangkat Jaringan.",
    "lanjutan": "Materi: IP Address, Subnetting, dan Topologi Jaringan."
}

kuis = {
    "pemula": [
        {"soal": "Perangkat yang berfungsi mengolah data di komputer adalah...",
         "opsi": ["Monitor", "CPU", "Keyboard"], "jawaban": "CPU"},
        {"soal": "Keyboard termasuk perangkat...",
         "opsi": ["Input", "Output", "Processing"], "jawaban": "Input"},
        {"soal": "RAM berfungsi untuk...",
         "opsi": ["Menyimpan data permanen", "Menyimpan data sementara", "Menghubungkan internet"],
         "jawaban": "Menyimpan data sementara"}
    ],

    "menengah": [
        {"soal": "Router digunakan untuk...",
         "opsi": ["Mencetak dokumen", "Menyebarkan jaringan", "Menyimpan file"],
         "jawaban": "Menyebarkan jaringan"},
        {"soal": "Kabel UTP memiliki berapa pasang kabel?",
         "opsi": ["2 pasang", "4 pasang", "8 pasang"], "jawaban": "4 pasang"},
        {"soal": "Perangkat jaringan untuk menghubungkan banyak komputer adalah...",
         "opsi": ["Hub/Switch", "Mouse", "Proyektor"], "jawaban": "Hub/Switch"}
    ],

    "lanjutan": [
        {"soal": "IP Address versi 4 (IPv4) memiliki panjang...",
         "opsi": ["16 bit", "32 bit", "128 bit"], "jawaban": "32 bit"},
        {"soal": "Network ID pada IP 192.168.1.10/24 adalah...",
         "opsi": ["192.168.1.0", "192.168.0.1", "192.168.10.1"],
         "jawaban": "192.168.1.0"},
        {"soal": "Topologi jaringan yang memakai HUB adalah...",
         "opsi": ["Ring", "Bus", "Star"], "jawaban": "Star"}
    ]
}

# ==============================
# FUNGSI KUIS
# ==============================
def tampilkan_materi(level):
    print("\n=== MATERI LEVEL:", level.upper(), "===")
    print(materi[level], "\n")

def jalankan_kuis(level):
    skor = 0
    soal_list = kuis[level][:]
    random.shuffle(soal_list)

    for q in soal_list:
        print("\n", q["soal"])
        for i, opsi in enumerate(q["opsi"]):
            print(f"{i+1}. {opsi}")

        while True:
            jawab = input("Jawaban Anda (angka): ").strip()
            if jawab.isdigit() and 1 <= int(jawab) <= len(q["opsi"]):
                break
            else:
                print("Masukkan angka yang valid!")

        if q["opsi"][int(jawab) - 1] == q["jawaban"]:
            skor += 1

    return skor

def adaptasi_level(level, skor):
    total = len(kuis[level])
    nilai = (skor / total) * 100
    print(f"\nNilai Anda: {nilai}")

    if nilai >= 80:
        print("Bagus! Naik ke level berikutnya.\n")

        if level == "pemula":
            return "menengah"
        elif level == "menengah":
            return "lanjutan"
        else:
            return "selesai"

    else:
        print("Nilai kurang. Ulangi level ini.\n")
        return level

# ==============================
# MENU UTAMA (otomatis tanpa menu)
# ==============================
def menu_utama(username):
    level = "pemula"

    while True:
        tampilkan_materi(level)

        skor = jalankan_kuis(level)
        level = adaptasi_level(level, skor)

        if level == "selesai":
            print("🎉 SELAMAT! Anda telah menyelesaikan seluruh level!\n")
            break

# ==============================
# PROGRAM UTAMA
# ==============================
while True:
    print("\n=== SELAMAT DATANG DI APLIKASI KUIS TKJ ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        user = login()
        if user:
            menu_utama(user)
            logout()

    elif pilihan == "2":
        register()

    elif pilihan == "3":
        print("Terima kasih telah menggunakan aplikasi!")
        break

    else:
        print("Pilihan tidak valid!\n")
