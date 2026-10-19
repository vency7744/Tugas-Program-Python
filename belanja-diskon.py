nama = input("Nama Pelanggan : ")
total_belanja = float(input("Total Belanja : "))

if total_belanja >= 500000:
    diskon = total_belanja * 0.10
else:
    diskon = 0

total_bayar = total_belanja - diskon

print(f"Nama pelanggan : {nama}")
print(f"Total belanja  : {total_belanja}")
print(f"Diskon         : {diskon}")
print(f"Total bayar    : {total_bayar}")