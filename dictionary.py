pelanggan= {"nama" : "Hakim",
            "umur" : 21
}
pelanggan2= {"nama" : "Alghi",
            "umur" : 22
}
for key in pelanggan:
    print(key)
    print(pelanggan[key])
for key in pelanggan2:
    print(key)
    print(pelanggan2[key])
    

daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan2)

for pelanggan in daftar_pelanggan:
    print("nama : {}". format(pelanggan["nama"]))
    print("umur : {}". format(pelanggan["umur"]))



