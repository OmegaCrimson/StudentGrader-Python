# Student Grader (Python) — CLI App  
برنامج تقييم الطلاب (Python) — تطبيق كونسول

A modular, console-based student grading system built in Python.  
نظام تقييم طلاب يعمل عبر الكونسول، يدعم إدخال درجات متعددة، حساب المعدل، وحفظ البيانات.

---

## 📦 Project Overview

[![Build](https://github.com/OmegaCrimson/StudentGrader-Python/actions/workflows/release.yml/badge.svg)](https://github.com/OmegaCrimson/StudentGrader-Python/actions/workflows/release.yml)
![Release](https://img.shields.io/github/v/release/OmegaCrimson/StudentGrader-Python)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Platform](https://img.shields.io/badge/platform-Windows-green)
![License](https://img.shields.io/github/license/OmegaCrimson/StudentGrader-Python)
![Downloads](https://img.shields.io/github/downloads/OmegaCrimson/StudentGrader-Python/total)
![Last Commit](https://img.shields.io/github/last-commit/OmegaCrimson/StudentGrader-Python)
![Commits per Month](https://img.shields.io/github/commit-activity/m/OmegaCrimson/StudentGrader-Python)
![Issues](https://img.shields.io/github/issues/OmegaCrimson/StudentGrader-Python)
![PRs](https://img.shields.io/github/issues-pr/OmegaCrimson/StudentGrader-Python)
![Contributors](https://img.shields.io/github/contributors/OmegaCrimson/StudentGrader-Python)
![Code Size](https://img.shields.io/github/languages/code-size/OmegaCrimson/StudentGrader-Python)
![Top Language](https://img.shields.io/github/languages/top/OmegaCrimson/StudentGrader-Python)
![Maintenance](https://img.shields.io/maintenance/yes/2025)
![GitHub Stars](https://img.shields.io/github/stars/OmegaCrimson/StudentGrader-Python?style=social)
![GitHub Forks](https://img.shields.io/github/forks/OmegaCrimson/StudentGrader-Python?style=social)
![Built by Mohamed Gonem](https://img.shields.io/badge/built%20by-Mohamed%20Gonem-blue?style=flat-square&logo=github)
![Made with Python and ❤️](https://img.shields.io/badge/made%20with-Python%20and%20%E2%9D%A4-red?style=flat-square&logo=python)
![Open Source](https://img.shields.io/badge/open%20source-yes-brightgreen?style=flat-square&logo=github)
![Maintained](https://img.shields.io/badge/maintained-actively-blue?style=flat-square)
![CLI App](https://img.shields.io/badge/interface-CLI-lightgrey?style=flat-square&logo=terminal)

---

## ✨ Features

- Add, view, and delete student records  
- Multi-subject support per student  
- GPA and percentage calculation  
- Input validation (Arabic & English digits)  
- Auto-saving to AppData  
- Clean CLI interface with modular services  
- Action/error logging  
- Extensible architecture

---

## 🚀 Getting Started

### Option 1: Download Executable

1. Visit the [Releases](https://github.com/OmegaCrimson/StudentGrader-Python/releases) page  
2. Download the latest `.zip` or `.exe`  
3. Run:
   - `StudentGrader.exe` (Windows)

### Option 2: Build from Source

```bash
git clone https://github.com/OmegaCrimson/StudentGrader-Python.git
cd StudentGrader-Python
pip install -r requirements.txt
python main.py
```

---

## 🧪 Sample CLI Output

```plaintext
Student Grader
──────────────
1. Add Student
2. View Student
3. View All Students
4. Delete Student
5. Delete All Students
6. Exit Program

Input: 1
Name: Ali
Age: 20
Subject name: Math
Score: 90
Max Score: 100
Teacher: Mr. Ahmed
```

---

## 🗂️ Project Structure

```
StudentGrader-Python/
├── main.py              # Entry point
├── models/
│   ├── student.py       # Student class
│   └── subject.py       # Subject class
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

- Python 3.11
- PyInstaller (for packaging)
- Console I/O
- JSON serialization
- GitHub Actions (CI/CD)

---

## 🔁 CI/CD Automation

This project uses GitHub Actions to:

- Build the executable on manual trigger
- Package the `.exe` and `.zip` artifacts
- Upload them to the [Releases](https://github.com/OmegaCrimson/StudentGrader-Python/releases) page

You can trigger a release manually using the GitHub Actions tab.

---

## 📄 License

Licensed under the [MIT License](LICENSE).  
Use, modify, and distribute freely — just credit the author: **Mohamed Gonem / محمد غنيم**

---

## 🙌 Acknowledgments

- Built with care, clarity, and curiosity  
- Inspired by real-world grading systems and CLI design patterns  
- Thanks to the open-source community for tools and ideas

---

**Built to be useful. Designed to be clear.  
تم بناؤه ليكون مفيدًا، وصُمم ليكون واضحًا.**