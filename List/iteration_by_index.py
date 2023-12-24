# for val in range, for loop iterates over 0 to n-1 for n set of values. No need to incremant like while loop
my_list = [
    12,
    13,
    45,
    "sushant",
    33.44,
    -23,
    56,
    "rode",
]


for i in range(0, len(my_list)):
    print(my_list[i])

i = 0
x = len(my_list)
# print(x)
while i < x:
    print(my_list[i])
    i = i + 1
