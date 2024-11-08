# Tarif sewa per hari untuk masing-masing jenis mobil
tarif = {
    "sport": 10000,
    "hiace": 1000,
    "innova": 500
}

# Fungsi untuk menghitung biaya sewa
def hitung_biaya_sewa(jenis_mobil, hari_sewa, member, weekend):
    # Ambil tarif per hari berdasarkan jenis mobil
    biaya_per_hari = tarif.get(jenis_mobil.lower(), 0)
    
    # Hitung total biaya tanpa diskon
    total_biaya = biaya_per_hari * hari_sewa
    
    # Berikan diskon sesuai status member
    if member:
        member = 0.10
        total_biaya = total_biaya - (total_biaya * member)  # Diskon 10% untuk member
    else:
        total_biaya *= 0.95 # Diskon 5% untuk non-member
    
    # Tambahkan biaya tambahan jika sewa di hari weekend
    if weekend:
        total_biaya += 100000

    return total_biaya

# Fungsi validasi input jenis mobil
def input_jenis_mobil():
    while True:
        jenis_mobil = input("Masukkan jenis mobil (sport/hiace/innova): ").strip().lower()
        # Cek apakah input berisi angka
        if not jenis_mobil.isalpha():
            print("Input tidak valid. Harap masukkan jenis mobil dengan huruf, tanpa angka.")
        elif jenis_mobil not in tarif:
            print("Jenis mobil tidak tersedia. Pilih antara 'sport', 'hiace', atau 'innova'.")
        else:
            return jenis_mobil

# Input data
jenis_mobil = input_jenis_mobil()
hari_sewa = int(input("Masukkan jumlah hari sewa: "))
member = input("Apakah penyewa adalah member? (y/n): ").strip().lower() == 'y'
weekend = input("Apakah sewa di hari weekend? (y/n): ").strip().lower() == 'y'

# Hitung dan tampilkan biaya sewa
biaya_sewa = hitung_biaya_sewa(jenis_mobil, hari_sewa, member, weekend)
print(f"Total biaya sewa: Rp {biaya_sewa:.2f}")
