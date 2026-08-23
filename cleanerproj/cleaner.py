import logging
from pathlib import Path
import shutil
from collections import defaultdict

# Set up clean logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Upgraded Mapping: Added Programs, Presentations, and Data types
EXTENSION_MAP = {
    # Images
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".svg": "Images",
    # Documents & Presentations
    ".pdf": "Documents", ".docx": "Documents", ".doc": "Documents", ".txt": "Documents", 
    ".xlsx": "Documents", ".csv": "Documents", ".pptx": "Presentations", ".ppt": "Presentations",
    # Media
    ".mp3": "Audio", ".wav": "Audio", ".mp4": "Video", ".mkv": "Video", ".mov": "Video",
    # Archives & Code
    ".zip": "Archives", ".tar": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".py": "Code", ".js": "Code", ".html": "Code", ".css": "Code",
    # Data & Executables
    ".json": "Data", ".xml": "Data", ".exe": "Programs", ".msi": "Programs"
}

def get_unique_path(destination_dir: Path, filename: str) -> Path:
    """Generates a non-conflicting path if a file with the same name exists."""
    target_path = destination_dir / filename
    if not target_path.exists():
        return target_path

    stem = target_path.stem
    suffix = target_path.suffix
    counter = 1

    while target_path.exists():
        target_path = destination_dir / f"{stem}_{counter}{suffix}"
        counter += 1

    return target_path

def organize_directory(target_dir: Path, preview_only: bool = False) -> None:
    """Parses and organizes files in the given directory into categorized subfolders."""
    if not target_dir.exists() or not target_dir.is_dir():
        logging.error(f"\n[ERROR] Provided path '{target_dir}' is not a valid directory.")
        return

    mode_text = "[PREVIEW MODE]" if preview_only else "[ACTIVE MODE]"
    logging.info(f"\n{mode_text} Starting scan on: {target_dir.resolve()}\n")
    
    # Track statistics
    summary = defaultdict(int)
    moved_count = 0

    for file_path in target_dir.iterdir():
        # Skip subdirectories to prevent recursive movement loops
        if file_path.is_dir():
            continue

        ext = file_path.suffix.lower()
        # Ignore files without extensions
        if not ext:
            continue
            
        category = EXTENSION_MAP.get(ext, "Others")
        destination_folder = target_dir / category
        final_path = get_unique_path(destination_folder, file_path.name)

        if preview_only:
            logging.info(f"Would move: '{file_path.name}' -> {category}/")
            summary[category] += 1
            moved_count += 1
        else:
            try:
                # Create folder only when we are actually moving files
                destination_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(final_path))
                logging.info(f"Moved: '{file_path.name}' -> {category}/")
                summary[category] += 1
                moved_count += 1
            except PermissionError:
                logging.warning(f"Permission denied: Could not move '{file_path.name}'. File might be open.")
            except Exception as e:
                logging.error(f"Failed to move '{file_path.name}': {e}")

    # Print a clean summary table
    print("-" * 40)
    print(f"SUMMARY: {moved_count} file(s) processed")
    print("-" * 40)
    if moved_count > 0:
        for cat, count in sorted(summary.items()):
            print(f" {cat.ljust(15)} : {count} file(s)")
    else:
        print(" No loose files found to organize.")
    print("-" * 40)

if __name__ == "__main__":
    print("-" * 40)
    print("      PC Folder Organizer Utility Pro")
    print("-" * 40)
    
    folder_input = input(
        "Enter the full path of the folder you want to organize \n"
        "(e.g., C:\\Users\\Name\\Downloads) or press Enter for the current folder: "
    ).strip()

    if not folder_input:
        target_directory = Path.cwd()
    else:
        # STRIP FIX: Remove invisible Windows characters
        folder_input = folder_input.strip('\u202a\u202b\u202c\u202d\u202e\'"')
        target_directory = Path(folder_input)

    # Ask the user if they want a dry run
    preview_choice = input("\nDo you want to preview the changes first? (y/n): ").strip().lower()
    is_preview = preview_choice == 'y'

    organize_directory(target_directory, preview_only=is_preview)
    
    # If it was just a preview, ask if they want to proceed for real
    if is_preview:
        proceed = input("\nDo you want to proceed and move these files now? (y/n): ").strip().lower()
        if proceed == 'y':
            organize_directory(target_directory, preview_only=False)
    
    input("\nPress Enter to exit...")
    
