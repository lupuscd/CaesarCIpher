def decryption(message, key):
    """Decrypt given message"""

    symbols = 'abcdefghijklmnopqrstuvwxyz0123456789 !.?@#$%^&*()<>'
    decrypted = ''

    for symbol in message:
        if symbol in symbols:
            symbolindex = symbols.find(symbol)
            decryptedindex = symbolindex - key

            if decryptedindex < 0:
                decryptedindex = decryptedindex + len(symbols)

            decrypted = decrypted + symbols[decryptedindex]

        else:
            decrypted = decrypted + symbol
    return decrypted
