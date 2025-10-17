def encode1(letter1):
    vowels=["A","E","I","O","U"]
    ascii1=ord(letter1)
    if letter1 in vowels:
        ascii2=ascii1+5
    else:
        ascii2=ascii1+4
    letter2=chr(ascii2)
    print(letter2)
encode1("O")
encode1("A")
encode1("U")
