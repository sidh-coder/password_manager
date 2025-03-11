
import modules.encryption as encrypt

salt = b'unique_salt'
masterpass = input("enter master password :")

key = encrypt.hash(masterpass)
while True:
    login = input("enter masterpass again :")

    verify = encrypt.verifylogin(key,masterpass)
    if(verify==True):
        print("logged in")
        password = input("enter password :")
        key=encrypt.encrypt_key(masterpass,salt)
        cipher_text=encrypt.encrypt_password(password,key)
        masterpass2 = input("enter master password again :")
        try:
            password=encrypt.decrypt_password(key,cipher_text)
            print(password)
        except:
            print("wrong masterpass")
    else:
        print("wrong password, try again")
