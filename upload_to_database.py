import streamlit_authenticator as stauth

import database as db

usernames = ["pparker", "rmiller"]
names = ["Peter Parker", "Rebecca Miller"]
passwords = ["abc123", "def456"]
hashed_passwords = stauth.Hasher(passwords).generate()


for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)