# 📸 Directory Snapshot Tool

This CLI tool allows you to take snapshots of a directory structure and compare them later. Useful for detecting changes between plugin versions, before/after installs, or system integrity checks.

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
