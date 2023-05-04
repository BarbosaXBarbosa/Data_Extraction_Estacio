# -*- coding: utf-8 -*-

try:
    open("../dados/arquivoinexistente.txt", 'r')
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição: ", erro)

print("Término programa")
