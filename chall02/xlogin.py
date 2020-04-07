import sys

a = ['.-','-...','-.-.','-..','.','..-.','--.','....', 
    '..','.---','-.-','.-..','--','-.','---','.--.',
    '--.-','.-.','...','-','..-','...-','.--','-..-',
    '-.--','--..']
if len(sys.argv) == 2:
    cadena = (sys.argv[1])
    for str in cadena:
        if (ord(str) != 32 and (ord(str) < 97 or ord(str) > 122)):
            print("Usage: ./xlogin.py <a-zA-Z string>")
            sys.exit()
    if not cadena:
        print("Usage: ./xlogin.py <a-zA-Z string>")
    for str in cadena:
        if (ord(str) > 64 and ord(str) < 91):
            str = chr(ord(str) + 32)
        if (ord(str) == 32):
            print(" ", end="")
            continue
        i = 97
        while (i != ord(str)):
            i = i + 1
        print(a[i - 97], end="")
else:
    print("Usage: ./xlogin.py <a-zA-Z string>")