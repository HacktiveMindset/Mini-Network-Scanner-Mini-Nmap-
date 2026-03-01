# 🌐 Mini Network Scanner (Mini Nmap)

A Python-based **Network Reconnaissance Tool** that performs host
discovery, port scanning, and service/banner detection --- inspired by
real-world penetration testing workflows.

This project demonstrates how cybersecurity professionals enumerate
network targets during the reconnaissance phase.

> ⚠️ Built for **educational and ethical security testing only**.

------------------------------------------------------------------------

## 🚀 Features

✅ Host Discovery (Check if target is alive)\
✅ TCP Port Scanning (1--1024 ports)\
✅ Service / Banner Detection\
✅ Automated Recon Output\
✅ Beginner-Friendly Security Automation

------------------------------------------------------------------------

## 🧠 Project Objective

This project helps understand:

-   Network Reconnaissance Techniques
-   Port Scanning Fundamentals
-   Service Enumeration
-   Penetration Testing Workflow
-   Python Automation for Security

------------------------------------------------------------------------

## 🏗️ Project Structure

    network_scanner/
    │
    ├── scanner.py           # Main execution file
    ├── host_discovery.py    # Host availability check
    ├── port_scanner.py      # Port scanning logic
    ├── banner_grabber.py    # Service detection
    └── requirements.txt

------------------------------------------------------------------------

## ⚙️ Installation

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/HacktiveMindset/Mini-Network-Scanner-Mini-Nmap-.git
cd Mini-Network-Scanner-Mini-Nmap-
```

### 2️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Usage

Run the scanner:

``` bash
python scanner.py
```

Enter target:

    scanme.nmap.org

------------------------------------------------------------------------

## 📊 Example Output

    === Mini Network Scanner ===

    [+] Checking if host is alive...
    [ALIVE] Host reachable

    [+] Scanning ports...
    [OPEN] Port 22
    [OPEN] Port 80

    ===== SERVICE DETECTION =====
    Port 22: OpenSSH
    Port 80: Apache HTTP Server

    ===== SCAN COMPLETE =====

------------------------------------------------------------------------

## 🔍 How It Works

### 1. Host Discovery

Checks DNS resolution to confirm the host is reachable.

### 2. Port Scanning

Uses Python sockets to test TCP connections across common ports.

### 3. Banner Grabbing

Attempts to retrieve service banners to identify running services.

------------------------------------------------------------------------

## 🛡️ Security Concepts Covered

-   Network Enumeration
-   Attack Surface Discovery
-   Service Fingerprinting
-   Reconnaissance Phase (Red Team)

------------------------------------------------------------------------

## ⚠️ Legal Disclaimer

Use this tool only for:

✅ Personal lab environments\
✅ Authorized penetration testing\
✅ Learning cybersecurity

❌ Do NOT scan networks or systems without permission.

The author is not responsible for misuse.

------------------------------------------------------------------------

## 🧰 Technologies Used

-   Python 3
-   Socket Programming
-   Basic Networking Concepts

------------------------------------------------------------------------

## 📈 Future Improvements

-   Multithreaded scanning
-   Faster async scanning
-   CIDR network scanning
-   Output report export (TXT/HTML)
-   OS fingerprinting logic

------------------------------------------------------------------------

## 👨‍💻 Author

**Piyush Mujmule**

Cybersecurity Enthusiast | Aspiring DevSecOps Engineer\
Focused on Ethical Hacking, Automation & Security Research.

------------------------------------------------------------------------

## ⭐ Support

If you found this project useful:

⭐ Star the repository\
🍴 Fork and improve it\
🛡️ Practice ethical hacking responsibly

------------------------------------------------------------------------

## 📚 Learning Purpose

Part of a hands-on cybersecurity learning journey focused on real-world
penetration testing methodologies.
