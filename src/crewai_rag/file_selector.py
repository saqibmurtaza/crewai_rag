from pathlib import Path
from tkinter import Tk, filedialog

def ask_user_to_upload_file():
    """Prompt user to upload a `.txt`, `.md`, or `.pdf` file."""
    print("📂 Please select a `.txt`, `.md`, or `.pdf` file to upload.")

    root = Tk()
    root.withdraw()  # Hide the main Tkinter window

    # ✅ Force Tkinter to be on top (Fix for some environments)
    root.after(100, root.lift)
    root.after(200, lambda: root.attributes('-topmost', True))
    
    # ✅ Open file dialog
    file_path = filedialog.askopenfilename(filetypes=[
        ("Text Files", "*.txt"),
        ("Markdown Files", "*.md"),
        ("PDF Files", "*.pdf"),
    ])

    if not file_path:
        print("❌ No file selected. Exiting...")
        exit()

    return Path(file_path)

# ✅ Store the uploaded file path
uploaded_file_path = ask_user_to_upload_file()
print(f"✅ File uploaded: {uploaded_file_path}")
