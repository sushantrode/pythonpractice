# Create patterns using nested loops

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")

    print(end="\n")

# Create patterns using nested loops

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")

    print()  # empty print statement adds input to next line, if we use \n then it adds 2 lines. Alternatively we can use end = "\n" in print statement

# Create patterns using nested loops

for i in range(1, 6):
    for j in range(5, 0, -1):
        print(j, end=" ")

    print(end="\n")

# Create patterns using nested loops

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")

    print(end="\n")

# Create patterns using nested loops

for i in range(5, 0, -1):
    for j in range(1, 6):
        print(i, end=" ")

    print(end="\n")

# Create patterns using nested loops
num = int(input("Enter no of lines you want in pattern : "))

for i in range(1, num + 1):
    for j in range(1, 6):
        print(i, end=" ")

    print(end="\n")

# Create patterns using nested loops
num = int(input("Enter no of lines you want in pattern : "))

for i in range(num, 0, -1):
    for j in range(1, 6):
        print(i, end=" ")

    print(end="\n")
