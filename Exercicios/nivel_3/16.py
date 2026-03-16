# 16. Leia uma palavra e conte quantas vogais ela possui (considere a, e, i, o, u).

palavra = "Corinthians"
vericador = "aeiouAEIOU"
vogais = 0

for i in palavra:
    for j in vericador:
        if i == j:
            vogais = vogais + 1
    print(f"{i} vogais = {vogais}")
print(f"A palavra: {palavra} contém {vogais} vogais")