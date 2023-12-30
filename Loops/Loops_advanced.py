# Right angle triangle pyramid with 1
k = 10  # No of spaces ,now of rows multiplied by 2 , 1 for character 1 for space end =" ", can work with 1 per space but not asthetic
for i in range(0, 6):
    # add a loop for space

    for j in range(0, k):  # alternative for j in range (i,5)  since the spaces were 5
        print(end=" ")
    k = k - 2

    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Right angle triangle pyramid with *
k = 10  # No of spaces ,now of rows multiplied by 2 , 1 for character 1 for space end =" ", can work with 1 per space but not asthetic
for i in range(0, 6):
    # add a loop for space

    for j in range(0, k):
        print(end=" ")
    k = k - 2

    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# OR Alternative ,  it is much easier but the no stars in a row can be increased by using additional constants
for i in range(1, 6):
    # add a loop for space

    for j in range(i, 5):
        print(
            " ", end=" "
        )  # Spaces are needed for right angle triangle , try putting @ instead to understand

    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#  pyramid with **
k = 10  # No of spaces ,now of rows multiplied by 2 , 1 for character 1 for space end =" ", can work with 1 per space but not asthetic
l = 1
for i in range(0, 6):
    # add a loop for space

    for j in range(0, k):
        print(end=" ")
    k = k - 2

    for j in range(
        1, l + 1
    ):  # alternative-  for j in range (1,i*2), no need to increment
        print("*", end=" ")
    l = l + 2
    print()

# OR Alternative 1
for i in range(1, 6):
    # add a loop for space

    for j in range(i, 5):
        print(
            end=" "
        )  # Additional spaces can be added , but then we need to increase the *. look at alt 2

    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# OR Alternative 2

for i in range(1, 6):
    # add a loop for space adjustment
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(
        1, i * 2
    ):  # The no of stars were increased by i*2, if loop started with 0 then (i*2-1)
        print("*", end=" ")
    print()


#   reverse pyramid with **
k = 0
l = 9  # Need a odd no , as we want 1 star at the end and we are reducing by 2
for i in range(5, 0, -1):
    # add a loop for space
    for j in range(0, k):
        print(end=" ")
    k = k + 2

    for j in range(l, 0, -1):
        print("*", end=" ")
    l = l - 2
    print()

# OR Alternative
for i in range(1, 6):
    # add a loop for space

    for j in range(1, i + 1):
        print(end=" ")

    for j in range(6, i, -1):
        print("*", end=" ")
    print()


#  pyramid with ** and reverse pyramid
k = 10
l = 1
for i in range(0, 5):
    # add a loop for space

    for j in range(0, k):
        print(end=" ")
    k = k - 2

    for j in range(1, l + 1):
        print("*", end=" ")
    l = l + 2
    print()

k = 4
l = 7
for i in range(4, 0, -1):
    # add a loop for space
    for j in range(0, k):
        print(end=" ")
    k = k + 2

    for j in range(l, 0, -1):
        print("*", end=" ")
    l = l - 2
    print()

# OR Alternative
for i in range(1, 6):
    for j in range(6, i, -1):
        print(end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(1, 5):
    # add a loop for space

    for j in range(1, i + 2):
        print(end=" ")

    for k in range(5, i, -1):
        print("*", end=" ")
    print()


#  reverse pyramid   and pyramid with **
k = 2
l = 9
for i in range(5, 0, -1):
    # add a loop for space
    for j in range(0, k):
        print(end=" ")
    k = k + 2

    for j in range(l, 0, -1):
        print("*", end=" ")
    l = l - 2
    print()

k = 10
l = 1
for i in range(0, 5):
    # add a loop for space

    for j in range(0, k):
        print(end=" ")
    k = k - 2

    for j in range(1, l + 1):
        print("*", end=" ")
    l = l + 2
    print()

# Or Alternative

for i in range(1, 6):
    # add a loop for space adjustment

    for j in range(1, i + 1):
        print(end=" ")

    for k in range(6, i, -1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    # add a loop for space adjustment

    for j in range(7, i, -1):
        print(end=" ")

    for k in range(1, i + 1):
        print("*", end=" ")
    print()
