
# Vigenère Cipher Encryption and Decryption 🛡️

This project implements the Vigenère cipher technique for encrypting and decrypting messages. The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. A key is used to shift the letters in the message.

## Features ✨

The program allows the user to:

1. Encrypt a message using a keyword 🔐.
2. Decrypt an encrypted message using the same keyword 🔓.
3. Validate the key to ensure it only contains alphanumeric characters 🧮.
4. Handle non-alphabetic characters without encryption or decryption 🔠.

## How It Works ⚙️

1. **Encrypting a Message**:
   - The program takes a plain text message and a key.
   - Each character in the message is shifted by the value determined by the corresponding character in the key.

2. **Decrypting a Message**:
   - The program takes an encrypted message and the same key used for encryption.
   - Each character in the encrypted message is shifted back to its original value using the key.

3. **Key Validation**:
   - The key must consist of only letters and numbers.
   - The program will raise an error if the key contains any special characters or spaces.

## Instructions 📝

1. Run the program.
2. Select an option to either encrypt or decrypt a message.
3. Enter your message and a valid key (letters and numbers only).
4. The program will display the encrypted or decrypted message.

---
### Example For both Encryption and Decryption Working.

```python
Program for Vigenère Cipher Encryption and Decryption

Choose an option:
1. Encrypt a message ?
2. Decrypt a message ?
3. Exit ?
Enter your choice (1 , 2 , or 3)--> 1
Enter the message --> Hello World
Enter the key (only letters and numbers allowed) --> secret
Encrypted message --> Zincs Pgvnu

Choose an option:
1. Encrypt a message ?
2. Decrypt a message ?
3. Exit ?
Enter your choice (1 , 2 , or 3)--> 2           
Enter the message -->  Zincs Pgvnu
Enter the key (only letters and numbers allowed) --> secret
Decrypted message -->  Hello World

Choose an option:
1. Encrypt a message ?
2. Decrypt a message ?
3. Exit ?
Enter your choice (1 , 2 , or 3)--> 3 
Exiting program......./
```

---
## 🤝 Contributing :

If u have any idea's feel free to contribute   
Fork the repository if needed , make your changes, and submit a pull request.


## 📜 License :

This project is licensed under the **Apache 2.0 License**.
