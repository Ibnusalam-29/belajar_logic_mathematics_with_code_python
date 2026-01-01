#Menyaring siswa di atas 12 tahun

umurSiswa = [15, 14, 11, 17, 13, 15, 10, 17, 16, 15]
siswaDiatas12 = [umurSiswa[i] for i in range(len(umurSiswa)) if umurSiswa[i] > 12]

print(f"Siswa dengan umur di atas 12 tahun: {siswaDiatas12}")