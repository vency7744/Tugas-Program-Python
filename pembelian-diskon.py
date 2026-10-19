BIAYA_ADMIN = 1500
nama = input("Nama pembeli: ").strip().title()
barang = input("Nama barang: ").strip().title()
harga = float(input("Harga satuan: "))
jumlah = int(input("Jumlah barang: "))
uang = float(input("Uang yang dibawa: "))
subtotal = harga * jumlah
total = subtotal + BIAYA_ADMIN
data_valid = harga > 0 and jumlah > 0
uang_cukup = uang >= total
print("\n--- RINGKASAN ---")
print(f"Pembeli : {nama}")
print(f"Barang : {barang}")
print(f"Subtotal : Rp{subtotal:,.0f}")
print(f"Biaya admin : Rp{BIAYA_ADMIN:,.0f}")
print(f"Total : Rp{total:,.0f}")
print(f"Data valid : {data_valid}")
print(f"Uang cukup : {uang_cukup}")