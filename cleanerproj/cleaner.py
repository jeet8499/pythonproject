
import logging
from pathlib import Path
import shutil

# Set up clean logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Mapping extensions to category folders
EXTENSION_MAP = {
    # Images
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".svg": "Images",
    # Documents
    ".pdf": "Documents", ".docx": "Documents", ".doc": "Documents", ".txt": "Documents", 
    ".xlsx": "Documents", ".csv": "Documents",
    # Media
    ".mp3": "Audio", ".wav": "Audio", ".mp4": "Video", ".mkv": "Video",
    # Archives & Code
    ".zip": "Archives", ".tar": "Archives", ".py": "Code", ".js": "Code",
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


def organize_directory(target_dir: Path) -> None:
    """Parses and organizes files in the given directory into categorized subfolders."""
    if not target_dir.exists() or not target_dir.is_dir():
        logging.error(f"Provided path '{target_dir}' is not a valid directory. Please check the path.")
        return

    logging.info(f"Starting cleanup on: {target_dir.resolve()}")
    moved_count = 0

    for file_path in target_dir.iterdir():
        # Skip subdirectories to prevent recursive movement loops
        if file_path.is_dir():
            continue

        ext = file_path.suffix.lower()
        # Fallback to 'Others' if extension is unknown
        category = EXTENSION_MAP.get(ext, "Others")

        destination_folder = target_dir / category
        destination_folder.mkdir(exist_ok=True)

        final_path = get_unique_path(destination_folder, file_path.name)

        try:
            shutil.move(str(file_path), str(final_path))
            logging.info(f"Moved: '{file_path.name}' -> {category}/")
            moved_count += 1
        except PermissionError:
            logging.warning(
                f"Permission denied: Could not move '{file_path.name}'. File might be open/in use."
            )
        except Exception as e:
            logging.error(f"Failed to move '{file_path.name}': {e}")

    logging.info(f"Cleanup complete! Successfully organized {moved_count} file(s).")

if __name__ == "__main__":
    print("-" * 40)
    print("      PC Folder Organizer Utility")
    print("-" * 40)
    
    # Prompt the user to enter the path they want to clean
    folder_input = input(
        "Enter the full path of the folder you want to organize \n"
        "(e.g., C:\\Users\\Name\\Downloads) or press Enter for the current folder: "
    ).strip()

    # If the user just presses Enter, use the current directory
    if not folder_input:
        target_directory = Path.cwd()
    else:
        # STRIP FIX: Remove invisible Windows characters (U+202A, U+202C, etc.) and quotes
        folder_input = folder_input.strip('\u202a\u202b\u202c\u202d\u202e\'"')
        target_directory = Path(folder_input)

    print("\n")
    organize_directory(target_directory)
    
    # Keeps the window open if you double-clicked the file in Windows
    input("\nPress Enter to exit...")
                
                
                
            
