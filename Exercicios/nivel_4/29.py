# 29. Leia uma palavra e verifique se ela é palíndromo (lê igual de trás para frente).

palavra = 'radar'

if palavra == palavra[::-1]:
    print(f"{palavra} é uma palvra paliíndromo")
else:
    print(f"{palavra} não é uma palvra paliíndromo")