n1 = int(input("Digite o pirmeiro número:"))#perguntando o primeiro numero
n2 = int(input("Digite o segundo número:"))#perguntando o segundo numero
n3 = int(input("Digite o terceiro número:"))#perguntando o terceiro numero

if n1 > n2 and n1 > n3:#se n1 é maior que n2 e n1 maior n3
    print("O maior é", n1)
elif n2 > n3:#se n2 for maior que n3
    print("O maior é", n2)
else:#se nao for o n3 é maior
    print("O maior é", n3)