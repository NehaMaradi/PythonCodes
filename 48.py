def otpGen2(size,qty):
    import random as rd
    n=size
    for i in range(0,qty,1):
        rdn=rd.randint(10**(n-1),(10**n)-1)
        print(rdn)
print("ICICI")
otpGen2(6,10)
print("HDFC")
otpGen2(4,20)
banks=[]
sizes=[]
qtys=[]
f1=open("banks.txt","r")
for i in range(0,4,1):
    s1=f1.readline()
    list1=s1.split(",")
    banks.append(list1[0])
    sizes.append(int(list1[1]))
    qtys.append(int(list1[2]))

otpGen2(sizes[0],qtys[0])
otpGen2(sizes[1],qtys[1])
