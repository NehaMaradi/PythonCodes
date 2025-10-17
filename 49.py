s1="Dear $$name,wish you and your family a very happy Deepavali"
f1=open("names.txt")
names=[]
emails=[]
for i in range(0,5,1):
    s2=f1.readline().strip()
    list1=s2.split(",")
    names.append(list1[0])
    emails.append(list1[1])
for i in range(0,5,1):
    name1=names[i]
    s3=s1.replace("$$name",name1)
    print(s3)
