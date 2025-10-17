import random as rd
import datetime as dt
list1=[1,2,3,4,5,6,10]
list2=[7,8,9]
f1=open("labexams.txt","a")
today1=dt.datetime.now()
print(today1)
y1=today1.year
M1=today1.month
d1=today1.day
h1=today1.hour
m1=today1.minute
s1=today1.second
today2=str(y1)+str(M1).zfill(2)+str(d1).zfill(2)+"_"+str(h1).zfill(2)+str(m1).zfill(2)+str(s1).zfill(2)
print(today2)
f1.write(today2+"\n")
str1="Please answer any one question each from Section A and Section B"
str2="Wish you the very best"
usn1=int(input('Enter starting usn:'))
print(str1)
for i in range(0,4,1):
    ques=[]
    q1=rd.choice(list1)
    q2=rd.choice(list2)
    info1=str(usn1+i)+'-'+str(q1)+','+str(q2)+"\n"
    f1.write(info1)
    print('Projects for',usn1+i,'-',q1,q2)
f1.write("\n")
print(str2)
f1.close()
