# Right angle triangle pyramid with 1
k = 10  # No of spaces ,now of rows multiplied by 2 , 1 for character 1 for space end =" ", can work with 1 per space but not asthetic
for i in range(0, 6):
    # add a loop for space

    for j in range(0, k):
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


#  pyramid with **
k = 10  # No of spaces ,now of rows multiplied by 2 , 1 for character 1 for space end =" ", can work with 1 per space but not asthetic
l = 1
for i in range(0, 6):
    # add a loop for space

    for j in range(0, k):
        print(end=" ")
    k = k - 2

    for j in range(1, l + 1):
        print("*", end=" ")
    l = l + 2
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
