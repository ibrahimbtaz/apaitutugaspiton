try:
	tugas1 = float(input("Masukkan nilai tugas1: "))
	tugas2 = float(input("Masukkan nilai tugas2: "))
	uts    = float(input("Masukkan nilai uts: "))
	uas    = float(input("Masukkan nilai uas: "))
except ValueError:
	print("Input harus berupa angka")
	exit()

op1 = tugas1 + tugas2 / 2 * 0.25
op2 = uts * 0.25
op3 = uas * 0.5

hasil = op1 + op2 + op3

if hasil >= 87:
		print("A")
elif hasil >= 60:
		print("B")
elif hasil >= 50:
		print("C")
else:
		print("D")