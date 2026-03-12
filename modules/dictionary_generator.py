import itertools
import re

def generate_dictionary(name="", dob="", phone="", patterns=True):

    wordlist = set()

    if phone and not re.fullmatch(r"\d{10}", phone):
        print("Invalid phone number. Must be exactly 10 digits.")
        phone = ""

    base = [w for w in [name.lower(), name.capitalize(), dob, phone] if w]

    if patterns:
        for combo in itertools.permutations(base, 2):
            wordlist.add("".join(combo))

    if phone:
        wordlist.update([
            phone,
            phone[-4:],
            phone[-6:],
            name + phone[-4:],
            name + phone[-6:],
            phone + name,
            name.capitalize() + phone[-4:]
        ])

    mutations = []

    for word in wordlist:

        if len(word) < 3:
            continue

        mutations.extend([
            word,
            word + "123",
            word + "@",
            word.replace('a','@').replace('e','3').replace('o','0').replace('i','1').replace('s','$'),
            word.upper(),
            word.capitalize()
        ])

        if phone:
            mutations.extend([
                word + phone[-4:],
                word + phone[-6:]
            ])

    return list(set(mutations))


def save_wordlist(words, filename="wordlists/generated.txt"):

    with open(filename, "w") as f:
        for w in words:
            f.write(w + "\n")
