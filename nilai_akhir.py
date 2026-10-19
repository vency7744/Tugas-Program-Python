BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
nama = input("Nama mahasiswa : ").strip().title()
nilai_tugas = float(input("Nilai tugas : "))
nilai_uts = float(input("Nilai UTS : "))
nilai_uas = float(input("Nilai UAS : "))

nilai_akhir = (nilai_tugas * BOBOT_TUGAS
+ nilai_uts * BOBOT_UTS
+ nilai_uas * BOBOT_UAS)
data_valid = (0 <= nilai_tugas <= 100
and 0 <= nilai_uts <= 100
and 0 <= nilai_uas <= 100)
lulus_sementara = nilai_akhir >= 60
print("\n--- RINGKASAN HASIL ---")
print(f"Nama mahasiswa : {nama}")
print(f"Nilai tugas : {nilai_tugas}")
print(f"Nilai UTS : {nilai_uts}")
print(f"Nilai UAS : {nilai_uas}")
print(f"Nilai akhir : {nilai_akhir:.2f}")
print(f"Data valid : {data_valid}")
print(f"Lulus sementara : {lulus_sementara}")