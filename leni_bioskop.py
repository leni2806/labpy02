# Program menghitung harga tiket bioskop
# Harga dasar tiket
HARGA_REGULER = 50000
HARGA_VIP = 100000
DISKON_MEMBER = 0.2  # 20% diskon

def hitung_harga_tiket():
    print("=== Program Hitung Harga Tiket Bioskop ===")
    print("\nPilih tipe tiket:")
    print("1. Reguler (Rp50.000)")
    print("2. VIP (Rp100.000)")
    
    # Input tipe tiket
    while True:
        try:
            tipe_tiket = int(input("\nMasukkan pilihan (1/2): "))
            if tipe_tiket in [1, 2]:
                break
            print("Error: Pilihan tidak valid. Silakan pilih 1 atau 2.")
        except ValueError:
            print("Error: Mohon masukkan angka 1 atau 2.")

    # Input status member
    while True:
        member = input("Apakah anda memiliki kartu member? (y/n): ").lower()
        if member in ['y', 'n']:
            break
        print("Error: Mohon masukkan 'y' atau 'n'.")

    # Menentukan harga dasar menggunakan operator ternary
    harga_dasar = HARGA_REGULER if tipe_tiket == 1 else HARGA_VIP
    
    # Menghitung total harga dengan mempertimbangkan diskon member menggunakan operator ternary
    total_harga = harga_dasar * (1 - DISKON_MEMBER) if member == 'y' else harga_dasar
    
    # Menampilkan rincian pembayaran
    print("\n=== Rincian Pembayaran ===")
    print(f"Tipe Tiket: {'Reguler' if tipe_tiket == 1 else 'VIP'}")
    print(f"Status Member: {'Ya' if member == 'y' else 'Tidak'}")
    print(f"Harga Dasar: Rp{harga_dasar:,.0f}")
    if member == 'y':
        print(f"Diskon Member (20%): Rp{(harga_dasar * DISKON_MEMBER):,.0f}")
    print(f"Total Pembayaran: Rp{total_harga:,.0f}")

# Menjalankan program
if __name__ == "__main__":
   hitung_harga_tiket()