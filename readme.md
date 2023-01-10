# File Encryption/Decryption Script

This script allows a user to encrypt or decrypt all files on a chosen disk. It uses the Fernet module from the cryptography library to handle the encryption and decryption.

## Requirements

- Python 3.x
- psutil library
- pick library
- progress library
- cryptography library

## Usage

1. Run the script using `python main.py`
2. Select the disk on which you want to encrypt or decrypt files.
3. Select whether you want to encrypt or decrypt the files.
4. Enter a password that will be used to encrypt or decrypt the files.
5. Wait for the script to complete. All the files on the chosen disk will be encrypted or decrypted.

## Note
- Make sure to remember your password, otherwise you will not be able to decrypt the files.
- This script does not handle the possibility that user enters wrong password for decryption and it does not cover all the possible exception cases.
- If you encounter any issues or have any questions, please feel free to reach out to me.

### Note for Windows users:

- If you are using this script on Windows, please be aware that the operating system may flag the script as a potential threat (such as a ransomware) because it is designed to encrypt files.
- This is a false positive and the script does not contain any malware.