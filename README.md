# file-organizer
A simple Python script to automatically organize files in your Downloads folder


## ✨ Features

-   **Automatic Categorization:** Sorts files into folders like `Images`, `Documents`, `Videos`, `Archives`, etc.
-   **Easily Customizable:** Add new categories or change file extensions in a simple dictionary.
-   **Handles Duplicates:** Automatically renames files if a file with the same name already exists in the destination (e.g., `photo.jpg` becomes `photo_1.jpg`).
-   **Zero Dependencies:** Runs using only Python's standard libraries. No `pip install` needed!
-   **Cross-Platform:** Works on Windows, macOS, and Linux.

---

## 🚀 How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/python-file-organizer.git
    cd python-file-organizer
    ```

2.  **(Optional) Customize the script:**
    Open `organizer.py` in a text editor. You can change the `DOWNLOADS_PATH` to target a different folder or modify the `CATEGORIES` dictionary to fit your needs.

3.  **Run the script:**
    ```bash
    python organizer.py
    ```

And that's it! The script will scan the folder and move the files into their new homes.

---

## 🛠️ Customization

You can easily customize the script by editing the `organizer.py` file.

### Change the Target Folder

Modify the `DOWNLOADS_PATH` variable to point to any folder you want to organize.

```python
# Before
DOWNLOADS_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')

# After (Example: Organizing your Desktop)
DOWNLOADS_PATH = os.path.join(os.path.expanduser('~'), 'Desktop')
```

### Add or Change Categories

Modify the `CATEGORIES` dictionary. The key is the folder name, and the value is a list of file extensions.

```python
# Add a new category for Fonts
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ...],
    "Documents": [".pdf", ".docx", ...],
    "Fonts": [".ttf", ".otf", ".woff"], # <-- New category
    # ... and so on
}
```
 
---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details