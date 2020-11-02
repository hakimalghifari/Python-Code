#Ex1
fruitnames=[]

def add_fruitnames(name):
    fruitnames.append(name)
    for fruit in fruitnames:
        print(fruit)
    print("-----")
add_fruitnames("Orange")
add_fruitnames("Aple")
add_fruitnames("Melon")

fruitnames.append("Orange")
for fruit in fruitnames:
    print(fruit)
    print("-----")

fruitnames.append("Aple")
for fruit in fruitnames:
    print(fruit)
    print("-----")


#Ex2
def total(x,y):
    total=x+y
    return total

print(total(1,2))
jumlah = total(1,2)
print(jumlah)