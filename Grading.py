Utheory = float(input("Enter the theory exam score "))
Upractice = float(input("Enter the practice exam score "))


if Utheory>=70 and Upractice>=70:
    print("congratulation, you passed!")
elif Utheory>=70 and Upractice<70:
    print("you have to repeat the practice exam.")
elif Utheory<70 and Upractice>=70:
    print("you have to repeat the theory exam.")
elif Utheory<70 and Upractice<70:
    print("you have to repeat the theory and practice exam.")