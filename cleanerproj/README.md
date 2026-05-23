# Smart Task Automation Bot 🧹

A Python-based automation script that monitors and organizes cluttered directories (like your Downloads folder) by cleanly sorting files into distinct sub-folders based on their extensions.

---

## 🚀 Features
- **Automatic Classification:** Inspects all items in a target folder and categorizes them automatically.
- **Cross-Platform Path Safety:** Built using Python's `os` library to handle file paths cleanly across Windows, Mac, and Linux.
- **Smart Directory Creation:** Automatically detects if a destination folder (like `Images` or `Documents`) exists; if not, it builds it on the fly.
- **Safety First:** Securely isolates folders and only targets individual files to prevent messy folder-nesting loops.

---

## 🛠️ Tech & Core Modules Used
As a medium-level automation project, this script dives deep into Python's core filesystem utilities:
- **`os.listdir`**: Acts as a digital scanner to compile loose filenames in a directory.
- **`os.path.join`**: Welds paths together dynamically using operating-system-specific separators (`/` vs `\`).
- **`os.path.isfile`**: Acts as a security guard to filter out sub-folders and shield them from changes.
- **`os.path.splitext`**: Uses text-splitting logic to isolate file extensions alongside their tracking dots.

---

## 📋 File Organization Rules Blueprint
The bot reads file signatures and dynamically channels them into structured zones:

| File Extensions | Destination Folder |
|---|---|
| `.jpg`, `.jpeg`, `.png`, `.gif` | `Images/` |
| `.pdf`, `.docx`, `.txt`, `.xlsx` | `Documents/` |
| `.mp3`, `.wav`, `.flac` | `Audio/` |
| `.mp4`, `.mkv`, `.mov` | `Video/` |
| `.zip`, `.rar`, `.tar.gz` | `Archives/` |

----
