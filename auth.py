import hashlib
import os

MASTER_FILE = "master.pass"

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def setup_master_password():
    """Setup master password on first run"""
    if os.path.exists(MASTER_FILE):
        return  # Already exists
    
    password = input("Create a master password: ")
    confirm = input("Confirm master password: ")
    
    if password != confirm:
        print("❌ Passwords do not match. Try again.")
        return setup_master_password()
    
    hashed = hash_password(password)
    with open(MASTER_FILE, "w") as f:
        f.write(hashed)
    
    print("✓ Master password set successfully!")

def authenticate():
    """Authenticate user with master password"""
    if not os.path.exists(MASTER_FILE):
        setup_master_password()
    
    with open(MASTER_FILE, "r") as f:
        stored_hash = f.read().strip()
    
    while True:
        entered = input("Enter master password: ")
        if hash_password(entered) == stored_hash:
            print("✓ Authentication successful!")
            return True
        else:
            print("❌ Incorrect password. Try again.")
