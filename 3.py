def fact(n):   
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return fact1
n1=6
result=fact(n1)
print(result)
