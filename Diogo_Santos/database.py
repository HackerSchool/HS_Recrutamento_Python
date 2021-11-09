'''
Set of functions to interact with the database
'''

import re
import os
import hashlib
import json
import base64


def checkCorrectCredentials(userName: str, userPassword: str) -> bool:
        if(checkNameExists(userName) and checkCorrectPassword(userName,userPassword)):
            return True
        else:
            return False


def checkNameExists(userName: str) -> bool:
    with open("database.json","r") as json_file:
        db = json.load(json_file)
        users = db["users"]
        for user in users:
            if (user["name"] == userName):
                return True

        return False


def checkCorrectPassword(userName: str, userPassword: str) -> bool:
    with open("database.json","r") as json_file:
        db = json.load(json_file)
        users = db["users"]
        for user in users:
            if (user["name"] == userName):
                # Note: user["salt"] is str, need to cast to byte
                # [2:-1] to remove b'..'
                bytes_salt = bytes(user["salt"][2:-1],"utf-8")
                bytes_key = bytes(user["key"][2:-1],"utf-8")

                return unhash(userPassword,bytes_salt,bytes_key) 
            

def checkStrengthPassword(userPassword: str) -> int:
    length = len(userPassword)
    hasLength = None if length < 5 else length
    hasDigit = re.search(r"[0-9]", userPassword)
    hasUpper = re.search(r"[A-Z]", userPassword)
    hasLower = re.search(r"[a-z]", userPassword)

    strength = 0
    for verification in [hasLength,hasDigit,hasUpper,hasLower]:
        if verification != None:
            strength += 4
                
    return strength


def changePassword(userName: str, newPassword: str) -> None:

    salt,key = hash(newPassword)

    with open("database.json","r") as json_file:

        db = json.load(json_file)
        users = db["users"]

    for user in users:
        if(user["name"] == userName):
            user["salt"] = str(salt)
            user["key"] = str(key)

    with open("database.json","w") as json_file:
        json.dump(db,json_file,indent=4)


def addNewUser(userName: str, userPassword: str) -> None:

    salt,key = hash(userPassword)

    with open("database.json","r") as json_file:

        db = json.load(json_file)
        users = db["users"]

        new_user = {"name": userName, "salt": str(salt), "key": str(key)} 
        users.append(new_user)

    with open("database.json","w") as f:
        json.dump(db,f,indent=4)


def hash(userPassword: str) -> bytes:
    # Generate random salt unique for each user
    # Adds difficulty for brute force attacks and rainbow tables
    # Forces attacker to separately attack each individual 
    salt = os.urandom(32)
    # Generate key based on password and salt
    key = hashlib.pbkdf2_hmac(
        'sha256',
        userPassword.encode('utf-8'), 
        salt, 
        100000 
    )
    # Encode bytes in base64
    salt = base64.b64encode(salt)
    key = base64.b64encode(key)

    return salt,key


def unhash(passwordToCheck: str, salt: bytes, key: bytes) -> bool:
    # Decode bytes from base64
    salt = base64.b64decode(salt)
    key = base64.b64decode(key)
    # Generate key based on password and salt
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        passwordToCheck.encode('utf-8'),
        salt, 
        100000
    )
    # If keys do not match
    # It means that the password used to generate the key is 
    # different from the original

    return True if new_key == key else False