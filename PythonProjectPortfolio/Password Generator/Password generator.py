import secrets
import string
import datetime

def generate_strong_password(length=16):
    """
    Generates a cryptographically secure random password.
    
    Args:
        length (int): The desired length of the password.
        
    Returns:
        str: A strong, randomly generated password.
    """
    # Define the character sets
    alphabet = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure the password contains at least one character from each set
    password = [
        secrets.choice(alphabet.lower()),
        secrets.choice(alphabet.upper()),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]
    
    # Combine all character sets for the rest of the password
    all_chars = alphabet + digits + special_chars
    
    # Fill the remaining length with random characters from the combined set
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))
    
    # Shuffle the list to ensure randomness and convert it to a string
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

def save_password_to_file(password, name, filename="passwords.txt"):
    """
    Saves a password with a timestamp and a user-defined name to a text file.
    
    Args:
        password (str): The password to be saved.
        name (str): The name or description for the password.
        filename (str): The name of the file to save to.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] - {name}: {password}\n"
    
    try:
        # Use 'a' mode to append to the file, and 'with' for auto-closing
        with open(filename, "a") as f:
            f.write(entry)
        print(f"Password for '{name}' saved to {filename}")
    except IOError as e:
        print(f"Error: Could not write to file {filename}. {e}")

def main():
    """
    Main function to run the password generator.
    """
    try:
        length = int(input("Enter the desired password length (e.g., 16): "))
        if length < 8:
            print("Password length should be at least 8 for security.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Get the name for the password
    password_name = input("Enter a name for this password (e.g., 'Google Account'): ")

    # Generate and display the password
    new_password = generate_strong_password(length)
    print(f"\nGenerated password: {new_password}")
    
    # Save the password to a file
    save_password_to_file(new_password, password_name)

if __name__ == "__main__":
    main()

