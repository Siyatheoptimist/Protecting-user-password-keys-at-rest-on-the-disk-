import os
import shutil
import getpass
import zipfile
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

# Generate a random key (File Encryption Key)
def generate_random_key():
    return AESGCM.generate_key(bit_length=256)

# Encrypt the data using the given key
def encrypt_data(data, key):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    encrypted_data = aesgcm.encrypt(nonce, data, None)
    return nonce + encrypted_data

# Decrypt the data using the given key
def decrypt_data(encrypted_data, key):
    aesgcm = AESGCM(key)
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]
    return aesgcm.decrypt(nonce, ciphertext, None)

# Derive a key from the user passphrase using a KDF
def derive_key_from_passphrase(passphrase, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())

# Archive a folder into a ZIP file
def archive_folder(folder_path):
    zip_file_path = folder_path + '.zip'
    shutil.make_archive(folder_path, 'zip', folder_path)
    
    # Add a marker file to the ZIP archive to indicate it was created by our program
    with zipfile.ZipFile(zip_file_path, 'a') as zipf:
        zipf.writestr('encrypted_by_program.marker', 'This ZIP was created for folder encryption')
    
    return zip_file_path

# Extract a ZIP file to a folder and remove the marker file
def extract_zip(zip_file_path, extract_to_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
    
    # Remove the marker file after extraction
    marker_file_path = os.path.join(extract_to_folder, 'encrypted_by_program.marker')
    if os.path.exists(marker_file_path):
        os.remove(marker_file_path)

# Check if a ZIP file contains our marker file
def is_program_created_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        return 'encrypted_by_program.marker' in zipf.namelist()

# Function to encrypt a file
def protect_file(file_path, passphrase):
    try:
        # Generate a random File Encryption Key
        file_encryption_key = generate_random_key()
        
        # Read the file data
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        # Encrypt the file data using the File Encryption Key
        encrypted_file_data = encrypt_data(file_data, file_encryption_key)
        
        # Save the encrypted file data
        encrypted_file_path = file_path + '.enc'
        with open(encrypted_file_path, 'wb') as file:
            file.write(encrypted_file_data)
        
        # Derive a key from the user passphrase
        salt = os.urandom(16)  # A new random salt for key derivation
        derived_key = derive_key_from_passphrase(passphrase, salt)
        
        # Encrypt the File Encryption Key using the derived key
        encrypted_fek = encrypt_data(file_encryption_key, derived_key)
        
        # Save the encrypted FEK and salt to a file
        with open(file_path + '.key', 'wb') as key_file:
            key_file.write(salt + encrypted_fek)
        
        # Delete the original file
        os.remove(file_path)
    except Exception as e:
        print(f"Error protecting file {file_path}: {e}")

# Function to decrypt a file
def decrypt_file(encrypted_file_path, key_file_path, passphrase):
    try:
        # Read the encrypted file data
        with open(encrypted_file_path, 'rb') as file:
            encrypted_file_data = file.read()
        
        # Read the salt and encrypted FEK
        with open(key_file_path, 'rb') as key_file:
            data = key_file.read()
            salt = data[:16]
            encrypted_fek = data[16:]
        
        # Derive the key from the user passphrase
        derived_key = derive_key_from_passphrase(passphrase, salt)
        
        # Decrypt the FEK using the derived key
        file_encryption_key = decrypt_data(encrypted_fek, derived_key)
        
        # Decrypt the file data using the decrypted FEK
        decrypted_file_data = decrypt_data(encrypted_file_data, file_encryption_key)
        
        # Save the decrypted file data
        decrypted_file_path = encrypted_file_path.replace('.enc', '')
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_file_data)
        
        print(f"File '{encrypted_file_path}' decrypted successfully.")
    except Exception:
        print("Invalid passphrase.")

# Function to decrypt a ZIP file
def decrypt_zip(encrypted_zip_path, passphrase):
    try:
        # Decrypt the ZIP file
        key_file_path = encrypted_zip_path.replace('.enc', '.key')
        decrypt_file(encrypted_zip_path, key_file_path, passphrase)
        
        # Check if the ZIP file was created by our program
        decrypted_zip_path = encrypted_zip_path.replace('.enc', '')
        if is_program_created_zip(decrypted_zip_path):
            base_folder_path = decrypted_zip_path.replace('.zip', '')
            extract_zip(decrypted_zip_path, base_folder_path)
            os.remove(decrypted_zip_path)
            print(f"Folder '{base_folder_path}' decrypted successfully.")
        else:
            print(f"ZIP file '{decrypted_zip_path}' decrypted successfully.")
    except Exception as e:
        print(f"Error decrypting ZIP file {encrypted_zip_path}: {e}")

# Function to encrypt a folder
def encrypt_folder(folder_path, passphrase):
    try:
        # Archive the folder into a ZIP file
        zip_file_path = archive_folder(folder_path)
        
        # Encrypt the ZIP file
        protect_file(zip_file_path, passphrase)
        
        # Delete the original folder after encryption
        shutil.rmtree(folder_path)
        
        print(f"Folder '{folder_path}' encrypted successfully.")
    except Exception as e:
        print(f"Error encrypting folder {folder_path}: {e}")

# Main menu-driven function
def main():
    while True:
        print("1. Encrypt File/Folder")
        print("2. Decrypt File/Folder")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            path = input("Enter the file/folder path to encrypt: ")
            passphrase = getpass.getpass(prompt='Enter passphrase: ')
            if os.path.isfile(path):
                protect_file(path, passphrase)
                print(f"File '{path}' encrypted successfully.")
            elif os.path.isdir(path):
                encrypt_folder(path, passphrase)
                print(f"Folder '{path}' encrypted successfully.")
            else:
                print("Invalid path.")
        
        elif choice == '2':
            path = input("Enter the encrypted file/folder path to decrypt: ")
            passphrase = getpass.getpass(prompt='Enter passphrase: ')
            if os.path.isfile(path) and path.endswith('.zip.enc'):
                decrypt_zip(path, passphrase)
            elif os.path.isfile(path) and path.endswith('.enc'):
                key_file_path = path.replace('.enc', '.key')
                decrypt_file(path, key_file_path, passphrase)
            else:
                print("Invalid path or file is not encrypted.")
        
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
