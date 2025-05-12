# 🧹 Temp Cleaner

A lightweight Windows utility that deletes temporary files to help speed up your PC. Built in Python, this tool targets user and system temp folders — including `%TEMP%`, `%TMP%`, and `C:\Windows\Temp`.

> ✅ Permanently deletes `.tmp`, `.log`, and other leftover junk files.
> ⚠️ Requires Administrator privileges to fully clean `C:\Windows\Temp`.

---

## 📦 Features

- Cleans the following directories:
  - `%TEMP%`, `%TMP%`
  - `C:\Windows\Temp`
  - `AppData\Local\Temp`
- Reports how many `.log` files were deleted from `C:\Windows\Temp`
- Works as a standalone `.exe` (no Python install required)
- Open source and customizable

---

## 🚀 How to Use

### 🐍 Run the Python Script (Developer Use)
1. Make sure Python is installed
2. Download `clean_temp.py`
3. Run it from an elevated Command Prompt:
   ```bash
   python clean_temp.py