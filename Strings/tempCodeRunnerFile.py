x = str(input("Input a string to calculate no of alpha,no,symbols and spaces:"))
count = 0
count1 = 0
c2=0
c3=0

for i in x:
    if i.isalpha() :
        count += 1
    elif i.isnumeric():
        count1 +=1
    elif i.isspace():
        c2 +=1
    else :
        c3 +=1

print(f"No of alphabets are {count},numbers are {count1}, symbols are {c3} and spaces are {c2}")