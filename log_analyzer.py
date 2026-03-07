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