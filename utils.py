import hashlib
import re


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed):
    return hash_password(password) == hashed


def is_valid_username(username):
    return bool(re.match(r"^[A-Za-z0-9_]{4,}$", username))


def is_valid_password(password):
    return len(password) >= 6
