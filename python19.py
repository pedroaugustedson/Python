nota1 = float(input("Nota 1:"))#perguntando a primeira nota
nota2 = float(input("Nota 2:"))#perguntando a segunda nota

media = (nota1 + nota2) / 2 # media igual a nota1 + nota2 dividido por 2

if media >= 7.0:#se nota for maior ou igual a 7 aprovado
    print("Aprovado")

elif media >= 5.0:#se a nota for maior ou igual a 5 recuperação
    print("Recuperação")

else:#se a nota for abaixo de 5 reprovado
    print("Reprovado")