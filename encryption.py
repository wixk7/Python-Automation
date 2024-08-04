import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(file_path)
    return encrypted_file_path

def encrypt_folder(folder_path, key):
    encrypted_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypted_file_path = encrypt_file(file_path, key)
            encrypted_files.append(encrypted_file_path)
    return encrypted_files

def main(folder_path):
    key = Fernet.generate_key()
    print(f'Encryption Key: {key.decode()}')
    encrypted_files = encrypt_folder(folder_path, key)
    for encrypted_file in encrypted_files:
        print(f'File encrypted to: {encrypted_file}')
    return encrypted_files, key

folder_path = r'SupportFiles'
encrypted_files, key = main(folder_path)
