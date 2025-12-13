from password_manager import add_password, get_password
from auth import authenticate

def main():
    authenticate()  # Authenticate before accessing vault
    
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            add_password(account, password)
            
        elif choice == "2":
            account = input("Enter account name: ")
            print("Password:", get_password(account))
            
        elif choice == "3":
            print("Exiting...")
            break
            
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
