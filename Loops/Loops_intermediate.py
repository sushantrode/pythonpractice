"""
Pattern 1
1
12
123
1234
12345
for loop if start and stop values are same then its empty run for eg for (2,2), so we need 1 additional
i determines the no of row. But what is printed in the row is j if different values.
if same values in all row like 1111,2222 etc we print i

"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""
Pattern 2
1
22
333
4444
55555
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
"""
Pattern 3
1
21
321
4321
54321
"""
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
"""
Pattern 4
5
54
543
5432
54321
"""
# Option 1 :
for i in range(5, 0, -1):
    print("5", end=" ")
    for j in range(4, 5 - i, -1):
        print(j, end=" ")
    print()

# Option 2. This is better. i determines the no of row. But what is printed in the row is j if different values.
for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()
"""
Pattern 5
5
44
333
2222
11111
"""
for i in range(5, 0, -1):
    print(i, end=" ")
    for j in range(5, i, -1):
        print(i, end=" ")
    print()

"""
Pattern 6
Same as ppattern 5 but with *

"""
for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print("*", end=" ")
    print()

"""
Pattern 7
54321
5432
543
54
5
"""
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()

"""
Pattern 8
same as above but with "*"

"""
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print("*", end=" ")
    print()
"""
Pattern 9
55555
4444
333
22
1
"""
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(i, end=" ")
    print()

"""
Pattern 10
54321
4321
321
21
1
"""
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


"""
Pattern 11
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
rows = 5
Start_no = 1
column = 1
for i in range(1, rows + 1):
    for j in range(1, column + 1):
        print(Start_no, end=" ")
        Start_no += 1
    print()
    column += 1
