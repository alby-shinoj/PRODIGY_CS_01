# Overview:
The Caesar Cipher is a basic encryption technique that shifts each letter in the plaintext by a fixed amount (the “key”) to create the ciphertext.
It’s a type of substitution cipher where each letter is replaced by another letter in the alphabet.

# The caesar_cipher Function:
This function takes two parameters:
text: The input message (plaintext or ciphertext).
shift: The shift value (positive for encryption, negative for decryption).
### It processes each character in the input text:
If the character is an alphabet letter (uppercase or lowercase), it calculates the shifted character.
If the character is not an alphabet letter (e.g., punctuation or space), it remains unchanged.
### The shifted character is determined by:
Finding the base (either ‘A’ or ‘a’) based on the case of the original character.
Applying the shift and wrapping around the alphabet (using modulo 26).
Converting the shifted value back to a character.
The function returns the resulting encrypted or decrypted text.
### The main Function:
This function is the entry point of the program.
It prompts the user to input their message and the shift value.
It calls the caesar_cipher function to perform the encryption or decryption.
Finally, it displays the result.

## Example Usage:
For encryption:
```python
Enter your message: Hello, World!
Enter the shift value (positive for encryption, negative for decryption): 3
Encrypted text: Khoor, Zruog!
```
For decryption:
```python
Enter your message: Khoor, Zruog!
Enter the shift value (positive for encryption, negative for decryption): -3
Decrypted text: Hello, World!
```
