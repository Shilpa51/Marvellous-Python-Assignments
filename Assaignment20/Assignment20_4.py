import os
import hashlib
import sys
import time

def get_checksum(path):
    hasher = hashlib.md5()
    try:
        with open(path, 'rb') as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    except Exception:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicateRemoval.py <Directory>")
        return

    start_time = time.time()
    directory = sys.argv[1]
    checksums = {}

    with open("Log.txt", "w") as log:
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                checksum = get_checksum(full_path)
                if not checksum:
                    continue
                if checksum in checksums:
                    log.write(f"Deleted Duplicate: {full_path}\n")
                    os.remove(full_path)
                else:
                    checksums[checksum] = full_path

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
