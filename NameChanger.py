import os

# Folder containing your images
folder_path = "C:/Users/river/488/NewDendrites"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# OPTIONAL: If you only want to rename certain file extensions, specify them:
valid_extensions = ('.jpg', '.jpeg', '.png', '.heic')

# Filter out files that are not images (and optionally sort them for consistent ordering)
image_files = [f for f in files if f.lower().endswith(valid_extensions)]
image_files.sort()  # Sort alphabetically, or you can sort by creation time, etc.

for i, filename in enumerate(image_files):
    # Get the current file's extension
    ext = os.path.splitext(filename)[1].lower()
    
    # Create the new filename (e.g., "0.jpg")
    new_filename = f"{i}{ext}"
    
    # Build full old/new file paths
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_filename)
    
    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed {filename} to {new_filename}")
