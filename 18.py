import random as rd
list1=[1,2,3,4,5,6,10]
list2=[7,8,9]

master=[]
str1="Please answer any one question each from Section A and Section B"
str2="Wish you the very best"
usn1=int(input('Enter starting usn:'))
print(str1)
for i in range(0,4,1):
    ques=[]
    q1=rd.choice(list1)
    q2=rd.choice(list2)
    pair=q1,q2
    ques.append(pair)
    master.append(pair)
    print('Projects for',usn1+i,'-',q1,q2)
print(str2)
print(master)
