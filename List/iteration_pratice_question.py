# Print the list in reverse order
a = [1, 24, -45, -50, 67, 4, 20, 19, 8]
x = len(a) - 1
while x >= 0:
    print(a[x], end=" ")
    x -= 1
# # using For loop for (start,end is exclusive,increment/decrement), thus use -1 instead of 0
for i in range(x, -1, -1):
    print(a[i], end=" ")

# Print the even no from the list

for i in a:
    if i % 2 == 0:
        print(i, end=" ")


# Print the odd no from the list

for i in a:
    if i % 2 != 0:
        print(i)

# Print the values at even index
b = ["ra", 24, "su", -50, 67, 4, 20, 19, 8]
for x in range(0, len(b)):
    if x % 2 == 0:
        print(b[x], end=" ")

# Print the sum of all the no in the list
c = [2, 5, 3, 10, 20]
sum = 0
for x in c:
    sum = sum + x

print(f"The sum of the list of no : {c} is equal to = {sum}")

# Make your own list. Count the number of even numbers present in that list.
c = [2, 5, 3, 10, 20, 45, 33, 50]
count = 0
for x in c:
    if x % 2 == 0:
        count += 1


print(f"No of even elements in the list are {count}")

# Make your own list. Count how many numbers are divisible by both 2 and 5 in that list.
c = [2, 5, 3, 10, 20, 45, 33, 50]
count = 0
for x in c:
    if x % 2 == 0 and x % 5 == 0:
        count += 1


print(f"No of elements divisible by 2 and 5 in the list are {count}")

# Make your own list. Find the sum of all even numbers present in that list
c = [2, 5, 3, 10, 20, 45, 33, 50, 55, 65, 80, 22, 30]
d = []
count = 0
sum = 0
for x in c:
    if x % 2 == 0:
        sum = sum + x
        count += 1
        d.append(x)

print(f"No of even elements list are {count} and they are {d} and their sum is {sum}")

# Make your own list. Find the sum of all numbers divisible by 3 or 4
c = [2, 5, 3, 10, 20, 45, 33, 50, 55, 65, 80, 22, 30]
d = []
count = 0
sum = 0
for x in c:
    if x % 3 == 0 or x % 4 == 0:
        sum = sum + x
        count += 1
        d.append(x)

print(
    f"No of elements divisible by 3 or 4 are {count} and they are {d} and their sum is {sum}"
)

# Make your own list. Print how many positive and negative numbers are here.
c = [2, 5, 3, -10, -20, -45, 33, -50, 55, 65, -80, 22, 30]
d = []
e = []
count_p = 0
count_n = 0

for x in c:
    if x < 0:
        count_n += 1
        e.append(x)
    else:
        count_p += 1
        d.append(x)

print(
    f"No of positive elements {count_p} and negative elements are {count_n} and Positive no are {d} and negative no are {e} "
)

# Make your own list. Print the largest number present in that list.
c = [-2, 5, 3, 10, -20, -45, 33, -50, 55, 65, -80, 22, 30, 1000]
ln = len(c)
x = 0
hg = c[
    0
]  # In case of all the values being zero, initiate the value by first value of list instead of 0

# # Else is optional
while x < ln:
    if hg < c[x]:
        hg = c[x]
    x += 1

print(hg)

# Using for loop , iterate by value
for i in c:
    if hg < i:
        hg = i

print(f"the largest no in the list {c} is {hg} ")


#  Make your own list. Print the smallest number present in that list

c = [-2, 5, 3, 10, -20, -45, 33, -50, 55, 65, -80, 22, 30, 1000, 2000, -4000]

ln = len(c)
x = 0
lw = 0

# # Using while loop
while x < ln:
    if lw > c[x]:
        lw = c[x]

    x += 1

print(lw)

# Using for loop , iterate by index
for i in range(0, ln):
    if lw > c[i]:
        lw = c[i]

print(f"The smallest no in the list {c} is {lw} ")
