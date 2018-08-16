
""" Elwyn Omanga """
password = 0
try:
    password = input("Enter a password at least 10 characters long: ")
except len(password) < 1:
    password = input("Enter a password at least 10 characters long: ")
while len(password) < 10:
    password = input("Enter a password at least 10 characters long: ")
print('*'*len(password))

