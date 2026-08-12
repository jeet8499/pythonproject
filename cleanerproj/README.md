Absolutely — for **your actual code**, I’d make the GitHub README section look like this:

# Automated File Organizer 🗂️

A Python-based command-line automation utility that organizes cluttered directories by automatically sorting files into categorized sub-folders based on their file extensions.

---

## 🚀 Features

* **Automatic File Classification:** Detects file extensions and moves files into appropriate categories such as `Images`, `Documents`, `Audio`, `Video`, `Code`, and `Archives`.
* **Duplicate File Handling:** Prevents files from being overwritten by automatically generating unique filenames when conflicts occur.
* **Smart Directory Creation:** Creates category folders automatically when they don't already exist.
* **Case-Insensitive Detection:** Handles extensions such as `.jpg`, `.JPG`, and `.Jpg` consistently.
* **Safety First:** Skips existing directories to prevent recursive folder movement and organization loops.
* **Error Handling & Logging:** Provides clear logs and handles permission errors or failed file operations gracefully.
* **Command-Line Support:** Allows users to specify any target directory, with the current directory used by default.

---

## 🛠️ Tech & Core Modules Used

This project focuses on Python's built-in filesystem and automation capabilities:

* **`pathlib.Path`**: Provides clean, cross-platform file and directory path handling.
* **`shutil.move`**: Handles moving files between directories.
* **`argparse`**: Provides a command-line interface for specifying the target directory.
* **`logging`**: Displays clean status messages, warnings, and errors.
* **`dict` (`EXTENSION_MAP`)**: Maps file extensions to their corresponding category folders.

---

## 📋 File Organization Rules Blueprint

The organizer reads each file's extension and dynamically routes it into the appropriate folder:

| File Extensions                                  | Destination Folder |
| ------------------------------------------------ | ------------------ |
| `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`          | `Images/`          |
| `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.csv` | `Documents/`       |
| `.mp3`, `.wav`                                   | `Audio/`           |
| `.mp4`, `.mkv`                                   | `Video/`           |
| `.zip`, `.tar`                                   | `Archives/`        |
| `.py`, `.js`                                     | `Code/`            |
| Unknown extensions                               | `Others/`          |

---

## ▶️ Usage

Run the script from the terminal:

```bash
python organizer.py "path/to/directory"
```

If no path is provided, the script organizes the **current directory**:

```bash
python organizer.py
```

---

## 📁 Example

Before:

```text
Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
├── script.py
└── archive.zip
```

After:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Audio/
│   └── song.mp3
├── Video/
│   └── movie.mp4
├── Code/
│   └── script.py
└── Archives/
    └── archive.zip

