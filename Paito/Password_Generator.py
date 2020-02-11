import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
length = input("Tamanho da Senha: ")
length = int(length)
many = input("Quantas Senhas: ")
many = int(many)
for p in range(many):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print("\n"+password)
