#!/bin/bash
# user_cleanup.sh
# Deletes users who haven't logged in for over 90 days (excluding system users)

THRESHOLD=90

echo "Checking for inactive users..."
for user in $(lastlog | awk -v T="$THRESHOLD" '$NF ~ /^[0-9]+/ && $NF > T {print $1}'); do
  sudo userdel -r "$user"
  echo "Deleted user: $user"
done
