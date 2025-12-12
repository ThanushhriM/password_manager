from cryptography.fernet import Fernet
import json, os

def load_key():
    with open("master.key", "rb") as file:
        return file.read()

key = load_key()
fernet = Fernet(key)

VAULT_FILE = "data/vault.enc"

def save_passwords(data):
    encoded = json.dumps(data).encode()
    encrypted = fernet.encrypt(encoded)
    with open(VAULT_FILE, "wb") as file:
        file.write(encrypted)

def load_passwords():
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, "rb") as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    return json.loads(decrypted.decode())

def add_password(account, password):
    data = load_passwords()
    data[account] = password
    save_passwords(data)
    print(f"Password saved for {account}")

def get_password(account):
    data = load_passwords()
    if account in data:
        return data[account]
    return "Account not found."
