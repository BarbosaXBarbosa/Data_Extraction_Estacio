# -*- coding: utf-8 -*-

import os

try:
    os.remove("dados/teste.txt")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição: ", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo.")
    print("Descrição: ", erro)
except IsADirectoryError as erro:
    print("Remove serve apenas para arquivos.")
    print("Descrição: ", erro)

print("Término do programa")

