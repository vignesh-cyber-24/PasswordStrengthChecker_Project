# 🔐 Secure Password Strength Checker

A Python-based command-line tool that evaluates the strength of passwords based on:
- Length
- Presence of uppercase, lowercase, numbers, and symbols
- Shannon entropy estimation (measures randomness)
- Color-coded feedback and result logging

## 📦 Features
- Password length and character diversity validation
- Entropy-based randomness calculation
- Colorized strength output (Weak, Moderate, Strong)
- Logs results with timestamp to a local `password_strength.log` file
- Clean and beginner-friendly Python implementation

## 📂 How to Run
### Install required module:
```
pip install colorama
```

### Run the program:
```
python password_checker.py
```

Type `exit` to quit the program.

## 📈 Example
```
Enter a password to test: Cyber@123
Password: Cyber@123
Strength: Strong
Entropy: 53.21
```

## 📖 Techniques Used
- Regular Expressions (regex) for pattern matching
- Shannon Entropy calculation for randomness estimation
- Colorama for terminal color output
- File handling for logging

## 📜 Log Example (`password_strength.log`)
```
2025-04-13 14:25:10.123456 - Password: Cyber@123, Strength: Strong
```

## ✅ Author
- Developed as a one-day cybersecurity project for résumé enhancement.
