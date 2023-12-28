# List comphresion is a faster way and short cut for creating a list over a loop

# Normal
my_list = []

for i in range(1, 21):
    my_list.append(i)

print(my_list)
#  With comphresion
# Part  before is what to add to list , i is the value to be added, it can be even strng, like add '*' 100 times in the list
# Condition can also be added for what to add , here if else is mandatory
my_list = [i for i in range(1, 21)]
print(my_list)
# add * 30 times to list, you are adding a string
my_list = ["*" for i in range(1, 31)]
print(my_list)
# with if ...else for what to add, part before for loop
my_list = [
    "Even" if i % 2 == 0 else "odd" for i in range(1, 20)
]  # Output is even, odd in the list for all the even and odd values respectively
print(my_list)

# Part  after for/range  is when to add or condition , i is the value to be added but when the condition is satisfied
# the condition after for has only if and no else
my_list = [
    i for i in range(1, 21) if i % 2 == 0
]  # Add even no only to the list between 1 and 20
print(my_list)

# Generate a list of squares of numbers from 1 to 10 using list comprehension
my_list = [i * i for i in range(1, 11)]
print(my_list)
# Add the the no of characters in the list using list comphresion

my_list = ["apple", "banana", "kiwi"]

my_list1 = [len(row) for row in my_list]  # Output is (5,6,4)
print(my_list1)

# Using the for loop

my_list = ["apple", "banana", "kiwi"]

c_list = []
for i in my_list:
    c = 0
    for j in i:
        c = c + 1
    c_list.append(c)
print(c_list)

# Repeat the characters 3 times
my_list = ["a", "b", "k"]
my_list1 = [i * 3 for i in my_list]
print(my_list1)

# Create an odd and even list with odd even characters

my_list = [[i, "Even"] if i % 2 == 0 else [i, "Odd"] for i in range(1, 11)]
print(my_list)  # Output ([1,odd], [2, even]...)

# Create nested for loops in it , outer loop is first and then after inner loop and inner loop has condition
# Create a 2X2 matrix. 2 rows and 2 colums, it uses inner loop in [] first then outer loop
# Normal
matrix = []

for i in range(0, 2):
    # append an empty matrix
    matrix.append([])

    for j in range(1, 3):
        matrix[i].append(j)

print(matrix)

# With comphresion

matrix = [
    [j for j in range(1, 3)] for i in range(0, 2)
]  # same result as above, output [[1,2],[1,2]] , inner loop is first

print(matrix)

matrix = [
    j for i in range(0, 2) for j in range(1, 3)
]  # output [1,2,1,2] inner loop is 2nd

print(matrix)

matrix = [
    [j for i in range(0, 2)] for j in range(1, 3)
]  # output [[1,1],[2,2]] inner loop is 2nd

print(matrix)


# Creating a function which is used in inside if


sentence = "The rocket, who was named Ted, came back \
... from Mars because he missed his friends."


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]


# Creating a function which is used in inside if
def get_price(price):
    return price if price > 0 else 0


original_prices = [1.25, 0, 10.22, 3.78, 0, 1.16]
prices = [get_price(i) for i in original_prices]
