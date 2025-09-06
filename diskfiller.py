import os
import threading
import time
import uuid
from datetime import datetime


storageLetters = ["D"] # UPDATE HERE

def generate_random_bytes(size_mb):
    size_bytes = size_mb * 1024 * 1024
    return os.urandom(size_bytes)
    
    
def create_folder(folderDest):
    if not os.path.exists(folderDest):
        os.makedirs(folderDest)


def create_zero_bytes_files(folderdestination, filesize):
    counter = 0
    try:
        while True:
            filename = os.path.join(folderdestination, f"{uuid.uuid4()}.bin")
            with open(filename, "wb") as f:
                f.write(generate_random_bytes(filesize))
            counter += 1
            if counter % 10:
                date = datetime.now().strftime('%H:%M:%S')
                print(date + " : Disk filling " + folderdestination + " in progress...")
    except:
        pass


def fill_storage_threads(storageLetter):
    folderdestination = os.path.join(str(storageLetter + ":\\"), "fill_storage")
    create_folder(folderdestination)
    thread1 = threading.Thread(target=create_zero_bytes_files, args=(folderdestination, 1024,))
    thread1.start()
    time.sleep(3)
    thread2 = threading.Thread(target=create_zero_bytes_files, args=(folderdestination, 1024,))
    thread2.start()

    for thread in [thread1, thread2]:
        thread.join()

    create_zero_bytes_files(folderdestination, 128)
    print("Storage " + storageLetter + " is full !")


def main():
    threads = []
    for storageLetter in storageLetters:
        print("Start to fill storage : " + storageLetter)
        storageThread = threading.Thread(target=fill_storage_threads, args=(storageLetter,))
        storageThread.start()
        threads.append(storageThread)
    for thread in threads:
        thread.join()


main()
