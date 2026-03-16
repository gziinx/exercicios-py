# 17. Leia uma frase e conte quantas palavras ela tem (dica: separar por espaços).

Frase = "eu sou o melhor"
palavras = 0
for i in Frase:
    if i != " ":
        palavras += 1
print(f"A sua frase: {Frase}, contém {palavras} palavras")