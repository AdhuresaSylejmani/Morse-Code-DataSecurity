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