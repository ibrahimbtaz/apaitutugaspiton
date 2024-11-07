try:
	# x = int(input("Masukkan x: "))
	# y = int(input("Masukkan y: "))
	x = 10
	y = 20
except ValueError:
	print("Input harus berupa angka")
	exit()

if x >= y:
	print("x lebih besar dari y")
else:
	temp = x
	x = y
	y = temp
	# if hasil >= y	: 
	print(f"Nilai x sekarang lebih besar dari y: x = {x}, y = {y}")

