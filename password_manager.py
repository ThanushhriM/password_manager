from cryptography.fernet import Fernet
import json
import os

VAULT_DIR = "data"
VAULT_FILE = os.path.join(VAULT_DIR, "vault.enc")
KEY_FILE = "master.key"

def _ensure_vault_dir():
    """Create data directory if it doesn't exist"""
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)

def load_key():
    """Load encryption key from master.key file"""
    try:
        with open(KEY_FILE, "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {KEY_FILE} not found. Run 'python generate_key.py' first.")
        exit(1)

key = load_key()
fernet = Fernet(key)

def save_passwords(data):
    """Save encrypted passwords to vault"""
    _ensure_vault_dir()
    try:
        encoded = json.dumps(data).encode()
        encrypted = fernet.encrypt(encoded)
        with open(VAULT_FILE, "wb") as file:
            file.write(encrypted)
    except Exception as e:
        print(f"Error saving passwords: {e}")

def load_passwords():
    """Load and decrypt passwords from vault"""
    _ensure_vault_dir()
    try:
        if not os.path.exists(VAULT_FILE):
            return {}
        with open(VAULT_FILE, "rb") as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
        return json.loads(decrypted.decode())
    except Exception as e:
        print(f"Error loading passwords: {e}")
        return {}

def add_password(account, password):
    """Add or update password for an account"""
    data = load_passwords()
    data[account] = password
    save_passwords(data)
    print(f"✓ Password saved for {account}")

def get_password(account):
    """Retrieve password for an account"""
    data = load_passwords()
    if account in data:
        return data[account]
    return "❌ Account not found."
