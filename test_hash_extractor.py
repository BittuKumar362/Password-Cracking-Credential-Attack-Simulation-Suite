from modules.hash_extractor import *

print("\nTesting Linux Shadow Extraction\n")

shadow = extract_shadow("hashes/shadow_sample.txt")

for entry in shadow:
    print("User:", entry["user"])
    print("Hash:", entry["hash"])
    print("Algorithm:", entry["algorithm"])
    print()

print("\nTesting Windows SAM Extraction\n")

windows = extract_windows_hashes("hashes/windows_hashes.txt")

for entry in windows:
    print("User:", entry["user"])
    print("Hash:", entry["hash"])
    print("Algorithm:", entry["algorithm"])
    print()
