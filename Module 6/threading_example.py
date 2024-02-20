import time
import threading


def download_file(file_name):
    print(f"Starting donwload of {file_name}")
    time.sleep(4)
    print(f"Download of {file_name} complete")


files_to_download = ["file1.zip", "file2.zip", "file3.zip"]

for file in files_to_download:
    download_thread = threading.Thread(target = download_file, args=(file,))
    download_thread.start() 