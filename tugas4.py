tarif ={
	'sport' : 10000,
	'hiace' : 1000,
	'innova': 500,
}

def user_input(jenis_mobil, hari,	member,weekend) :
	harga_per_hari = tarif.get(jenis_mobil.lower(),0)
	total_harga = harga_per_hari * hari

	if member :
		total_harga *= 0.10
	else :
		total_harga *= 0.05

	if weekend :
		total_harga += 100000
	
	return total_harga

while True :
	jenis_mobil = input("Masukkan jenis mobil (sport/hiace/innova): ").strip().lower()

	if not jenis_mobil.isalpha():
		print("Input tidak valid. Harap masukkan jenis mobil dengan huruf, tanpa angka.")
	elif jenis_mobil not in tarif :
		print("Jenis mobil tidak tersedia. Pilih antara 'sport', 'hiace', atau 'innova'.")
	else:
		break
	
