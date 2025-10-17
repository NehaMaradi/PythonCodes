prison=['c','c','c','c','c','c','c','c','c','c']
for i in range(0,10,1):
    prison[i]='o'
print(prison)

for i in range(1,10,2):
    prison[i]='c'
print(prison)

for j in range(2,5,1):
    for i in range(j,10,j+1):
        if(prison[i]=='o'):
            prison[i]='c'
        else:
            prison[i]='o'
    print(prison)

