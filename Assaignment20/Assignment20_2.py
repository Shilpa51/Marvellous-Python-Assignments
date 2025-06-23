import os
import hashlib
import sys

def get_file_checksum(path):
    hasher = hashlib.md5()
    try:
        with open(path, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception as e:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicate.py <Directory>")
        return

    directory = sys.argv[1]
    checksums = {}
    with open("Log.txt", "w") as log:
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                checksum = get_file_checksum(full_path)
                if not checksum:
                    continue
                if checksum in checksums:
                    log.write(f"Duplicate: {full_path}\n")
                else:
                    checksums[checksum] = full_path

if __name__ == "__main__":
    main()
