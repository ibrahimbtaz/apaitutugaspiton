type_karyawan = input("Masukkan tipe karyawan(manager/supervisor/staff)")
k_karyawan = input("Masukkan Kinerja karyawan (A/B/C)")
hari = int(input("Masukkan jumlah hari tidak kerja dalam 1 bulan : "))

if type_karyawan == "manager":
		if k_karyawan == "A":
			gaji = 10000000
		elif k_karyawan == "B":
			gaji = 8000000
		elif k_karyawan == "C":
			gaji = 6000000
elif type_karyawan == "supervisor":
		if k_karyawan == "A":
			gaji = 7000000
		elif k_karyawan == "B":
			gaji = 6000000
		elif k_karyawan == "C":
			gaji = 5000000
elif type_karyawan == "staff":
		if k_karyawan == "A":
			gaji = 4000000
		elif k_karyawan == "B":
			gaji = 3000000
		elif k_karyawan == "C":
			gaji = 2000000

potongan_gaji = hari * 5000
gaji -= potongan_gaji

print("Gaji yang diterima karyawan adalah : ", gaji)
