
import modules.database as db
import modules.encryption as encrypt
salt = b'unique_salt'

def user_pass(user):
    while True:
        print("Enter 1 to add new password\nEnter 2 to view exsisting passwords\nEnter 3 to exit")
        ip = int(input())
        if ip == 1:
            site_name = input("enter site name: ")
            password = input("enter password: ")
            key = encrypt.encrypt_key(user['master_password'],salt)
            encrypted_password = encrypt.encrypt_password(password,key)
            db.add_entry(site_name,user['username'],encrypted_password)
            print("successfully added password")

        elif ip == 2:
            key = encrypt.encrypt_key(user['master_password'],salt)
            site_name = input("enter site name")
            result = db.get_entry(site_name,user['username'])
            ciphered_password = result['password']
            deciphered_password = encrypt.decrypt_password(key,ciphered_password)
            print(deciphered_password)
        else:
            break

def createuser():
    username=input("Enter username: ")
    email = input("enter email id: ")
    for i in range(3):
        password1 = input("enter master password: ")
        password2 = input("enter master password again: ")
        if(password1==password2):
            key = encrypt.hash(password1)
            db.add_user(username,key,email)
            print("user has been created")
            break
        else:
            print("try again, passwords donot match")

def login():
    username = input("enter username: ")
    user = db.list_user_data(username)
    if user!=False:
        for i in range(10):
            password = input("enter master password: ")
            if(encrypt.verifylogin(user['master_password'],password)):
                print("you are successfully Logged in")
                user_pass(user)
            else:
                print("password is incorrect, you have "+10-i+" chances remaining ")
        db.delete_user(username)
        print("sorry too many wrong attempts. DELETING PASSWORDS...")


while True:
    print("Enter 1 to create new user\nEnter2 if existing user\nEnter 0 to exit\n")
    ip = int(input())
    if ip == 1:
        createuser()
    elif ip ==2:
        login()
    else:
        exit()
