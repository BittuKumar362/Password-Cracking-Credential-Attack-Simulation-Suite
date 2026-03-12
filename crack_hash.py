from modules.hash_extractor import extract_hash
from modules.brute_force_simulator import brute_force
from modules.password_analyzer import analyze

print("\nHash Cracking Simulation\n")

print("1. Load hash from file")
print("2. Enter hash manually")

choice = input("Select option: ")

if choice == "1":
    # new extractor returns list of dicts
    hash_entries = extract_hash("hashes/hash.txt")
else:
    # simulate single input hash
    single_hash = input("Enter target hash: ")
    hash_entries = [{"hash": single_hash, "algorithm": "Unknown"}]

for h in hash_entries:

    hash_value = h["hash"]
    algo = h.get("algorithm", "Unknown")

    print("\nTarget Hash:", hash_value)
    print("Detected Algorithm:", algo)

    # Use your brute force (max length 4 as before)
    pwd, attempts, t = brute_force(hash_value, 4)

    if pwd:

        print("Recovered Password:", pwd)
        print("\nAttempts Made:", attempts)
        print("Time Taken:", round(t, 4), "seconds")

        ent, strength, reco = analyze(pwd)

        print("\nPassword Analysis")
        print("-----------------")
        print("Entropy:", ent)
        print("Strength:", strength)

        print("\nRecommendations:")
        for r in reco:
            print("-", r)

    else:
        print("Password not cracked")
