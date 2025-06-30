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
