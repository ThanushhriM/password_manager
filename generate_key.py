from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate and save encryption key"""
    if os.path.exists("master.key"):
        print("✓ master.key already exists. Skipping generation.")
        return
    
    key = Fernet.generate_key()
    with open("master.key", "wb") as key_file:
        key_file.write(key)
    
    print("✓ Encryption key generated and saved as 'master.key'")

if __name__ == "__main__":
    generate_key()
