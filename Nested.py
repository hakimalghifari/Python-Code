for i in range(2):
    print("i: {}" . format(i))
    for j in range(3):
        print("j: {}". format(j))


for baris in range(2):
    for kolom in range(3):
        print("{}.{} ". format(baris+1,kolom+1), end= " ")
    print()

count=1
for baris in range(4):
    for kolom in range(4):
        print(count, end= " ")
        count = count +1
    print()
    