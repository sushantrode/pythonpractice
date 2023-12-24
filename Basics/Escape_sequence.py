"""Escape sequence are used to print statement in the certain way. They are always used within double quotes
Examples are \, \\,\n,\t,\b,\',\\"
\t add 4 spaces
"""
print("Hello World \nThis is new line")

print('Hello "world"')
# This works ' and " " vice versa . use of end indicate we append defined "" and attach next print statement if any
print("'Hello world'")  # This works ' and " " vice versa

print('"Hello world"')  # Output is "Hello world"

print(" \\\Hello world")  # Output is \\Hello world
print(" \\Hello world")  # Output is \Hello world
print('Hello "world"', end="")
# Use of end indicate we append defined "" and attach next print statement if any
print("sushant")
