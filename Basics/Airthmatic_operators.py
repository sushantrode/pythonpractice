"""
In python, left hand value(x) % right hand value(y), if x<y then rem is x 
'/' division gives answer in float and '//' floor division gives answer in int or rounded down to lowest integer 
and in negative higher is less. For example, -2.5 is rounded down to its lowest integer i.e. -3
x+=3 is x=x+3, x**=2 mean x = x**2 

"""

x = -10
y = 4
s = 22
d = 7
d1 = s / d
d2 = round(d1, 2)
z = x / y
z1 = x // y

print(f"division is {z} and its float")
print(f"Floor division is {z1} and its integer to lowest value")
# To print no upto 2 decimal use format as {var : .2f}  , 2 is required no of decimals

print(f"Pi Value derived using the round function {d2}")
print(f"Value of pie derived using the var : .2f  method is : {d1:.2f}")
