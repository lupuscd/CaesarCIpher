def encryption(message, key):
    """Encrypts given message"""

    symbols = 'abcdefghijklmnopqrstuvwxyz0123456789 !.?@#$%^&*()<>'
    encrypted = ''

    for symbol in message:
        if symbol in symbols:
            symbolindex = symbols.find(symbol)
            encryptedindex = symbolindex + key

            if encryptedindex > len(symbols):
                encryptedindex = encryptedindex - len(symbols)

            encrypted = encrypted + symbols[encryptedindex]

        else:
            # add the symbol without changing it
            encrypted = encrypted + symbol
    return encrypted
