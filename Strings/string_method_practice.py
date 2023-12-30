# Ask a string from user. Count how many alphabets are there in that string

x = str(input("Input a string to calculate alphabets :"))
count = 0

for i in range(0, len(x) - 1):
    # We can simply use i as well
    if x[i].isalpha():
        count += 1
print(f"No of alphabets in the string are : {count}")

# Ask a string from user. Count the number of uppercase and lowercase characters in that String.

x = str(input("Input a string to calculate no of uppercase and lowercase :"))
count = 0
count1 = 0

for i in x:
    if i.isupper():
        count += 1
    elif i.islower():
        count1 += 1

print(
    f"No of Upper case alphabets are {count} and lower case alphabet in the string are  {count1}"
)

# Convert the alphabets to uppercase

x = str(input("Input a string to convert to uppercase  :"))
y = x.upper()
print(y)

# Convert upper to lower and vice versa
x = str(input("Input a string to swapcase  :"))
y = x.swapcase()
print(y)

# Ask a string from user. Print the count of how many alphabets, digits,spaces and symbols (everything else)

x = str(input("Input a string to calculate no of alpha,no,symbols and spaces:"))
count = 0
count1 = 0
c2 = 0
c3 = 0

for i in x:
    if i.isalpha():
        count += 1
    elif i.isnumeric():
        count1 += 1
    elif i.isspace():
        c2 += 1
    else:
        c3 += 1

print(
    f"No of alphabets are {count},numbers are {count1}, symbols are {c3} and spaces are {c2}"
)
