import os


def get_folders(folder_path="surfline_data"):
    files = os.listdir(folder_path)
    return files
