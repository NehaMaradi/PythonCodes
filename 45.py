count=10
prison=['c','c','c','c','c','c','c','c','c','c']
for i in range(0,count,1):
    prison[i]='o'
print(prison)

for i in range(1,count,2):
    prison[i]='c'
print(prison)
print()

for j in range(2,5,1):
    for i in range(j,count,j+1):
        if(prison[i]=='o'):
            prison[i]='c'
        else:
            prison[i]='o'
    print(prison)
