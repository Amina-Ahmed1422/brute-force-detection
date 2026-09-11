src/brute_force_detector.py
import re
from collections import Counter

LOG_FILE = "logs/auth.log" THRESHOLD = 5
failed_attempts = []

with open(LOG_FILE, "r") as file:
     for line in file:
         if "Failed password" in line:
             match = re.search(r"from (\d+.\d+.\d+.\d+)", line)
             if match:
                 ip = match.group(1)
                 failed_attempts.append(ip)
ip_counts = Counter(failed_attempts)
print("=== Brute Force Detection ===")
for ip, count in ip_counts.items():
    if count >= THRESHOLD:
       print("[ALERT] Possible brute-force attack detected!") 
       print(f"Source IP: {ip}")  
       print(f"Failed attempts: {count}")
