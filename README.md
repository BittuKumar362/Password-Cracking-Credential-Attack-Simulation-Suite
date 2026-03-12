# Password Cracking & Credential Attack Suite  

A Python-based cybersecurity toolkit designed to demonstrate password auditing, dictionary generation, hash extraction, and password cracking techniques in a controlled environment.
This project helps illustrate how weak passwords can be identified and compromised using automated password analysis and dictionary-based attacks. The toolkit is intended for educational purposes, helping students and cybersecurity enthusiasts understand common password security weaknesses and ethical password testing methods.

---

## Features 

### Dictionary Generation 

- Generates password candidates using personal information.

- Includes pattern variations and character mutations.

### Password Strength Analysis

- Calculates password entropy.

- Classifies password strength (Weak / Medium / Strong).

- Provides recommendations for improving password security.

### Password Audit Report

- Generates a structured password security report.

- Displays password entropy, strength level, and recommendations.

### Hash Extraction

- Extracts hashes from sample files.

- Supports hash extraction from Linux shadow samples and Windows hash dumps.

### Hash Cracking Simulation

- Performs dictionary-based hash cracking.

- Displays cracking attempts and time taken.

---

## Project Structure
```bash 
PasswordCrackingCredentialAttackSuite/
│
├── main.py
├── crack_hash.py
├── test_hash_extractor.py
├── install.sh
│
├── modules/
│   ├── dictionary_generator.py
│   ├── password_analyzer.py
│   ├── report_generator.py
│   ├── hash_extractor.py
│   └── brute_force_simulator.py
│
├── wordlists/
│   └── generated.txt
│
├── reports/
│   └── audit_report.txt
│
├── hashes/
│   ├── hash.txt
│   ├── shadow_sample.txt
│   └── windows_hashes.txt

```
## Installation
```bash 
git clone https://github.com/yourusername/PasswordCrackingCredentialAttackSuite.git
cd PasswordCrackingCredentialAttackSuite
chmod +x install.sh
./install.sh
``` 
## Usage
### 1. Password Audit & Dictionary Generation
Run:
```bash
	python3 main.py
``` 
### The program will ask for:
-	Name
-	Date of Birth
-	Phone Number
### It will generate:
```bash
- wordlists/generated.txt
- reports/audit_report.txt
``` 
2. Hash Cracking Simulation
Run:
```bash 
	python3 crack_hash.py
``` 
## Options:
1.	Load hash from file
2.	Enter hash manually
## Example Output
```bash
Target Hash: 900150983cd24fb0d6963f7d28e17f72
Recovered Password: abc

Attempts Made: 9027
Time Taken: 0.0042 seconds

Password Analysis
-----------------
Entropy: 14.10
Strength: Weak

Recommendations:
- Increase password length
- Add symbols
``` 

## 3. Hash Extraction
Run:
```bash
	python3 test_hash_extractor.py
``` 
The module extracts hashes from files located in the hashes directory.
## 4. Hash Input Files
Place hashes inside the following files:
```bash 
•	hashes/hash.txt
•	hashes/shadow_sample.txt
•	hashes/windows_hashes.txt
``` 

