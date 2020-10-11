namabuah=[]

def tambah_namabuah(nama):
    namabuah.append(nama)
    for buah in namabuah:
        print(buah)
    print("-----")
tambah_namabuah("jeruk")
tambah_namabuah("apel")
tambah_namabuah("melon")

namabuah.append("jeruk")
for buah in namabuah:
    print(buah)
    print("-----")

namabuah.append("apel")
for buah in namabuah:
    print(buah)
    print("-----")

def total(x,y):
    total=x+y
    return total

print(total(1,2))
#jumlah = total(1,2)
#print(jumlah)