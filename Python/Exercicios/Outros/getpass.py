# https://github.com/RochaGabriell
from getpass import getpass

user = input("Username: ")
password = getpass("Password: ") # fornece uma maneira segura de lidar com os prompts de senha, via terminal

print(user, password)