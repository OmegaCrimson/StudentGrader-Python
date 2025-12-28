# ReadMeForge 🛠️📘 — README Builder Toolkit  
ReadMeForge 🛠️📘 — أداة إنشاء ملفات README احترافية

A modular, multilingual README generator with badge creation, section templates, and seamless integration across CLI, GUI, and Python server components.  
مولّد README متعدد اللغات، يدعم إنشاء الشارات، وتنسيق الأقسام، ويعمل عبر واجهات CLI وGUI وخادم Python.

---

## 📦 Project Overview

[![Build](https://github.com/OmegaCrimson/ReadMeForge/actions/workflows/tester.yml/badge.svg)](https://github.com/OmegaCrimson/ReadMeForge/actions/workflows/tester.yml)
[![Build](https://github.com/OmegaCrimson/ReadMeForge/actions/workflows/release.yml/badge.svg)](https://github.com/OmegaCrimson/ReadMeForge/actions/workflows/release.yml)
![Release](https://img.shields.io/github/v/release/OmegaCrimson/ReadMeForge)
![.NET & Python](https://img.shields.io/badge/.NET%207%20%7C%20Python-3.11-blueviolet)
![Platform](https://img.shields.io/badge/platform-Windows-green)
![License](https://img.shields.io/github/license/OmegaCrimson/ReadMeForge)
![Downloads](https://img.shields.io/github/downloads/OmegaCrimson/ReadMeForge/total)
![Last Commit](https://img.shields.io/github/last-commit/OmegaCrimson/ReadMeForge)
![Commits per Month](https://img.shields.io/github/commit-activity/m/OmegaCrimson/ReadMeForge)
![Issues](https://img.shields.io/github/issues/OmegaCrimson/ReadMeForge)
![PRs](https://img.shields.io/github/issues-pr/OmegaCrimson/ReadMeForge)
![Contributors](https://img.shields.io/github/contributors/OmegaCrimson/ReadMeForge)
![Code Size](https://img.shields.io/github/languages/code-size/OmegaCrimson/ReadMeForge)
![Top Language](https://img.shields.io/github/languages/top/OmegaCrimson/ReadMeForge)
![Maintenance](https://img.shields.io/maintenance/yes/2025)
![GitHub Stars](https://img.shields.io/github/stars/OmegaCrimson/ReadMeForge?style=social)
![GitHub Forks](https://img.shields.io/github/forks/OmegaCrimson/ReadMeForge?style=social)
![Built by Mohamed Gonem](https://img.shields.io/badge/built%20by-Mohamed%20Gonem-blue?style=flat-square&logo=github)
![Made with C#, Python & ❤️](https://img.shields.io/badge/made%20with-C%23%2C%20Python%20and%20%E2%9D%A4-red?style=flat-square&logo=dotnet)
![Open Source](https://img.shields.io/badge/open%20source-yes-brightgreen?style=flat-square&logo=github)
![Maintained](https://img.shields.io/badge/maintained-actively-blue?style=flat-square)
![Multilingual](https://img.shields.io/badge/language-English%20%7C%20Arabic-yellow?style=flat-square)

---

## ✨ Features

- 🧱 Modular architecture: Python backend + C# CLI + WinForms GUI  
- 🏷️ Auto-generated README sections (Features, Installation, Usage, License, etc.)  
- 🖼️ Dynamic badge generation (build, license, downloads, etc.)  
- 🌐 Multilingual support (English + Arabic)  
- 🧩 Extensible templates for custom sections  
- 🧪 Integrated testing and CI/CD via GitHub Actions  
- 📦 One-click packaging and release automation  
- 🧠 Clean codebase with reusable components

---

## 🚀 Getting Started

### Option 1: Download Executable

1. Visit the [Releases](https://github.com/OmegaCrimson/ReadMeForge/releases) page  
2. Download the latest `.zip` or `.exe`  
3. Run:
   - `ClientCLI.exe` for CLI
   - `ClientGUI.exe` for GUI

### Option 2: Build from Source

```bash
git clone https://github.com/OmegaCrimson/ReadMeForge.git
cd ReadMeForge
# Build CLI
dotnet publish ClientCLI/ClientCLI.csproj -c Release -o out/ClientCLI
# Build GUI
dotnet publish ClientGUI/ClientGUI.csproj -c Release -o out/ClientGUI
# Run Python server
pip install -r PythonServer/requirements.txt
python PythonServer/PythonServer.py
```

---

## 🧪 Sample CLI Output

```plaintext
ReadMeForge CLI
───────────────
1. Generate README
2. Add Badge
3. Add Section
4. Preview Output
5. Export to File
6. Exit

Input: 1
Project Name: MyCoolTool
Select Sections: [x] Features [x] Installation [x] License
README generated successfully!
```

---

## 🗂️ Project Structure

```
ReadMeForge/
├── ClientCLI/              # C# CLI project
│   └── ClientCLI.csproj
├── ClientGUI/              # C# GUI project (WinForms)
│   └── ClientGUI.csproj
├── PythonServer/           # Python backend
│   ├── PythonServer.py
│   └── requirements.txt
├── workflows/              # GitHub Actions
├── package.json            # Semantic-release config
└── README.md
```

---

## 🛠️ Tech Stack

- C# (.NET 7) — CLI & GUI  
- Python 3.11 — Backend server  
- PyInstaller — Python packaging  
- GitHub Actions — CI/CD  
- Semantic-release — Versioning & changelog

---

## 🔁 CI/CD Automation

This project uses GitHub Actions to:

- Build all components (CLI, GUI, Python)  
- Package them into a single `.zip`  
- Auto-tag and generate changelog using `semantic-release`  
- Upload artifacts to the [Releases](https://github.com/OmegaCrimson/ReadMeForge/releases) page

Trigger a release manually via the GitHub Actions tab.

---

## 📄 License

Licensed under the [MIT License](LICENSE).  
Use, modify, and distribute freely — just credit the author: **Mohamed Gonem / محمد غنيم**

---

## 🙌 Acknowledgments

- Built with modularity, automation, and multilingual support in mind  
- Inspired by the need for polished, professional open-source documentation  
- Thanks to the open-source community for tools, ideas, and badge APIs

---

**Build better READMEs. Automate the polish.  
أنشئ ملفات README أفضل — تلقائيًا وباحترافية.**