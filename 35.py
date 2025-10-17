n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
for j in range(n1,n2+1,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print()

