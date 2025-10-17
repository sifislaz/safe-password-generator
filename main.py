import argparse
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

def parser_setup(parser):
    # Define parser arguments
    parser.add_argument('-l', '--length', type=int, default=12, choices=range(8,65), help='Length of the password (default: 12, min: 8, max: 64)')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters in the password')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits in the password')
    parser.add_argument('-s', '--special-chars', action='store_true', help='Include special characters in the password')
    parser.add_argument('-v', '--version', action='version', version='Password Generator 1.1', help='Show program version and exit')
    parser.add_argument('--passphrase', type=int, choices=range(4,9), default=6, help='Generate a passphrase with the specified number of words (4-8)')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Password Generator", description="Generate a secure password based on specified criteria.")  # Define the parser
    parser_setup(parser)  # Setup the parser with arguments
    args = parser.parse_args()  # Parse the command-line arguments
    print("=========Password Generator=========")
    print("Generating a password and checking its strength ...")
    try:
        if args.passphrase:
            passgen = PassphraseGenerator(num_words=args.passphrase)  # Create a PassphraseGenerator instance
            passphrase = passgen.generate()  # Generate the passphrase
            print(f"Generated Passphrase: {passphrase}")
        else:
            gen = PasswordGenerator(length=args.length, uppercase=args.uppercase, digits=args.digits, special_chars=args.special_chars)  # Create a PasswordGenerator instance
            gen.generate()  # Generate the password
            password = gen.get_password()  # Retrieve the generated password
            entropy = gen.get_entropy()  # Calculate the entropy of the password
            print(f"Generated Password: {password}")
            print(f"Password Entropy: {entropy:.2f} bits")
            if entropy < 50:
                print("The generated password is weak.")
            elif 50 <= entropy < 70:
                print("The generated password is moderate.")
            else:
                print("The generated password is strong.")
    except ValueError as err:
        print(f"Error: {err}")