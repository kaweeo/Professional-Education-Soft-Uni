def char_in_range():
    a = input()
    b = input()

    for symbol in range (ord(a) + 1, ord(b)):
        if symbol == ord(b):
            print(chr(symbol))
        else:
         print(chr(symbol), end=" ")

char_in_range()