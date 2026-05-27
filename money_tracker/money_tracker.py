import json
import os
from datetime import datetime

# ========================
# FILE DATABASE
# ========================
FILE_DATA = "data_keuangan.json"


# ========================
# LOAD DATA
# ========================
def load_data():
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            return json.load(file)
    return []


# ========================
# SAVE DATA
# ========================
def save_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)


# ========================
# FORMAT RUPIAH
# ========================
def format_rupiah(angka):
    return f"Rp{angka:,}".replace(",", ".")


# ========================
# TAMBAH TRANSAKSI
# ========================
def tambah_transaksi(data):
    print("\n=== Tambah Transaksi ===")

    # Input jenis
    while True:
        jenis = input("Jenis (masuk/keluar): ").lower()

        if jenis in ["masuk", "keluar"]:
            break
        else:
            print("❌ Jenis harus masuk atau keluar!")

    # Input jumlah
    while True:
        try:
            jumlah = int(input("Jumlah: "))
            break
        except ValueError:
            print("❌ Jumlah harus angka!")

    # Input keterangan
    keterangan = input("Keterangan: ")

    # Input tanggal
    tanggal = input("Tanggal (DD-MM-YYYY, kosong = hari ini): ")

    if tanggal == "":
        tanggal = datetime.now().strftime("%d-%m-%Y")

    transaksi = {
        "tanggal": tanggal,
        "jenis": jenis,
        "jumlah": jumlah,
        "keterangan": keterangan
    }

    data.append(transaksi)
    save_data(data)

    print("✅ Transaksi berhasil ditambahkan!")


# ========================
# LIHAT TRANSAKSI
# ========================
def lihat_transaksi(data):
    print("\n=== Daftar Transaksi ===")

    if not data:
        print("Belum ada transaksi.")
        return

    for i, t in enumerate(data, start=1):
        print(
            f"{i}. "
            f"[{t['tanggal']}] "
            f"{t['jenis'].capitalize()} - "
            f"{format_rupiah(t['jumlah'])} "
            f"({t['keterangan']})"
        )


# ========================
# HITUNG SALDO
# ========================
def hitung_saldo(data):
    saldo = 0

    for t in data:
        if t["jenis"] == "masuk":
            saldo += t["jumlah"]

        elif t["jenis"] == "keluar":
            saldo -= t["jumlah"]

    return saldo


# ========================
# RESET DATA
# ========================
def reset_data(data):
    print("\n⚠️ Semua data akan dihapus!")

    konfirmasi = input("Ketik 'ya' untuk reset data: ")

    if konfirmasi == "ya":
        data.clear()
        save_data(data)
        print("✅ Semua data berhasil direset!")
    else:
        print("❌ Reset dibatalkan.")


# ========================
# MENU UTAMA
# ========================
def menu():
    data = load_data()

    while True:
        print("\n======================")
        print("     MONEY TRACKER")
        print("======================")
        print("1. Tambah Transaksi")
        print("2. Lihat Transaksi")
        print("3. Lihat Saldo")
        print("4. Reset Semua Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_transaksi(data)

        elif pilihan == "2":
            lihat_transaksi(data)

        elif pilihan == "3":
            saldo = hitung_saldo(data)
            print(f"\n💰 Saldo Saat Ini: {format_rupiah(saldo)}")

        elif pilihan == "4":
            reset_data(data)

        elif pilihan == "5":
            print("\n👋 Program selesai.")
            break

        else:
            print("❌ Pilihan tidak valid!")


# ========================
# RUN PROGRAM
# ========================
menu()
