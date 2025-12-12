import hashlib
import os

MASTER_FILE = "master.pass"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup_master_password():
    if os.path.exists(MASTER_FILE):
        return  # already exists

    password = input("Create a master password: ")
    confirm = input("Confirm master password: ")

    if password != confirm:
        print("Passwords do not match. Try again.")
        return setup_master_password()

    hashed = hash_password(password)
    with open(MASTER_FILE, "w") as f:
        f.write(hashed)
    print("Master password set successfully!")

def authenticate():
    if not os.path.exists(MASTER_FILE):
        setup_master_password()

    stored_hash = open(MASTER_FILE).read().strip()

    while True:
        entered = input("Enter master password: ")
        if hash_password(entered) == stored_hash:
            print("Authentication successful!")
            return True
        else:
            print("Incorrect password. Try again.")
