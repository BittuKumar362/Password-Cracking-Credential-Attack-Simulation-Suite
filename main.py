from modules.dictionary_generator import *
from modules.password_analyzer import *
from modules.report_generator import *
import hashlib

print("\nPassword Security Audit Tool\n")

# User input
name = input("Enter name for dictionary generation: ")
dob = input("Enter DOB (DDMMYYYY): ")
phone = input("Enter phone number: ")

# Step 1: Generate dictionary
words = generate_dictionary(name, dob, phone)

save_wordlist(words)

print(f"[+] Dictionary generated with {len(words)} passwords")

# Step 2: Password Security Audit
audit_results = []

for pwd in words[:10]:   # analyze first 10 passwords

    hash_value = hashlib.md5(pwd.encode()).hexdigest()

    ent, strength, reco = analyze(pwd)

    audit_results.append({
        "password": pwd,
        "hash": hash_value,
        "entropy": ent,
        "strength": strength,
        "recommendation": reco
    })

# Step 3: Generate report
generate_audit_report(audit_results)

print("\n[+] Password Security Audit Report Generated")

print("\nProject Execution Completed Successfully")
