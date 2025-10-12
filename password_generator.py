import secrets
import string
import math

class PasswordGenerator:


    def __init__(self, length=12, uppercase=True, digits=True, special_chars=True):
        self._password = None
        self._character_pool = []  # List to hold character sets
        self._pool_size = 0
        if length < 8 or length > 64:  # Safety recommendations
            raise ValueError("Password length must be between 8 and 64 characters.")
        self._length = length
        if uppercase:
            self._character_pool.append(string.ascii_uppercase)
            self._pool_size += len(string.ascii_uppercase)
        if digits:
            self._character_pool.append(string.digits)
            self._pool_size += len(string.digits)
        if special_chars:
            self._character_pool.append(string.punctuation)
            self._pool_size += len(string.punctuation)
        self._character_pool.append(string.ascii_lowercase)
        self._pool_size += len(string.ascii_lowercase)
    

    def generate(self):
        if not self._character_pool:
            raise ValueError("No valid characters available for password generation.")
        password = ''.join(secrets.choice(secrets.choice(self._character_pool)) for _ in range(self._length))  # Ensure at least one character from each set is included
        self._password = password


    def get_password(self):
        if self._password is None:
            raise ValueError("Password has not been generated yet. Call generate() first.")
        return self._password
    

    def get_entropy(self):
        if self._password is None:
            raise ValueError("Password has not been generated yet. Call generate() first.")
        entropy = math.log2(math.pow(self._pool_size, self._length))  # Entropy in bits
        return entropy