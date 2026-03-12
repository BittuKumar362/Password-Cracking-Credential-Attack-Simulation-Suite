import os

os.makedirs("reports", exist_ok=True)


# PASSWORD SECURITY AUDIT REPORT
def generate_audit_report(results):

    with open("reports/audit_report.txt","w") as f:

        f.write("Password Security Audit Report\n")
        f.write("--------------------------------\n\n")

        for r in results:

            f.write(f"Password: {r['password']}\n")
            f.write(f"MD5 Hash: {r['hash']}\n")
            f.write(f"Entropy: {r['entropy']}\n")
            f.write(f"Strength: {r['strength']}\n")

            f.write("Recommendations:\n")

            for rec in r["recommendation"]:
                f.write("- " + rec + "\n")

            f.write("\n-----------------------------\n\n")


# HASH CRACKING REPORT
def generate_crack_report(hash_value,password,attempts,time_taken,entropy,strength,recommendation):

    with open("reports/crack_report.txt","w") as f:

        f.write(f"Target Hash: {hash_value}\n")
        f.write(f"Recovered Password: {password}\n\n")

        f.write(f"Attempts Made: {attempts}\n")
        f.write(f"Time Taken: {time_taken:.4f} seconds\n\n")

        f.write("Password Analysis\n")
        f.write("-----------------\n")

        f.write(f"Entropy: {entropy}\n")
        f.write(f"Strength: {strength}\n\n")

        f.write("Recommendations:\n")

        for r in recommendation:
            f.write("- " + r + "\n")
