# 18. Leia 10 notas (0 a 10) e calcule a média. Depois, informe quantas ficaram acima da média.
notas = [7,5,6,8,10,6,3,9,8,10]
total = 0
for i in notas:
    total = total + i

media = total / 10
acima = 0
for i in notas:
    if i > media:
        acima += 1
print(f"{acima} alunos ficou acima da média de {media}")