import re



# Identify hashing algorithm
def identify_hash(hash_value):

    length = len(hash_value)

    if hash_value.startswith("$6$"):
        return "SHA-512"

    elif hash_value.startswith("$5$"):
        return "SHA-256"

    elif hash_value.startswith("$1$"):
        return "MD5 (Unix)"

    elif re.fullmatch(r"[a-fA-F0-9]{32}", hash_value):
        return "MD5 / NTLM"

    elif re.fullmatch(r"[a-fA-F0-9]{40}", hash_value):
        return "SHA-1"

    elif re.fullmatch(r"[a-fA-F0-9]{64}", hash_value):
        return "SHA-256"

    elif re.fullmatch(r"[a-fA-F0-9]{128}", hash_value):
        return "SHA-512"

    else:
        return "Unknown"


# Extract Linux /etc/shadow
def extract_shadow(file_path):

    results = []

    with open(file_path) as f:

        for line in f:

            parts = line.strip().split(":")

            if len(parts) < 2:
                continue

            username = parts[0]
            hash_value = parts[1]

            algo = identify_hash(hash_value)

            results.append({
                "user": username,
                "hash": hash_value,
                "algorithm": algo
            })

    return results


# Extract Windows SAM hashes
def extract_windows_hashes(file_path):

    results = []

    with open(file_path) as f:

        for line in f:

            parts = line.strip().split(":")

            if len(parts) < 4:
                continue

            username = parts[0]
            ntlm_hash = parts[3]

            algo = identify_hash(ntlm_hash)

            results.append({
                "user": username,
                "hash": ntlm_hash,
                "algorithm": algo
            })

    return results

# Generic hash extractor
def extract_hash(file_path):

    hashes = []

    with open(file_path) as f:
        for line in f:
            h = line.strip()
            if h:
                hashes.append({
                    "hash": h,
                    "algorithm": identify_hash(h)
                })

    return hashes
