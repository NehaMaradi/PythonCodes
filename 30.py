def encode1(letter1):
    vowels=["A","E","I","O","U"]
    ascii1=ord(letter1)
    if letter1 in vowels:
        ascii2=ascii1+5
    else:
        ascii2=ascii1+4
    letter2=chr(ascii2)
    return letter2
def encode2(word1):
    result=""
    len1=len(word1)
    for i in range(0,len1,1):
        letter1=word1[i]
        result=result+encode1(letter1)
    return result

result=encode2("ABC")
print(result)
result=encode2("AEIOU")
print(result)
