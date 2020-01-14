# caesar cipher

# import pyperclip

message = 'This is my secret message.'
key = 13
mode = 'encrypt'    # set to 'encrypt' or 'decrypt'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrupted) number for this symbol
        num = LETTERS.find(symbol)  # get the number of the symbol
        print(num)
        if mode == 'encrypt':
            num = num + key 
        elif mode == 'decrypt':
            num = num - key 

        # handle the wrap-around if num is larger than length of 
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/ decrypted number's symbol at the end of translated 
        translated = translated + LETTERS[num] 

    else:
        # just add the symbol without encrypting/ decrypting  
        translated = translated + symbol

# print the encrypted/ decrupted string to the screen 
print(translated)

# copy the encrypted/ decrypted string to the clipboard 
# pyperclip.copy(translated)
