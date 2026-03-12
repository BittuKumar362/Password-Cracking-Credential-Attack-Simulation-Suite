#!/bin/bash
echo "-------------------------------------------------"
echo "Password Cracking & Credential Attack Suite Setup"
echo "-------------------------------------------------"

# Check python installation
echo "[*] Checking Python installation..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Python3 is not installed. Please install Python3 first."
    exit 1
fi

echo "[+] Python3 found."

# Create required directories
echo "[*] Creating project directories..."

mkdir -p wordlists
mkdir -p reports
mkdir -p hashes

echo "[+] Directories created."

# Create empty files if not exist
touch wordlists/generated.txt
touch reports/audit_report.txt
touch hashes/hash.txt

echo "[+] Required files created."

echo "------------------------------------"
echo "Installation Completed Successfully!"
echo "------------------------------------"

echo ""
echo "To run the project:"
echo "python3 main.py"
echo ""
echo "To crack hashes:"
echo "python3 crack_hash.py"
echo ""
echo "To test hash extractor:"
echo "python3 test_hash_extractor.py"
