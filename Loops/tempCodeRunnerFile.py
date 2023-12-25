k = 2 
l = 9
for i in range (5,0,-1):
    # add a loop for space     
    for j in range (0,k):
        print(end= " ")
    k = k +2

    for j in range (l,0,-1):
        print('*',end = " ")
    l = l-2
    print()

k = 10  
l = 1
for i in range (0,5):
    # add a loop for space 
    
    for j in range (0,k):
        print(end= " ")
    k = k -2

    for j in range (1,l+1):
        print('*',end = " ")
    l = l+2
    print()