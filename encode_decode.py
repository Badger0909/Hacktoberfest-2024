def caesar_encode(text, shift):
    encoded_text = ""
    
    for char in text:
        if char.isalpha():
            # Shift the character and wrap around the alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encoded_text += encoded_char
        else:
            # Non-alphabetic characters remain unchanged
            encoded_text += char

    return encoded_text

def caesar_decode(text, shift):
    return caesar_encode(text, -shift)  # Decoding is just encoding with the negative shift

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the text to encode: ")
    shift = int(input("Enter the shift value (1-25): "))

    encoded = caesar_encode(plaintext, shift)
    print(f"Encoded text: {encoded}")

    decoded = caesar_decode(encoded, shift)
    print(f"Decoded text: {decoded}")
