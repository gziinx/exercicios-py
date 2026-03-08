# 7. Leia 3 lados e verifique se formam triângulo. Se formar, classifique: equilátero, isósceles ou escaleno

l1 = float(input("Digite o primeiro lado do triangulo:"))
l2 = float(input("Digite o segundo lado do triangulo:"))
l3 = float(input("Digite o terceiro lado do triangulo:")) 

if l1 == l2 and l1 == l3:
    print("O seu triangulo é equilátero")
elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2:
    print("O seu triangulo é isóceles")
elif l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print("Triangulo invalido, a soma dos dois menores são menor que a maior")
else:
    print("O seu triangulo é escaleno")
