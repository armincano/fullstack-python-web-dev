for i in range(6):
    for j in range(i):
        print('* ', end="")
    print("")
    
i=1
while(i<=5):
    j=5
    while(j>=i):
        print(j, end=' ')
        j-=1
    i+=1
    print()