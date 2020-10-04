UjianTeori =input("Masukkan nilai ujian teori ")
UjianPraktek = input("Masukkan nilai ujian praktek ")

Nteori=float(UjianTeori)
Npraktek=float(UjianPraktek)

if Nteori>=70 and Npraktek>=70:
    print("selamat, anda lulus!")
elif Nteori>=70 and Npraktek<70:
    print("Anda harus mengulang ujian praktek.")
elif Nteori<70 and Npraktek>=70:
    print("Anda harus mengulang ujian teori.")
elif Nteori<70 and Npraktek<70:
    print("Anda harus mengulang ujian teori dan praktek.")
