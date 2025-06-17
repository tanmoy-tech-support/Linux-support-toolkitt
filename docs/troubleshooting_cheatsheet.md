# 🛠️ Linux Troubleshooting Cheatsheet

A quick reference for first-line tech support tasks on Ubuntu, Red Hat, and Kali systems.

---

## ✅ Basic System Checks

- `uptime` — Check load average and uptime
- `df -h` — View disk usage in human-readable format
- `free -m` — Memory usage in MB
- `top` / `htop` — Monitor system processes

---

## 🔌 Network & DNS

- `ip a` — Show IP address and interfaces
- `ping 8.8.8.8` — Test external connectivity
- `nmcli device status` — Check network device state
- `dig` / `nslookup` — DNS resolution test
- `traceroute` — Network path analysis

---

## 🔍 Service & Logs

- `systemctl status apache2` — Check service status (e.g., Apache)
- `journalctl -xe` — View system logs
- `tail -f /var/log/syslog` — Real-time logs

---

## 🔐 User & Permission

- `id username` — View UID and group info
- `groups username` — View group membership
- `chmod`, `chown`, `usermod` — Manage permissions and users

---

## 🧼 Common Fixes

- `sudo apt update && sudo apt upgrade` — System update
- `sudo systemctl restart <service>` — Restart service
- `sudo kill -9 <PID>` — Kill stuck process

---

📌 *Updated by Tanmoy Chakraborty, Linux Support Toolkit*
