# Advanced Python Port Scanner

A multi-threaded TCP port scanner built in Python that detects open ports, identifies common services, and supports both IP addresses and domain names (automatically resolved to IP).

---

## Features

* 🔹 Multi-threaded scanning for faster performance
* 🔹 Supports both **IP addresses and domain names**
* 🔹 Automatic domain → IP resolution
* 🔹 Detects **common services** running on open ports
* 🔹 Custom port range scanning (1–65535)
* 🔹 Clean and structured scan summary
* 🔹 Real-time display of open ports

---

## Tech Stack

* Python 3
* `socket` (network communication)
* `threading` (parallel scanning)
* `datetime` (scan timing)

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/iamvijay8877/CUSTOM-PORT-SCANNER-PYTHON.git
```

2. Navigate into the project folder:

```bash
cd CUSTOM-PORT-SCANNER-PYTHON
```

3. Run the script:

```bash
python scanner.py
```

---

## Usage

You will be prompted to enter:

* Target (IP or domain)
* Start port
* End port

### Example:

```
Enter target (IP or hostname): google.com
Start port: 1
End port: 1000
```

---

## Sample Output

```
[INFO] Resolved to IP: 142.250.xxx.xxx

[INFO] Scanning google.com on ports 1–1000...

  [OPEN]  Port 80     → HTTP (Website - No Encryption)
  [OPEN]  Port 443    → HTTPS (Website - Encrypted)

=======================================================
                   SCAN SUMMARY
=======================================================
  Target       : google.com (142.250.xxx.xxx)
  Port Range   : 1 → 1000
  Time Taken   : 2.45 seconds
  Open Ports   : 2 found

  PORT    SERVICE
  ------  ------------------------------
  80      HTTP (Website - No Encryption)
  443     HTTPS (Website - Encrypted)
=======================================================
```

---

## Disclaimer

This tool is intended for **educational and ethical purposes only**. Do not scan systems without proper authorization.

---

## Future Improvements

* Banner grabbing (service version detection)
* Export results to file (CSV/JSON)
* Add CLI arguments using `argparse`
* Improve service detection beyond common ports
* Add GUI interface

---

## Author

Vijay Kumar
