"""
String methods()
Title,Capitalized,upper,lower,swapcase,isupper,islower,isalpha,isalnum,isspace
"""

a = "sushant rode"
x = a.title()
x = a.capitalize()
x = a.swapcase()  # swap the case upper to lower and vice versa
x = a.islower()  # Output True
x = a.isalnum()  # Check for alpha +numeric , output is false, for symbols
x = a.isdigit()  # Output is False
x = a.isspace()  # All spaces , output is false
print(x)
