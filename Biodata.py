Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Height = float(input("Enter your height: "))
Weight = float(input("Enter your weight: "))

Biodata = "My name is {}, i am {} years old, my height is {:.2f} cm and my weight {:.2f} kg". format(Name, Age, Height, Weight)
print(Biodata)