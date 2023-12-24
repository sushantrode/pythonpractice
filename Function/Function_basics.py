"""
Function return null case
def addition (n1,n2):
   total = n1+n2
   print (total)
Lets call the function
x = addition (100,200)
print(x)
Output : 
300
None  # In this case as the function did not return anything , the value was none
addition (True,True)
addition (True,False)
addition (False,False)
Output :
2 # In python , True =1, False = 0
1
0

Method vs Function
Method is use of function with datatype. a =[], a.append(), append is method
"""


def addition(n1, n2):
    total = n1 + n2
    print(total)


addition(False, False)
