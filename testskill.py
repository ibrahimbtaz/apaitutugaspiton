print("=="*10)
print("pemesanan makanan")
print("=="*10)

def user_input(makanan, harga, jumlah, member, weekend) :
	harga_per_makanan = harga.get(makanan.lower(),0)
	total_harga = harga_per_makanan * jumlah

	if member :
		total_harga *= 0.10
	else :
		total_harga *= 0.05

	if weekend :
		total_harga += 100000
	
	return total_harga