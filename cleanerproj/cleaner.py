import argparse
import logging
from pathlib import Path
import shutil

# Set up clean logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Mapping extensions to category folders
EXTENSION_MAP = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    # Media
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Video",
    ".mkv": "Video",
    # Archives & Code
    ".zip": "Archives",
    ".tar": "Archives",
    ".py": "Code",
    ".js": "Code",
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
        logging.error(f"Provided path '{target_dir}' is not a valid directory.")
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
                f"Permission denied: Could not move '{file_path.name}'. File might be in use."
            )
        except Exception as e:
            logging.error(f"Failed to move '{file_path.name}': {e}")

    logging.info(
        f"Cleanup complete! Successfully organized {moved_count} file(s)."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automated File Organizer Utility"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the directory to organize (default: current directory)",
    )

    args = parser.parse_args()
    target_directory = Path(args.path)

    organize_directory(target_directory)
for item in all_items:
    full_path = os.path.join(target_folder,item)
    
    if os.path.isfile(full_path):
        file_name, extension = os.path.splitext(item)
        
        extension = extension.lower()
        
        if extension in Extension_map:
            folder_name = Extension_map[extension]
            destination_folder = os.path.join(target_folder, folder_name)
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(f"Created new Folder :{folder_name}")
                
            final_file_path = os.path.join(destination_folder,item)
            
            
            shutil.move(full_path, final_file_path)
            print(f"Moved:{item} -> {folder_name}/")
            
print("\n Cleanup complete!YOur folder is organized ")
                
                
                
                
            
