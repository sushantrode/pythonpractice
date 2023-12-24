c = [5, 3, -10, 20, -45, 33, -50, -80, -4000]

ln = len(c)
x = 0
lw = 0

while x < ln:
    if lw > c[x]:
        lw = c[x]

    x += 1

print(lw)
