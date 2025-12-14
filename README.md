# 🔐 Password Manager (Python)

A simple **command-line Password Manager** built using Python. This project allows users to securely store and retrieve passwords for different accounts after authentication.

---

## 📌 Features

* 🔑 Master authentication before access
* ➕ Add passwords for accounts
* 🔍 Retrieve stored passwords
* 🧩 Modular code structure
* 🖥️ Simple CLI-based interface

---

## 📂 Project Structure

```
password-manager/
│
├── main.py                # Entry point (menu & control flow)
├── password_manager.py    # Logic to add and retrieve passwords
├── auth.py                # Authentication logic
├── passwords.txt          # Stored passwords (auto-created)
└── README.md              # Project documentation
```

---

## ⚙️ How It Works

1. User runs the program
2. Authentication is required (master password)
3. Menu options are displayed:

   * Add a password
   * Get a password
   * Exit
4. Passwords are stored and retrieved using file handling

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/password-manager.git
```

2. Navigate into the project directory:

```bash
cd password-manager
```

3. Run the program:

```bash
python main.py
```

---

## 🧪 Example Usage

```
Password Manager
1. Add Password
2. Get Password
3. Exit

Choose an option: 1
Enter account name: gmail
Enter password: mypassword123
```

---

## 🛡️ Security Note

⚠️ This project is for **learning purposes only**.

* Passwords are stored in plain text
* Printing passwords is not secure

For real-world usage, encryption and secure storage should be implemented.

---

## 🚀 Future Improvements

* Encrypt stored passwords
* Hide password input (`getpass`)
* Update & delete password options
* Limit authentication attempts
* Use a database instead of text files

---

## 🧑‍💻 Author

Thanushhri M

---

## 📄 License

This project is open-source and free to use for educational purposes.
