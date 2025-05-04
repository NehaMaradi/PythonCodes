def fact(n):   
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return fact1
n1=3
n2=8
list1=[]
for i in range(n1,n2+1,1):
    list1.append(fact(i))
print(list1)

