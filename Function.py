def myfunction():
    print("Hello function")

myfunction()

#Ex1
def myFunction(name):
    print("Hello {}". format(name))

myFunction("Hakim")
myFunction("Alghi")
myFunction("Fari")

#Ex2
def my_function(firstname, lastname):
    print("Hello {} {}". format(firstname, lastname))

my_function("Hakim", "al ghifari")
my_function("Alghi", "el brochimieus")
my_function("Fari", "no partiro")

#Ex3
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
