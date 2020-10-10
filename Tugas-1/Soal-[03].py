Uteori = float(input("Masukkan nilai ujian teori "))
Upraktek = float(input("Masukkan nilai ujian praktek "))


if Uteori>=70 and Upraktek>=70:
    print("selamat, anda lulus!")
elif Uteori>=70 and Upraktek<70:
    print("Anda harus mengulang ujian praktek.")
elif Uteori<70 and Upraktek>=70:
    print("Anda harus mengulang ujian teori.")
elif Uteori<70 and Upraktek<70:
    print("Anda harus mengulang ujian teori dan praktek.")
