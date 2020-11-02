data = int(input("Berapa data: "))

name_customer = []
age_customer = []

for i in range(data):
 print("Data ke {}". format(i+1))
 name = input("Name : ")
 age = int(input("Age : "))

 name_customer.append(name)
 age_customer.append(age)

for i in range(len(name_customer)):
  print("Customer name {}, aged {} years". format(name_customer[i], age_customer[i]))
  