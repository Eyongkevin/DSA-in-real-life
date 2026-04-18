import random
import string

def generate_words(n):
    words = []
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=8))
        words.append(word)
    return words