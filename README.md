# 🔐 Password Strength Checker

**CodTech IT Solutions — Internship Project**

---

## 📌 Project Info

| Field         | Details                        |
|---------------|-------------------------------|
| Intern Name   | Subham Mondal                |
| Intern ID     | CTTS100            |
| Project Name  | Password Strength Checker     |
| Domain        | Cyber Security                |
| Duration      | 2 weeks |
              

---

## 📖 Overview

A Python-based **Password Strength Checker** that evaluates passwords against multiple security criteria and provides a detailed strength report with actionable suggestions.

---

## ✨ Features

- ✅ Checks 8 security criteria
- 📊 Calculates entropy (bits) for brute-force resistance
- 🏆 Strength score out of 100 with visual progress bar
- 💡 Personalized improvement suggestions
- 🚫 Detects common/weak passwords
- 🔁 Detects repeated & sequential character patterns
- 🙈 Hidden password input (no echo in terminal)

---

## 🛡️ Criteria Checked

| # | Criterion                  | Description                          |
|---|----------------------------|--------------------------------------|
| 1 | Minimum Length             | At least 8 characters                |
| 2 | Uppercase Letters          | At least one A-Z                     |
| 3 | Lowercase Letters          | At least one a-z                     |
| 4 | Digits                     | At least one 0-9                     |
| 5 | Special Characters         | At least one !@#$% etc.              |
| 6 | Not a Common Password      | Not in top 20 weak passwords list    |
| 7 | No Repeated Characters     | No "aaa", "111" patterns             |
| 8 | No Sequential Characters   | No "abc", "123" patterns             |

---

## 🚀 How to Run

### Requirements
- Python 3.x (no external libraries needed)

### Run
```bash
python password_checker.py
```

### Sample Output
```
==================================================
       PASSWORD STRENGTH ANALYSIS REPORT
==================================================

  Password : M*******3
  Length   : 9 characters
  Entropy  : 53.6 bits

  ── Criteria Check ──
  [✔] Length: 9 characters (minimum 8)
  [✔] Contains uppercase letter (A-Z)
  [✔] Contains lowercase letter (a-z)
  [✔] Contains digit (0-9)
  [✘] Contains special character (!@#$...)
  [✔] Not a commonly used password
  [✔] No repeated characters (e.g., aaa, 111)
  [✔] No sequential characters (e.g., abc, 123)

  ── Strength Score ──
  [███████████████░░░░░] 76/100

  Result : 🟢  Strong

  ── Suggestions ──
  → Add special characters (!@#$%...)
==================================================
```

---

## 📁 Project Structure

```
password_strength_checker/
│
├── password_checker.py   # Main script
└── README.md             # Project documentation
```

---

## 🔬 How Strength is Calculated

**Score = (Criteria Passed / Total Criteria) × 80 + Entropy Bonus (max 20)**

- **Entropy** = `length × log₂(character pool size)`
- Higher entropy = more resistant to brute-force attacks

| Score Range | Label       |
|-------------|-------------|
| 0–19        | 🔴 Very Weak  |
| 20–39       | 🟠 Weak       |
| 40–59       | 🟡 Moderate   |
| 60–79       | 🟢 Strong     |
| 80–100      | ✅ Very Strong |

---

## 📄 License
This project is created for educational purposes as part of the CodTech Internship Program.
