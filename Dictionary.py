customer= {"Name" : "Hakim",
           "Age" : 21
}
customer2= {"Name" : "Alghi",
            "Age" : 22
}
for key in customer:
    print(key)
    print(customer[key])
for key in customer2:
    print(key)
    print(customer2[key])
    

list_customer = []
list_customer.append(customer)
list_customer.append(customer2)

for customer in list_customer:
    print("Name : {}". format(customer["Name"]))
    print("Age : {}". format(customer["Age"]))



