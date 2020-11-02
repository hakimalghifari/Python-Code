list_name = []
list_number= []
print("Welcome! ")
print("    ")
NumberMenu=1
while NumberMenu!=3:
    print("------Menu------")
    print("1. Contact List")
    print("2. Add Contact")
    print("3. Exit ")  
    print("   ")
    NumberMenu=int(input("Choose Menu: "))

    if NumberMenu==1:
      if len(list_name)==0 and len(list_number)==0:
        print("No data")
      else:
         print("Contact List:")
         for x in range(len(list_name)):
             print("Name: ",list_name[x])
             print("Phone Number: ",list_number[x]) 
                      
    elif NumberMenu==2:
     Profile1=str(input("Name: "))
     Profile2=str(input("Phone Number: "))
     list_name.append(Profile1)
     list_number.append(Profile2)
     print("Contact added succesfully!")
    elif NumberMenu==3:
     print("Program finished, bye!")
     break
    elif NumberMenu!=1 or NumberMenu!=2 or NumberMenu!=3:
     print("Menu not available")
    


