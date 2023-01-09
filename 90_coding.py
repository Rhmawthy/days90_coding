while True :
	angka = int(input("masukkan angka : "))
	
	if angka <= 10 :
		h = [i for i in range (1,angka + 1)]
		print (h)
		
	elif  angka >= 10 :
		print("angka terlalu tinggi")
		break