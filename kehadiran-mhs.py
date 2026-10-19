nama = input("Nama mahasiswa: ")
kehadiran = float(input("Persentase kehadiran: "))
nilai = float(input("Nilai akhir: "))
if kehadiran >= 75:
    if nilai >= 60:
        status = "LULUS"
    else:
        status = "BELUM LULUS - nilai akhir di bawah 60"
else:
    status = "TIDAK MEMENUHI SYARAT - kehadiran di bawah 75%"
print(f"Nama   : {nama}")
print(f"Status:{status}")