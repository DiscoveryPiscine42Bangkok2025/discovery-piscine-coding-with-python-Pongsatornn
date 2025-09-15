first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
mult  = first_number*second_number
print(f"{first_number} x {second_number} = {mult}")
if mult < 0 :
    print("This number is negative.")
elif mult > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
