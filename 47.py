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
