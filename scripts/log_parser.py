# log_parser.py
# Parses syslog to count error occurrences by type

import re
from collections import Counter

LOG_FILE = "/var/log/syslog"  # Or try /var/log/messages in RedHat

def parse_errors(log_file):
    with open(log_file, "r", errors="ignore") as f:
        lines = f.readlines()

    errors = [line for line in lines if "error" in line.lower()]
    types = [re.findall(r'\b\w+\b', line.lower())[2] for line in errors if len(re.findall(r'\b\w+\b', line.lower())) > 2]

    count = Counter(types)
    return count

if __name__ == "__main__":
    results = parse_errors(LOG_FILE)
    print("\n🧾 Error Summary:")
    for err_type, count in results.items():
        print(f"{err_type}: {count}")
