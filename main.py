# Python program to implement Morse Code Translator

MORSE_CODE = { 'A':'wow', 'B':'-...',

                    'C':'-.-.', 'D':'-..', 'E':'.',

                    'F':'..-.', 'G':'--.', 'H':'....',

                    'I':'..', 'J':'.---', 'K':'-.-',

                    'L':'.-..', 'M':'--', 'N':'-.',

                    'O':'---', 'P':'.--.', 'Q':'--.-',

                    'R':'.-.', 'S':'...', 'T':'-',

                    'U':'..-', 'V':'...-', 'W':'.--',

                    'X':'-..-', 'Y':'-.--', 'Z':'--..',

                    '1':'.----', '2':'..---', '3':'...--',

                    '4':'....-', '5':'.....', '6':'-....',

                    '7':'--...', '8':'---..', '9':'----.',

                    '0':'-----', ', ':'--..--', '.':'.-.-.-',

                    '?':'..--..', '/':'-..-.', '-':'-....-',

                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):

    cipher = ''

    for letter in message:

        if letter != ' ':


            cipher += MORSE_CODE[letter] + ' '

        else:
            cipher += ' '



    return cipher
  
  def decrypt(message):

    message += ' '

    decipher = ''

    citext = ''

    for letter in message:

        if (letter != ' '):

            i = 0

            citext += letter
            
        else:
 
            i += 1

            if i == 2 :

                decipher += ' '
        
            else:

                decipher += list(MORSE_CODE.keys())[list(MORSE_CODE

                .values()).index(citext)]

                citext = ''

    return decipher



def main():



    message = "Ne jemi grupi i pare ne lenden siguria e te dhenave"



    result = encrypt(message.upper())



    print (result)

    message = "-. .  .--- . -- ..  --. .-. ..- .--. ..  ..  .--. wow .-. .  -. .  .-.. . -. -.. . -.  ... .. --. ..- .-. .. wow  .  - .  -.. .... . -. wow ...- . "



    result = decrypt(message)



    Make_Sound(message)



    print (result)







if __name__ == '__main__':



    main()
