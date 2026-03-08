failed_logins = 0
successful_logins = 0
suspicious_ips = set()

with open("auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_logins += 1

            parts = line.split()
            ip = parts[-4]
            suspicious_ips.add(ip)

        if "Accepted password" in line:
            successful_logins += 1

print("Log Summary")
print("------------------")
print(f"Failed login attempts: {failed_logins}")
print(f"Successful logins: {successful_logins}")

print("\nSuspicious IPs:")
for ip in suspicious_ips:
    print(ip)

if failed_logins > 5:
    print("\n⚠️ Possible brute force attack detected")

# -----------------------------
# Create summary for AI analysis
# -----------------------------

summary = f"""
Failed login attempts: {failed_logins}
Successful logins: {successful_logins}
Suspicious IPs: {list(suspicious_ips)}
"""

# -----------------------------
# AI Explanation
# -----------------------------

import requests

def explain_with_ai(summary):

    prompt = f"""
You are a cybersecurity analyst.

Explain the following log summary and identify possible threats:

{summary}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    print("\nAI Security Analysis:\n")
    print(result["response"])

# Run AI analysis
explain_with_ai(summary)