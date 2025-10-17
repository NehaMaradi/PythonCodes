def encode1(letter1):
    vowels=["A","E","I","O","U"]
    ascii1=ord(letter1)
    if letter1 in vowels:
        ascii2=ascii1+5
    else:
        ascii2=ascii1+4
    letter2=chr(ascii2)
    print(letter2)
word1="ABC"

letter1=word1[0]
encode1(letter1)

letter1=word1[1]
encode1(letter1)

letter1=word1[2]
encode1(letter1)
