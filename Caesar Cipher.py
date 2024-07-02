def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether it's an uppercase or lowercase letter
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def main():
    user_input = input("Enter your message: ")
    shift_value = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
    
    encrypted_text = caesar_cipher(user_input, shift_value)
    print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
