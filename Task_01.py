#The First Task (Caesar Cipher) Provided By Prodigy Infotech
#Code By Md Chand(tech-defence)
def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher."""
    return encrypt(text, -shift)

def get_shift():
    """Get a valid shift value from the user."""
    while True:
        try:
            return int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def display_menu():
    """Display the menu options to the user."""
    print("\n~~~Choose Options~~~")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

def main():
    print("*** Welcome to the Caesar Cipher Program! ***")
    
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            message = input("Enter your message to encrypt: ")
            shift = get_shift()
            result = encrypt(message, shift)
            print("Encrypted message:", result)
        elif choice == '2':
            message = input("Enter your message to decrypt: ")
            shift = get_shift()
            result = decrypt(message, shift)
            print("Decrypted message:", result)
        elif choice == '3':
            print("Thank you for using the Caesar Cipher Program!")
            break
        else:
            print("Invalid choice. Please try again.")

# After this here the main() function called
main()
