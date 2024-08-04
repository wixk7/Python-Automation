import os
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, key):
    fernet = Fernet(key)
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    decrypted_file_path = encrypted_file_path.replace('.encrypted', '')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    os.remove(encrypted_file_path)
    print(f'File decrypted to: {decrypted_file_path}')
    return decrypted_file_path

def decrypt_folder(encrypted_folder_path, key):
    for root, _, files in os.walk(encrypted_folder_path):
        for file in files:
            encrypted_file_path = os.path.join(root, file)
            decrypt_file(encrypted_file_path, key)
    print(f'All files in folder {encrypted_folder_path} decrypted.')
    return encrypted_folder_path

encrypted_folder_path = r'SupportFiles'
key = b'iGN5XGf28DYoqHqmu6k5m17LEoEJj0MDx4gtKFAKPRg='

decrypt_folder(encrypted_folder_path, key)
