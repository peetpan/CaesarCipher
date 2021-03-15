print('''
 ________________________________________
|     _____                              |
|    / ____|                             |
|   | |     __ _  ___  ___  __ _ _ __    |
|   | |    / _` |/ _ \/ __|/ _` | '__|   |
|   | |___| (_| |  __/\__ \ (_| | |      |
|    \_____\__,_|\___||___/\__,_|_|      |                          
|     _____ _       _                    |
|    / ____(_)     | |                   | 
|   | |     _ _ __ | |__   ___ _ __      |
|   | |    | | '_ \| '_ \ / _ \ '__|     |
|   | |____| | |_) | | | |  __/ |        |
|    \_____|_| .__/|_| |_|\___|_|        |
|            | |                         |
|            |_|                         |
|________________________________________|                                 
''')


def encode(msg, shifted_no):
    en_msg = ''
    for i in msg:
        if i.isalpha():
            pos = ord(i) + shifted_no
            if pos > 122:
                pos = pos - 26
            i = chr(pos)
        en_msg += i
    print(f"\nHere's the encoded result: {en_msg}\n")


def decode(msg, shifted_no):
    de_msg = ''
    for i in msg:
        if i.isalpha():
            pos = ord(i) - shifted_no
            if pos < 97:
                pos = pos + 26
            i = chr(pos)
        de_msg += i
    print(f"\nHere's the decoded result: {de_msg}\n")


c = 'yes'
while c == 'yes':
    ip = input('Type \'encode\' to encrypt or \'decode\' to decrypt\n')
    if ip == 'encode':
        msg = input("Enter the Message which you want to encode: ").lower()
        shifted_no = int(input('Enter the Shift Number: '))
        shifted_no %= 26
        encode(msg, shifted_no)
    elif ip == 'decode':
        msg = input("Enter the Message which you want to decode: ").lower()
        shifted_no = int(input('Enter the Shift Number: '))
        shifted_no %= 26
        decode(msg, shifted_no)
    else:
        print('Invalid input')
        continue
    c = input('Enter \'yes\' if you wanna go again otherwise \'no\'\n')
