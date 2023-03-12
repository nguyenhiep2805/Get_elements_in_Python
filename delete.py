import os
import shutil


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Da xoa file {file_path}")
    else:
        print(f"File {file_path} khong ton tai")


def delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Da xoa folder {folder_path}")
    else:
        print(f"Folder {folder_path} khong ton tai")
