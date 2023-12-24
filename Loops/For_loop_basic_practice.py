# Calculate the sum of all the numbers from 1 to 10.
sum = 0
for i in range(1, 11):
    sum += i

print(f"Sum of all no between 1 to 10 is {sum}")

# Calculate product of all the numbers from 1 to 10.

product = 1
for i in range(1, 11):
    product *= i

print(f"Product of all no between 1 to 10 is {product}")

# Calculate how many numbers are divisible by 7 from 1 to 100.

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1

print(f"Count of numbers divisible by 7 from 1 to 100 is {count}")

# Factorial of a number means product of all the numbers from 1 to that number
num = int(input("Enter the no for factorial : "))
product = 1
for i in range(num, 0, -1):
    product *= i

print(f"Factorial of the {num}! is {product}")

# Ask a number from user. Print the multiplication table of that number.
num = int(input("Enter the no for Multiplication table : "))
print(f"The multiplication table for {num} is as follows :")
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
