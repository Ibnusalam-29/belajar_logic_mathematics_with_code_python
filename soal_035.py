#Menetukan apakah nilai ujian lulus atau tidak dari sebuah list
nilaiUjian = [60, 70, 80, 56, 90, 45, 89, 86, 51, 67, 89, 90, 99, 67, 34]

isLulus = [nilaiUjian[i] for i in range(len(nilaiUjian)) if nilaiUjian[i] >= 75]
print(f"Siswa dengan nilai ujian diatas 75: {isLulus}")

isNotlulus = [nilaiUjian[i] for i in range(len(nilaiUjian)) if nilaiUjian[i] <= 75]
print(f"Siswa dengan nilai ujian dibawah 75: {isNotlulus}")