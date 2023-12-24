""" 
Write a program that prompts the user to specify the length of a list
and then requests numbers to populate that list. Display the final list as
the output 
"""
len = int(input("Enter the length of the list : "))
a = []

while len > 0:
    p = int(input("Enter the number:"))
    a.append(p)
    len -= 1

print(f"The list is {a}")

""" 
Create a list and prompt the user for an 'old number' followed by a
'new number.' If the 'old number' exists in the list, replace it with the 'new
number' provided by the user.

"""

a = [5, 15, 20, 30, 15]

print(f"The list is {a}")

old = int(input("Enter the item you want to replace : "))
new = int(input("Enter the item you want to replace with : "))

for i in range(0, len(a)):
    if a[i] == old:
        a[i] = new

print(a)

# Below logic works for only first iteration. Not for duplicate values
if p in a:
    q = int(input("Enter the item you want to replace with : "))
    ind = a.index(p)
    a.remove(p)
    a.insert(ind, q)
    print(f"The updated list is {a}")
else:
    print("The no does not exist in list")


# Remove all the even numbers from the list.

a = [45, 66, 66, 66, 66, 78, 11, 11, 12, 12, 12]
b = []


for i in a:
    if i % 2 == 0:
        b.append(i)

for j in b:
    if j in a:
        a.remove(j)

print(a)


# Find the no's divisible in the list from the user input.

a = [5, 15, 20, 32, 16]
b = []

x = int(input("Enter the no to be divisible  the list with : "))

for i in a:
    if i % x == 0:
        b.append(i)

print(b)

# Seperate the list of even and odd no from the list

a = []
b = []
c = []
print("Please create a list of odd and even no ")
x = "yes"


while x == "yes":
    y = int(input("Enter a no :"))
    a.append(y)
    x = str(input("Do you wish to continue,yes/no : "))

for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

print("Orginal list : ", a)
print("Even no : ", b)
print("Odd no : ", c)

# Merge two list

d = b + c
print("Merged list : ", d)

# Make a list of your own. And remove all the duplicates element from that list

a = [5, 15, 20, 32, 16,20,32,5,5,10,10,10]
b=[]

for i in a :
    if i not in b :
        b.append(i)
       
a.sort()
print(a)
b.sort()
print(b)
        
# Find the average of all the no in the list 

a = [5, 15, 20, 5,5]
sum = 0
for i in a :
    sum = sum+i

print (f"The average of the list is : {sum//len(a)}") #// gives me an integer numerator

# Find the second largest number from the un sorted list

a = [5, 15, 20, 32, 16,20,32,5,5,10,10,10,87,98,99,30,60,101]

largest = float ("-inf") # This defines negative infinity
s_large = float ("-inf") 

for i in a :
    if i > largest :
        s_large = largest    #Since the list is not sorted we need to assign s large = largest
        largest = i
    elif i > s_large and i < largest :
        s_large = i

print(s_large)

# find all the prime no from the list

a = [5, 15,87,98,99,30,60,101]
b = []

for num in a :
    factors =0
    for i in range(1,num+1):
        if num%i == 0 :
            factors = factors+1
    if factors == 2 :
        b.append(num)

print (f"The prime no are : {b}")

# Split the list in 2 halves
a = [5, 15,87,98,99,30,60,101,112,12]
b=[]
c=[]

for i in range(0,len(a)//2) :
    b.append(a[i])

for i in range (len(a)//2,len(a)):
    c.append(a[i])

print(b)
print(c)

# Swap the first and last 
a = [5, 15,87,98,99,30,60,101,112,'sush']
b=a.copy()
b[-1] = a[0]
b[0] = a[-1]

print (a)
print(b)

# Reverse list using slicing
a = [5, 15,87,98,99,30,60,101,112,'sush']

b= a[-1: :-1]
print (b)

# Print every 3rd no in the list
a = [5, 15,87,98,99,30,60,101,112,'sush']
for i in range (1,len(a)+1):
    if i%3==0 :
        print(a[i-1])

# Split the list in 2 halves using slicing
a = [5, 15,87,98,99,30,60,101,112,'sush']
b = a[0:len(a)//2]
c= a[len(a)//2:len(a)]

print(b)
print(c)
print(d)








        



    





