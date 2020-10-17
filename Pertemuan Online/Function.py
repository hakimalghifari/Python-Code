def myfunction():
    print("Hello function")

myfunction()

#Dengan Argumen contoh1
def myFunction(nama):
    print("Hello {}". format(nama))

myFunction("Hakim")
myFunction("Alghi")
myFunction("Fari")

#Dengan Argumen contoh2
def my_function(namapertama, namaakhir):
    print("Hello {} {}". format(namapertama, namaakhir))

my_function("Hakim", "al ghifari")
my_function("Alghi", "el brochimieus")
my_function("Fari", "no partiro")

#Dengan Argumen contoh3
def my_Function(namapertamaa, namaakhirr=" "):
    print("Hello {} {}". format(namapertamaa, namaakhirr))

my_Function("Hakim", "al ghifari")
my_Function("Alghi", "el brochimieus")
my_Function("Fari")

#Keyword parameter
def my_Functionn(child3, child2, child1):
    print("The youngest child is " + child3)

my_Functionn(child1="anik", child2="unik", child3="annek")
my_Functionn("anik", "unik", "annek")
