nama = input("Nama Mahasiswa : ")
nim = input("NIM Mahasiswa : ")

nilai_tugas = float(input("Nilai tugas : "))
nilai_kuis = float(input("Nilai Kuis : "))
kehadiran = float(input("Kehadiran % : "))

nilai_akhir = 0.4 * nilai_tugas + 0.6 * nilai_kuis

if nilai_akhir >= 75 and kehadiran >= 75:
    status = "LULUS"
else:
    status = "TIMDAK LULUS"

print(f"Nama            : {nama}")
print(f"NIM             : {nim}")
print(f"Nilai Kehadiran : {nilai_akhir}")
print(f"Kehadiran       : {kehadiran:g}%")
print(f"Status          : {status}")