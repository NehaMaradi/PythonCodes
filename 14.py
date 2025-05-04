f2=open("friends.txt",'w')
for i in range(1,21,1):
    f2.write('friend'+str(i)+'\n')
f2.close()
