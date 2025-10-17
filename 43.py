prison=['c','c','c','c','c','c','c','c','c','c']
for i in range(0,10,1):
    prison[i]='o'
print(prison)

for i in range(1,10,2):
    prison[i]='c'
print(prison)

for i in range(2,10,3):
    if(prison[i]=='o'):
        prison[i]='c'
    else:
        prison[i]='o'
print(prison)

for i in range(3,10,4):
    if(prison[i]=='o'):
        prison[i]='c'
    else:
        prison[i]='o'
print(prison)

for i in range(4,10,5):
    if(prison[i]=='o'):
        prison[i]='c'
    else:
        prison[i]='o'
print(prison)


