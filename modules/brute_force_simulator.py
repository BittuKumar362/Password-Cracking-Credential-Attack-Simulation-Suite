
import hashlib
import itertools
import string
import time


def dictionary_attack(target_hash, wordlist_path):

    attempts = 0

    try:
        with open(wordlist_path) as f:
            for word in f:

                password = word.strip()
                attempts += 1

                hashed = hashlib.md5(password.encode()).hexdigest()

                if hashed == target_hash:
                    return password, attempts

    except FileNotFoundError:
        print("Wordlist not found")

    return None, attempts


def brute_force(target_hash, max_length=4, wordlist="wordlists/generated.txt"):

    charset = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    attempts = 0
    start = time.time()

    print("\nRunning dictionary attack...")

    password, dict_attempts = dictionary_attack(target_hash, wordlist)

    attempts += dict_attempts

    if password:
        return password, attempts, time.time() - start

    print("Dictionary attack failed. Starting brute force...\n")

    for length in range(1, max_length + 1):

        print(f"Trying length {length}")

        for guess in itertools.product(charset, repeat=length):

            attempts += 1
            password = "".join(guess)

            hashed = hashlib.md5(password.encode()).hexdigest()

            if hashed == target_hash:
                return password, attempts, time.time() - start

    return None, attempts, time.time() - start
