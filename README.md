# 🛡️ Phishing Detector (Basic)

A **basic phishing detection project written in Python** that analyzes URLs using simple rule-based checks to identify **possible phishing attempts**.

This project is intended for **learning cybersecurity fundamentals**, understanding how phishing URLs are structured, and practicing clean Python project organization.

---

## 📌 Features

- Detects **potential phishing URLs** using heuristic rules
- Flags common phishing indicators:
  - Long URLs
  - Suspicious keywords
  - Unsafe domain extensions
  - Missing HTTPS
  - Special characters and numbers
- Displays **clear reasons** for detection
- Simple **command-line interface (CLI)**

---

## 🧠 How It Works

Each URL is analyzed using predefined rules such as:

- URL length check  
- Presence of `@` symbol  
- Use of hyphens (`-`)  
- Use of `http://` instead of `https://`  
- Detection of common phishing keywords  
- Suspicious domain extensions  
- Numbers or IP-based URLs  

If one or more rules are triggered, the URL is marked as **potential phishing**, along with the reasons.

---

## 📂 Project Structure

phishing-detector/
│
├── main.py # Program entry point (user input & output)
├── detector.py # Core phishing detection logic
├── rules.py # Suspicious keywords & domain rules
└── README.md


---

## ▶️ Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/phishing-detector.git


2. Navigate to the project directory:

  ```bash
   cd phishing-detector

```

 Run the program:
  ```bash
   python main.py
```



Enter URLs separated by commas:
```
https://example.com, http://secure-login.xyz, https://bank-update.info
```
🧪 Example Output
```
Checking: http://secure-login.xyz
⚠️ POSSIBLE PHISHING DETECTED
 - No HTTPS (not secure)
 - Suspicious keyword found: 'login'
 - Suspicious domain extension: '.xyz'

Probably phishing attempt.
Do not click on the link and report it if necessary.

```
⚠️ Disclaimer

This tool performs basic checks only and should not be used as a replacement for professional security software.

Always verify URLs manually and use trusted cybersecurity tools.

## 🎯 Project Goals

  - Learn basic phishing detection techniques
  - Practice Python modular programming
  - Understand common phishing patterns
  - Build a foundation for more advanced cybersecurity projects

**🚀 Possible Improvements**

  - Machine learning–based detection
  - URL reputation checks
  - Browser extension integration
  - Logging and reporting system
  - Real-time scanning

## 📜 License

This project is for educational purposes.
Feel free to use, modify, and improve it.
