BATAS_BELANJA = 250000
PERSEN_DISKON = 0.10

nama_pelanggan = input("Nama pelanggan : ")
status_anggota = input("Anggota (ya/tidak) : ").strip().lower()
jumlah_buku = int(input("Jumlah buku : "))
total_belanja = float(input("Total belanja : "))

if status_anggota == "ya" and total_belanja >= BATAS_BELANJA:
    jumlah_diskon = total_belanja * PERSEN_DISKON
    keterangan = "DAPAT DISKON"
else:
    jumlah_diskon = 0
    keterangan = "TIDAK DAPAT DISKON"

total_bayar = total_belanja - jumlah_diskon

print()
print(f"Nama pelanggan : {nama_pelanggan}")
print(f"Status anggota : {status_anggota}")
print(f"Jumlah buku    : {jumlah_buku}")
print(f"Total belanja  : Rp{total_belanja:.0f}")
print(f"Jumlah diskon  : Rp{jumlah_diskon:.0f}")
print(f"Total bayar    : Rp{total_bayar:.0f}")
print(f"Keterangan     : {keterangan}")