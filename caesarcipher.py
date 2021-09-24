# Caesar Cipher

import random
import encryption as en
import decryption as de


message = input('Enter the message to be encrypted\\decrypted: \n').lower()

while True:
    answer = input('Do you have a specific key to use? y\\n\n').lower()

    if answer == 'y':
        while True:
            key = input('Please enter the key value: \n')
            try:
                if int(key):
                    key = int(key)
                    break

            except ValueError:
                print('Please enter a digit value.\n')
        break

    elif answer == 'n':
        key = random.randint(7, 18)
        break
    else:
        print('Please enter a valid value: y or n\n')

while True:
    mode = input('You want encryption or decryption? Press e or d.\n').lower()

    if mode == 'e':
        enc = en.encryption(message, key)
        with open('encrypted.txt', 'a') as fo:
            add_cont = fo.write(message + ' ' + enc + ' ' + str(key) + '\n')
        break
    elif mode == 'd':
        dec = de.decryption(message, key)
        with open('decrypted.txt', 'a') as fo:
            add_cont = fo.write(message + ' ' + dec + ' ' + str(key) + '\n')
        print(dec)
        break
    else:
        print('Please enter a valid mode: e or d.\n')
