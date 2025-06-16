# organizer.py

import os
import shutil
import time

# --- CONFIGURATION ---
# NOTE: This is the path to the folder you want to organize.
# On Windows it might be: 'C:/Users/YourUsername/Downloads'
# On macOS it might be: '/Users/YourUsername/Downloads'
# On Linux it might be: '/home/YourUsername/Downloads'
# The script automatically finds the correct path for your system.
DOWNLOADS_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
 
# This dictionary maps folder names to file extensions.
# You can easily add or change categories and extensions.
# The key is the name of the folder, and the value is a list of extensions.
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".odt", ".rtf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts & Code": [".py", ".js", "html", ".css", ".java", ".c", ".cpp", ".sh"],
    "Executables & Installers": [".exe", ".msi", ".dmg", ".pkg"]
     
    # Any file that doesn't fit a category will be moved to the "Other" folder.
}

def get_category(file_extension):
    """
    Finds the category for a given file extension.
    
    Args:
        file_extension (str): The extension of the file (e.g., '.pdf').
    
    Returns:
        str: The name of the category folder, or 'Other' if not found.
    """

     
    for category, extensions in CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Other"

def handle_duplicate_filename(dest_path, source_path):
    """
    Handles cases where a file with the same name already exists in the destination.
    It renames the new file by appending a counter (e.g., 'file_1.txt').
    
    Args:
        dest_path (str): The intended destination path for the file.
        source_path (str): The original source path of the file (not used here but good practice).

    Returns:
        str: A new, unique destination path.
    """
    if not os.path.exists(dest_path):
        return dest_path

    # Separate the filename and extension
    filename, extension = os.path.splitext(os.path.basename(dest_path))
    counter = 1
    
    # Keep trying new names until a unique one is found
    while True:
        new_filename = f"{filename}_{counter}{extension}"
        new_dest_path = os.path.join(os.path.dirname(dest_path), new_filename)
        if not os.path.exists(new_dest_path):
            return new_dest_path
        counter += 1

def organize_folder(path):
    """
    Organizes all files in the specified folder path into subdirectories based on their type.
    """
    print(f"Starting organization of: {path}\n")

    # Get a list of all items in the directory
    try:
        all_items = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The folder '{path}' was not found.")
        print("Please check the DOWNLOADS_PATH variable in the script.")
        return

    moved_count = 0
    # Loop through each item in the directory
    for item_name in all_items:
        source_path = os.path.join(path, item_name)

        # Skip if it's a directory or a hidden file
        if os.path.isdir(source_path) or item_name.startswith('.'):
            continue

        # Get the file extension (and make it lowercase for consistency)
        _, file_extension = os.path.splitext(item_name)
        file_extension = file_extension.lower()

        # If it's a file without an extension, skip it or categorize as 'Other'
        if not file_extension:
            category = "Other"
        else:
            category = get_category(file_extension)

        # Create the destination folder if it doesn't exist
        dest_folder = os.path.join(path, category)
        os.makedirs(dest_folder, exist_ok=True)

        # Get the final destination path, handling any potential duplicates
        dest_path = handle_duplicate_filename(os.path.join(dest_folder, item_name), source_path)
        
        # Move the file
        try:
            shutil.move(source_path, dest_path)
            moved_count += 1
            print(f"Moved: {item_name}  ->  [{category}]")
        except Exception as e:
            print(f"Error moving {item_name}: {e}")

    if moved_count == 0:
        print("No files were moved. The folder is already organized.")
    else:
        print(f"\nOrganization complete! Moved {moved_count} file(s).")


if __name__ == "__main__":
    # This block runs when the script is executed directly
    organize_folder(DOWNLOADS_PATH)