with open("../dados/exercicio_1_modulo_2.txt", "r") as arquivo:
    conteudo = arquivo.read().split(",")

with open("../dados/resultado1.txt", "w") as resultado:
    for item in conteudo:
        texto = f"Novo conteúdo {item.strip()}\n"
        resultado.write(texto)
