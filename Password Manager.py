from cryptography.fernet import Fernet
import os
import json

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_password(password, key):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password.encode()).decode()

def save_password(account, username, password):
    if not os.path.exists("key.key"):
        generate_key()
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    data = {}
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            data = json.load(file)
    data[account] = {"username": username, "password": encrypted_password}
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Password saved successfully!")

def retrieve_password(account):
    if not os.path.exists("key.key") or not os.path.exists("passwords.json"):
        print("No saved passwords found.")
        return
    key = load_key()
    with open("passwords.json", "r") as file:
        data = json.load(file)
    if account in data:
        username = data[account]["username"]
        password = decrypt_password(data[account]["password"], key)
        print(f"Account: {account}\nUsername: {username}\nPassword: {password}")
    else:
        print("Account not found.")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Save a password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            account = input("Enter account name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(account, username, password)
        elif choice == "2":
            account = input("Enter account name: ")
            retrieve_password(account)
        elif choice == "3":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()