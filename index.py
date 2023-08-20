import os
import hashlib

# Function to calculate MD5 hash of a file
def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# Function to scan a directory for potentially malicious files
def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            md5_hash = calculate_md5(file_path)
            print(f"Scanning: {file_path}, MD5: {md5_hash}")

            # Add your malware detection logic here
            # For demonstration purposes, we'll just print a message
            if "malicious" in file:
                print(f"!!! Potentially malicious file found: {file_path} !!!")

# Main function
if __name__ == "__main__":
    directory_to_scan = "/path/to/scan"
    scan_directory(directory_to_scan)
