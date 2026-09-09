# brute-force-detection
Python-based brute-force attack detection using authentication logs
# Objective
Detect potential SSH brute-force attacks by analyzing authentication logs and identifying IP addresses with multiple failed login attempts

# TECHNOLOGIES
-PYTHON
-Regular Expressions
-Linux authentication logs
-Git/GitHub
# Detection Rule
If an IP address has 5 or more failed login attempts, the script generates a brute-force alert.
# Example
```text
Source IP : 192.168.1.59
Failed attempts :5
Alert: Possible brute-force attack detected
