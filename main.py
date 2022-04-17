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
  
  def Make_Sound(message):



    import winsound



    import time



    frequence = 600



    duration = 200



    for cipher in message:



         if cipher == '.':



           winsound.Beep(frequence, duration)



         elif cipher == '-':



           winsound.Beep(frequence, 3*duration)



         elif cipher == ' ':



           time.sleep(0.5*3*duration/1000)



         elif cipher == ',':



           time.sleep(0.5*7*duration/1000)



         else:



           winsound.Beep(2*frequence, 3*duration)




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
