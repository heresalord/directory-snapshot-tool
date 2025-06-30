# 📸 Directory Snapshot Tool

Directory Snapshot Tool by KMS STUDIO DEV (Du-rock KOUMASSI)  The Directory Snapshot Tool is a powerful Python utility designed and developed by Du-rock KOUMASSI (heresalord)- KMS STUDIO DEV. This tool helps developers and system administrators take detailed snapshots of directory structures—including file sizes, SHA256 hashes, and modification timestamps—and compare them effortlessly over time.  Ideal for plugin developers, security auditors, and IT professionals, it provides clear JSON reports highlighting added, removed, or modified files. The tool features an intuitive command-line interface enhanced with Rich for clean and colorful output.  By using the Directory Snapshot Tool from KMS STUDIO DEV, you gain reliable insights into filesystem changes, enabling better version control, auditing, and system integrity checks.

---

## 🧾 Features

- Recursive directory scan
- JSON snapshot with:
  - Relative path
  - File size
  - SHA256 hash
  - Last modification date
- Snapshot naming: timestamp or custom name
- Compare two snapshots:
  - Added files
  - Removed files
  - Modified files (size or hash changes)
- Clean CLI output using [Rich](https://github.com/Textualize/rich)

---

## 🚀 Usage

```bash
python main.py
````

Interactive menu will let you:

* Take a snapshot
* Compare snapshots
* Exit safely

---

## 📂 Project Structure

```
directory_snapshot_tool/
├── main.py              # CLI entry point
├── snapshot.py          # Snapshot creation logic
├── compare.py           # Snapshot comparison logic
├── utils.py             # Hashing, formatting, timestamp utilities
├── snapshots/           # Stores snapshot .json files
└── assets/
    └── banner.txt       # ASCII banner
```

---

## 🔧 Installation

```bash
pip install -r requirements.txt
```

---

## ✅ Requirements

* Python 3.8+
typer	Création de la CLI et interface interactive
rich	Affichage coloré et convivial dans le terminal (tables, prompts, etc.)
hashlib	Calcul du hash SHA256 (inclus dans Python standard)
pathlib	Manipulation des chemins de fichiers (standard Python)
json	Sauvegarde et lecture des snapshots (standard Python)
os, sys

````

---

## 🔹 2. `requirements.txt`

```txt
rich
typer
hashlib
pathlib
os
````

---

## 🔹 3. `.gitignore`

```gitignore
# Ignore Python cache
__pycache__/
*.pyc

# Ignore virtual environments
.venv/
env/
venv/

# Ignore snapshots
snapshots/*.json

# Ignore system files
.DS_Store
```

---

## 🔹 4. `LICENSE` (MIT example)

```txt
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy...
(full MIT license here)
```

