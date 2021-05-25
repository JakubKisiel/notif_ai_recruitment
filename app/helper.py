import random
import hashlib

def generate_salt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    return "".join(chars)
def generate_hash(string_to_hash: str):
    return hashlib.sha256(string_to_hash.encode()).hexdigest()

