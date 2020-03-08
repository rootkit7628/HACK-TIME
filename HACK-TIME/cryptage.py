import hashlib

def cryptage(pswd):
    key=hashlib.md5(bytes(pswd,'utf-8')).hexdigest()
    return key;

a=input("Ton mot de passe >>>")
b=cryptage(a)

print(b)