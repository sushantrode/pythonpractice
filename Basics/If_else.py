# Find the largest no out of the input given by user

num1 = int(input("Enter 1st no :"))
num2 = int(input("Enter 2nd no :"))
num3 = int(input("Enter 3rd no :"))

if num1 > num2:
    if num1 > num3:
        print(f"Largest no is number 1: {num1}")
elif num2 > num3:
    if num2 > num1:
        print(f"Largest no is number 2: {num2}")
else:
    print(f"Largest no is number 3 :{num3}")
