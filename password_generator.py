import secrets
import string

class PasswordGenerator:
    def __init__(self, length=12, uppercase=True, digits=True, special_chars=True):
        if length < 8 or length > 64:  # Safety recommendations
            raise ValueError("Password length must be between 8 and 64 characters.")
        self._length = length
        self._uppercase = uppercase
        self._digits = digits
        self._special_chars = special_chars
        self._character_pool = self._create_character_pool()

    def _create_character_pool(self):
        pool = ''
        if self._uppercase:
            pool += string.ascii_uppercase
        if self._digits:
            pool += string.digits
        if self._special_chars:
            pool += string.punctuation
        pool += string.ascii_lowercase  # Always include lowercase letters
        return pool
    def generate(self):
        if not self._character_pool:
            raise ValueError("No valid characters available for password generation.")
        password = ''.join(secrets.choice(self._character_pool) for _ in range(self._length))
        return password