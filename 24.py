letter1="C"
vowels=["A","E","I","O","U"]
ascii1=ord(letter1)
if letter1 in vowels:
    ascii2=ascii1+5
else:
    ascii2=ascii1+4
letter2=chr(ascii2)
print(letter2)
