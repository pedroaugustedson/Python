a = int(input("Digite o primeiro lado:"))#Pergunta o primeiro lado
b = int(input("Digite o segundo lado:"))#Pergunta o segundo lado
c = int(input("Digite o terceiro lado: "))#Pergunta o terceiro lado

if a < b + c and b < a + c and c < a + b:#Cada lado precisa ser menor que a soma dos outros dois
    if a == b and b == c:  #Os tres lados iguais
        print("Equilátero")
    elif a == b or a == c or b == c:#se dois forem iguais
        print("Isósceles")
    else:# Nenhum lado igual
        print("Escaleno")
else:# Se não formar triângulo
    print("Esses lados não formam um triângulo")