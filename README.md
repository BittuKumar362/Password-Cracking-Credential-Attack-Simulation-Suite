# Password Cracking & Credential Attack Suite  

A Python-based cybersecurity toolkit designed to demonstrate password auditing, dictionary generation, hash extraction, and password cracking techniques in a controlled environment.
This project helps illustrate how weak passwords can be identified and compromised using automated password analysis and dictionary-based attacks. The toolkit is intended for educational purposes, helping students and cybersecurity enthusiasts understand common password security weaknesses and ethical password testing methods.

---

# Features 

### 1. Dictionary Generation 

- Generates password candidates using personal information.

- Includes pattern variations and character mutations.

### 2. Password Strength Analysis

- Calculates password entropy.

- Classifies password strength (Weak / Medium / Strong).

- Provides recommendations for improving password security.

### 3. Password Audit Report

- Generates a structured password security report.

- Displays password entropy, strength level, and recommendations.

### 4. Hash Extraction

- Extracts hashes from sample files.

- Supports hash extraction from Linux shadow samples and Windows hash dumps.

### 5. Hash Cracking Simulation

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
git clone https://github.com/BittuKumar362/Password-Cracking-Credential-Attack-Simulation-Suite.git
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
 wordlists/generated.txt
 reports/audit_report.txt
``` 
### 2. Hash Cracking Simulation
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
## Educational Purpose

### This project demonstrates:

- Password security weaknesses

- Dictionary-based password attacks

- Hash cracking simulation

- Password entropy analysis

It is designed for learning cybersecurity concepts and ethical password auditing techniques.

## Limitations

- Currently supports limited hash algorithms (mainly MD5).

- The audit report stores only the first 10 generated passwords.

- Dictionary generation is based on user-provided personal information.

- Hash extraction uses sample files only.

## Ethical Use Disclaimer

- This tool is created strictly for educational and research purposes.
- It should only be used in controlled lab environments or systems where you have explicit permission.
- Unauthorized password cracking or credential attacks against real systems is illegal and unethical.

## Author
Bittu Kumar
B.Tech CSE | Cybersecurity Enthusiast
- GitHub: https://github.com/BittuKumar362
- LinkedIn: https://www.linkedin.com/in/bittu-kumar-ab2373339/

## Output Example 
1. main.py:
 <img width="975" height="308" alt="image" src="https://github.com/user-attachments/assets/9bd8f2f2-1228-47b1-bdb4-90bc9472dc90" />
2. reports/audit_report.txt: 
 <img width="975" height="525" alt="image" src="https://github.com/user-attachments/assets/efa80483-0dd4-4507-accd-7ebdce840aa3" />
<img width="975" height="571" alt="image" src="https://github.com/user-attachments/assets/ca9f0c1e-5895-4bb9-9c18-9a1ea9135881" />

3. wordlists/generated.txt  
<img width="975" height="541" alt="image" src="https://github.com/user-attachments/assets/69657a75-6c66-4f7f-8837-b8d40533e0ba" />
<img width="975" height="619" alt="image" src="https://github.com/user-attachments/assets/a6b12353-e0d1-43a9-bb01-672e808ba546" />

4. crack_hash.py
<img width="975" height="506" alt="image" src="https://github.com/user-attachments/assets/faec3c1f-e47b-4241-961b-57cd23d624ca" />

5. test_hash_extractor.py
<img width="975" height="487" alt="image" src="https://github.com/user-attachments/assets/840a32f1-783f-4cf0-b79d-041ed6aea8b8" />


