import base64
from argon2 import PasswordHasher
from cryptography.fernet import Fernet #https://www.sqlshack.com/encrypting-passwords-with-python-scripts-in-sql-notebooks-of-azure-data-studio/
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

ph = PasswordHasher()

def hash(master_password):
    key = ph.hash(master_password)
    return(key)

def verifylogin(key,master_password):
    if(ph.verify(key,master_password)):
        return(True)
    else:
        return(False)

def encrypt_key(master_password,salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(master_password)
    return base64.urlsafe_b64encode(key)

def encrypt_password(password,key):
    cipher = Fernet(key)
    ciphered_text = cipher.encrypt(password.encode('utf-8'))
    return(ciphered_text)

def decrypt_password(key,cipher_text):
    cipher = Fernet(key)
    try:
        password = cipher.decrypt(cipher_text)
        return(password)
    except:
        raise Exception("wrong password error")