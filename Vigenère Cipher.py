# Written By Om [byt-ctrl]
""" Vigenere Cipher Program """


import re  # Constant expression for important validation

# encrypt the text using the Vigenère cypher.
def encrypt (plain_text,key) :
    
    encryption_text = ''
    key=key.upper()  # Convert the key to uppercase for convenience.
    key_length=len(key)
    key_index=0  # Record the present whereabouts of the key.
    
    for char in plain_text :
        if char.isalpha() :  # Encrypt just letters and digits.
            # Find the shift by knowing whether the letter is lowercase or uppercase.

            shift_base=65 if char.isupper() else 97
            key_char=key[key_index%key_length]  # Acquire the corresponding key character.
            shift=ord(key_char)-65  # Find the shift value of the key character.
            

            """  Encrypt the character using the Vigenère cipher technique.

               MAIN LOGIC
            """
                    
            encrypted_char=chr((ord(char)-shift_base+shift)%26+shift_base)
            encryption_text+=encrypted_char
            key_index+=1  # Proceed to the next significant character.

        else :
            encryption_text+=char  # The non-alphabetic characters stay the same.

    return encryption_text


# Use the Vigenère cipher to decrypt the message.

def decrypt(encryption_text,key) :
    decryption_text=''
    key=key.upper()  # Switching the key to uppercase for convenience.
    key_length=len(key)
    key_index=0  # Note where the key is at any given time.

    
    for char in encryption_text :
        if char.isalpha() :  # Only decrypt characters in the alphabet

           # Check to see if the letter is uppercase or lowercase to determine the shift.

            shift_base=65 if char.isupper() else 97
            key_char=key[key_index % key_length]  # Get the corresponding key character
            shift=ord(key_char)-65  # Determine the key character's shift value.

            
            # Use the Vigenère cipher algorithm to decrypt the character.
            decrypted_char=chr((ord(char)-shift_base-shift)%26+shift_base)
            decryption_text+=decrypted_char
            key_index+=1  # Go on to the following important character.

        else :
            decryption_text+=char  # Characters that are not alphabetic remain the same.


    return decryption_text


# Key validation function (alphanumeric characters only)
def validation_key(key) :

    if not re.match("^[A-Za-z0-9]+$",key) :  #Determine whether the key is alphanumeric.
        raise ValueError("The key can only contain letters and numbers .")
    return key.upper()  # For consistency, change the key to uppercase.



# Primary function of the software (MAIN PROGRAM)
def main() :
    print()
    print("Program for Vigenère Cipher Encryption and Decryption")
    
    while True :
        print("\nChoose an option:")
        print("1. Encrypt a message ?")
        print("2. Decrypt a message ?")
        print("3. Exit ?")
        
        choice=input("Enter your choice (1 , 2 , or 3)--> ")

        if choice=='3':
            print("Exiting program......./")
            break
        
        if choice not in ['1','2']:
            print("Invalid Choice . Please Enter 1 to encrypt , 2 to decrypt , 3 to exit .")
            continue

        
        message=input("Enter the message --> ")
        if not message:
            print("Message Box Cannot be empty . Please enter a valid number")
            continue
        


        # Validate the key entered by the user
        while True :
            try :
                key=input("Enter the key (only letters and numbers allowed) --> ").strip()
                if not key:
                    print("Key cannot be empty. Please enter a valid key.")
                    continue
                validation_key(key)  # Validate the key
                break  # Exit the loop if the key is valid
            except ValueError as err :
                print(err)  # Display error message if the key is invalid



        # Depending on the user's preference, either encrypt or decrypt
        if choice=='1':
            # Encrypt the message
            encryption_message=encrypt(message, key)
            print(f"Encrypted message --> {encryption_message}")

        elif choice=='2' :
            # Decrypt the message
            decryption_message = decrypt(message, key)
            print(f"Decrypted message --> {decryption_message}")


main() # Calling Main Function

# END
