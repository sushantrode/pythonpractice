# Methods like len(),index()=return index, sort()- sort in ascending order, can't sort mix of no and str,
#  reverse(),append(),remove(value)- remove by value, pop(index)-remove by index default is last
# extend()-add the elements from the iterable(list,tuple,sets,stringsetc)
# count(value)- count the value in list, insert(index,value)

a = [12, 13, 15.1, 3, 34, 60, 2, 1, -13]

a.sort()  # Sort the values , does not return anything
print(a)

a.reverse()  # Reverse the list irrespective of order
print(a)

a.sort(reverse=True)  # Easier way to sort the list in descending order
# a.append(["sush", "rode"])
print(a)
a.extend(["sush", "rode"])
print(a)

# Copy of one list to other copy() - creates a copy. Assignment operator works like change in list to other, list1 = list2

a = [12, 13, 15.1, 3, 34, 60, 2, 1, -13]
b=[]
# b=a
b= a.copy()
print(id(a))
print(id(b))
print(b)

a[1] = -1000

print(b)
print(a)

# Slicing of a list is like running the for(start,end) loop , the end is excluded or loop runs till last digit minus step
# same for slicing left to right a[0:4], this is a for loop with default step as 1, so this loops runs for values upto end-1
# a[0:8:2], every 2nd digit is skipped, 2 is step here
# to slice list without using negative, step is negative a[4:1:-1], slices list from Right ot left
# a [: : -1], slice the list entirely from right to left or reverses the list
# a [>len(a)//2], slice the list in half

