daftar_nama = []
daftar_nomor= []
print("Selamat datang! ")
print("   ")
NomorMenu=1
while NomorMenu<3:
    print("------Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar ")  
    print("   ")
    NomorMenu=int(input("Pilih Menu: "))

    if NomorMenu==1:
      if len(daftar_nama)==0 and len(daftar_nomor)==0:
        print("Tidak ada data")
      else:
         print("Daftar Kontak:")
         for x in range(len(daftar_nama)):
             print("Nama: ",daftar_nama[x])
             print("No Telepon: ",daftar_nomor[x]) 
                      
    elif NomorMenu==2:
     Profile1=str(input("Nama: "))
     Profile2=str(input("No Telepon: "))
     daftar_nama.append(Profile1)
     daftar_nomor.append(Profile2)
     print("Kontak berhasil ditambahkan!")
    elif NomorMenu==3:
     print("Program selesai, sampai jumpa!")
     break
    elif NomorMenu!=1 or NomorMenu!=2 or NomorMenu!=3:
     print("Menu Tidak Tersedia")
    


