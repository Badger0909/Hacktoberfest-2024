def caesar_cipher(text, shift, encode=True):
    shift = shift % 26 * (1 if encode else -1)
    result = []

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    try:
        text = input("Enter text: ")
        shift = int(input("Enter shift (1-25): "))
        
        encoded_text = caesar_cipher(text, shift)
        print(f"Encoded: {encoded_text}")
        
        decoded_text = caesar_cipher(encoded_text, shift, encode=False)
        print(f"Decoded: {decoded_text}")

    except ValueError:
        print("Please enter a valid integer for the shift value.")
