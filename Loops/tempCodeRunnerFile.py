for i in range(1, 6):
    # add a loop for space

    for j in range(i, 5):
        print(
            " ", end=" "
        )  # Spaces are needed for right angle triangle , try putting @ instead to understand

    for j in range(1, i + 1):
        print("*", end=" ")
    print()