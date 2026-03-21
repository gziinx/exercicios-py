# 23. Leia N números e determine o segundo maior valor (considere que pode haver repetidos)

n = [2793,432,808000,24893,325,32,205,89892]
maior = 0
segundo = 0
for i in n:
    if i > maior:
        maior = i
        for j in n:
            if j > segundo  and j < maior:
                segundo = j
print(maior)
print(segundo)