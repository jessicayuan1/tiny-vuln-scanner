# 🔍 Tiny Vulnerability Scanner

A lightweight Python-based static analyzer that detects common insecure patterns in source code using the `ast` module.

## 🚀 Features
- Detects high-risk function calls like `eval`, `exec`, `os.system`
- Simple, fast, and extendable
- Built entirely in Python
- Great as a base for deeper static analysis tools

## 📂 Project Structure
scanner.py # Core vulnerability 
scanner rules.py # Rule definitions 
sample_code/ # Example Python files to scan


## ⚙️ How to Use

1. Clone this repo:
```bash
git clone https://github.com/your-username/tiny-vuln-scanner.git
cd tiny-vuln-scanner
```
2. Run the scanner
python scanner.py sample_code/vulnerable_example.py

3. Output
[!] Code Execution via eval on line 3
[!] Command Injection via os.system on line 7

# Example output
$ python scanner.py sample_code/vulnerable_example.py
🔍 Scanning sample_code/vulnerable_example.py...
[!] Tainted Input (check usage) via `input` on line 5
[!] Code Execution via `eval` on line 6
[!] Command Injection via `os.system` on line 7
[!] Command Injection via `subprocess.call` on line 8
[!] Unsafe Deserialization via `pickle.load` on line 11
[!] Code Execution via `exec` on line 13
PS C:\Users\jessi\OneDrive\Documents\tiny-vuln-scanner> 