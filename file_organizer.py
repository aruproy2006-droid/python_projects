import os
import shutil

# Folder to organize
folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Folder not found!")
    exit()

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = file.split(".")[-1].lower()

        destination_folder = os.path.join(
            folder_path,
            extension.upper() + "_Files"
        )

        os.makedirs(destination_folder, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(destination_folder, file)
        )

print("Files organized successfully!")
