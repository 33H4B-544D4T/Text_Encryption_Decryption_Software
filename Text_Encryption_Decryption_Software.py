import random
from IPython.display import clear_output as cls

choice = ''
message = ''
cls_choice = ''

ascii_characters = [chr(x) for x in range(32,127)]

while str(choice) != '0':
    shuffled_list = [chr(x) for x in range(32,127)]
    result = ''
    
    choice = input("\nDo you want to Encrypt or Decrypt the Message?\n Enter 1 to Encrypt, 2 to Decrypt or 0 to Exit Program: ")

    if str(choice) == '1':
        message = input('\nEnter Message for Encryption: ')
        
        seed_val = input('Enter an Integer to use as a Seed: ')
        random.seed(seed_val)
        random.shuffle(shuffled_list)

        for index in range(0, len(message)):
            result += shuffled_list[ascii_characters.index(message[index])]

        print(f'\nEncoded Message: {result} \n\n')
        
        cls_choice = input("Clear Screen? Answer (Y/N): ").upper()
        if cls_choice == 'Y':
            cls()
            
    elif str(choice) == '2':
        message = input('\nEnter Message to Decrypt: ')

        seed_val = input('Enter an Integer to use as a Seed (should be the same one used to encrypt): ')
        random.seed(seed_val)
        random.shuffle(shuffled_list)

        for index in range(0, len(message)):
            result += ascii_characters[shuffled_list.index(message[index])]

        print(f'\nDecoded Message: {result} \n\n')
        
        cls_choice = input("Clear Screen? Answer (Y/N): ").upper()
        if cls_choice == 'Y':
            cls()

    elif str(choice) != '0':
        print('Invalid Input, please try again. \n\n')
        
else:
    print("\n\nThanks for using the Algorithm.")