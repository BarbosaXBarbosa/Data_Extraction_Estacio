# -*- coding: utf-8 -*-

import os

try:
    os.rename("dados/teste.txt", "dados/teste_beta.txt")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição: ", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo.")
    print("Descrição: ", erro)
except FileExistsError as erro:
    print("Arquivo destino já existe.")
    print("Descrição: ", erro)

print("Término do programa")


# Se precisarmos renomear sobrescrevendo o arquivo de destino, caso ele exista, podemos utilizar a função replace