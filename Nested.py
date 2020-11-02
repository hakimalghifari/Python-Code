for i in range(2):
    print("i: {}" . format(i))
    for j in range(3):
        print("j: {}". format(j))


for row in range(2):
    for column in range(3):
        print("{}.{} ". format(row+1,column+1), end= " ")
    print()

count=1
for row in range(4):
    for column in range(4):
        print(count, end= " ")
        count = count +1
    print()
    