import psutil
import os
from pick import pick
from progress.bar import Bar
from cryptography.fernet import Fernet
import hashlib
import base64

def encrypt_file(file_path, password):
    # Hash password
    password = password.encode()
    hashed_password = hashlib.sha256(password).digest()
    key = base64.urlsafe_b64encode(hashed_password)

    # Create Fernet object
    cipher = Fernet(key)

    # Encrypt file
    with open(file_path, "rb") as f:
        # Read the plaintext from the file
        plaintext = f.read()
    ciphertext = cipher.encrypt(plaintext)

    # Save encrypted file
    new_file_path = file_path + ".encrypted"
    with open(new_file_path, "wb") as f:
        f.write(ciphertext)
    os.remove(file_path)

def decrypt_file(file_path, password):
    # Hash password
    password = password.encode()
    hashed_password = hashlib.sha256(password).digest()
    key = base64.urlsafe_b64encode(hashed_password)

    # Create Fernet object
    cipher = Fernet(key)

    # Decrypt file
    with open(file_path, "rb") as f:
        # Read the ciphertext from the file
        ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)

    # Save decrypted file
    original_file_path = file_path[:-10]
    with open(original_file_path, "wb") as f:
        f.write(plaintext)
    os.remove(file_path)

def get_disks():
    """
    Get all connected disks in the system
    """
    psutil_out = psutil.disk_partitions()
    drives = []
    for partition in psutil_out:
        drive = partition.mountpoint.replace("\\","/")
        try:
            os.listdir(drive) # Check if the partition is accessible
            drives.append(drive)
        except:
            print(f"Drive {drive} is not accessible")
    return drives

def get_files_from_drive(drive):
    """
    Get all files from a drive
    """
    files = []
    bar = Bar("Finding all files on the drive.......")

    for dirpath, dirnames, filenames in os.walk(drive):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)
            bar.next()
    bar.finish()
    return files

if __name__ == '__main__':
    drives = get_disks()

    title = "Please choose the disk to encrypt or decrypt"
    drive = pick(drives,title,indicator="=>",default_index=0); drive=drive[0]
    files = get_files_from_drive(drive)
    title = "Do you want to encrypt or decrypt"
    options = ["Encrypt","Decrypt"]
    selected = pick(options,title,indicator="=>",default_index=0); selected=selected[1]

    if selected == 0:
        # Encrypt files
        bar = Bar("Encrypting all files", max=len(files))
        password = input("Password for your files: ")
        for file in files:
            encrypt_file(file, password)
            bar.next()
        bar.finish()

    elif selected == 1:
        # Decrypt files
        bar = Bar("Decrypting all files", max=len(files))
        password = input("Password for your files: ")
        for file in files:
            decrypt_file(file, password)
            bar.next()
        bar.finish()