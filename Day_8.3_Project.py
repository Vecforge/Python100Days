import ASCII_art as cca
import word_list as wl

def caesar_cipher():
    # Displaying ASCII art for Caesar Cipher
    print(cca.cc_art)

    # Control variable for number of iterations of Caesar Cipher
    go_again = True

    while go_again:
        # Accepting command for encrypting or decrypting data:
        inp = input("Type \'encode\' to encrypt, or \'decode\' to decrypt: ")
#-----------------------------------------------------------------------------------
        # Encoding part of the Cipher:
        if inp == "encode":
            #Accepting plaintext and Shift number for encoding
            plain_txt = input("Enter the message to encrypt without spaces: ").lower()
            shift_number = int(input("Enter the shift number: "))

            cipher_text = []
            plain_text_list = list(plain_txt)

            for i, ptt in enumerate(plain_text_list):
                ptt_ascii = ord(ptt)
                j = ptt_ascii % 97
                plain_text_list[i] = wl.alphabet_list[(j + shift_number) % 25]
            print("Here's the encoded result: " + "".join(plain_text_list))
#------------------------------------------------------------------------------------
        # Decoding part of the Cipher:
        elif inp == 'decode':
            cipher_text = input("Enter the text to decrypt: ").lower()
            shift_number = int(input("Enter the shift number: "))

            plain_text = []
            cipher_text_list = list(cipher_text)

            for i in cipher_text_list:
                ctt_ascii = ord(i)
                idx = ctt_ascii % 97
                plain_text.append(wl.alphabet_list[(idx - shift_number) % 25])
            print("Here's the decoded result: ", "".join(plain_text))
#------------------------------------------------------------------------------------
        go_again_yn = input("Type \'yes\' if you want to go again. Otherwise, type \'no\': ")

        if go_again_yn in ('no', 'No'):
            go_again = False

# Driver Code:
caesar_cipher()