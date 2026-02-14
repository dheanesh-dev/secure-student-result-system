import json
import os
from utils import hash_password, verify_password, is_valid_username, is_valid_password

USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def register_user():
    users = load_users()
    print("\n=== REGISTER USER ===")

    username = input("Username: ").strip()
    if not is_valid_username(username):
        print("❌ Invalid username (min 4 chars, letters/numbers/_ only)")
        return

    if username in users:
        print("❌ Username already exists")
        return

    password = input("Password: ").strip()
    if not is_valid_password(password):
        print("❌ Password must be at least 6 characters")
        return

    role = input("Role (admin/teacher/student): ").strip().lower()
    if role not in ["admin", "teacher", "student"]:
        print("❌ Invalid role")
        return

    users[username] = {
        "password": hash_password(password),
        "role": role
    }

    save_users(users)
    print("✅ User registered successfully")


def login_user():
    users = load_users()
    print("\n=== LOGIN ===")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username not in users:
        print("❌ User not found")
        return None

    if not verify_password(password, users[username]["password"]):
        print("❌ Incorrect password")
        return None

    print(f"✅ Login successful ({users[username]['role']})")
    return {
        "username": username,
        "role": users[username]["role"]
    }
