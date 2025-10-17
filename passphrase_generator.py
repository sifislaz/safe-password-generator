import secrets
import os.path

class PassphraseGenerator:
    def __init__(self, num_words):
        self._load_wordlist()
        self._passphrase = None
        self._dice = (1,2,3,4,5,6)  # Simulating a six-sided dice
        if num_words < 4 or num_words > 8:
            raise ValueError("Number of words must be between 4 and 8 for a secure passphrase.")
        self._num_words = num_words
        

    def _load_wordlist(self):
        """
        Load the EFF large wordlist from a text file.
        """
        wordlist = {}
        filename = os.path.join(os.getcwd(), 'assets',"eff_large_wordlist.txt")
        print(filename)
        with open(filename, 'r') as f:
            for line in f:
                (key, word) = line.strip().split("\t")
                wordlist[key] = word
        self._wordlist = wordlist

    def _roll_dice(self):
        """
        Simulate rolling five six-sided dice to generate a five-digit key.
        """
        return ''.join(str(secrets.choice(self._dice)) for _ in range(5))
    
    def generate(self):
        '''Generate a secure passphrase using the specified number of words.'''
        if not self._wordlist:
            raise ValueError("Wordlist is not loaded.")
        passphrase_words = []
        for _ in range(self._num_words):
            dice_key = self._roll_dice()
            word = self._wordlist[dice_key]
            if word:
                passphrase_words.append(word)
            else:
                raise ValueError(f"No word found for dice key: {dice_key}")
        self._passphrase = '-'.join(passphrase_words)
        return self._passphrase