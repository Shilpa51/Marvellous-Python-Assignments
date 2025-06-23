import os
import hashlib
import sys

def calculate_checksum(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryChecksum.py <Directory>")
        return
    
    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    with open("Log.txt", "w") as log:
        for root, _, files in os.walk(directory):
            for name in files:
                path = os.path.join(root, name)
                checksum = calculate_checksum(path)
                log.write(f"{path} -> {checksum}\n")

if __name__ == "__main__":
    main()
