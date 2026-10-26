nota1 = float(input("Digite a primeira nota:"))#Pergunta a primeira nota
nota2 = float(input("Digite a segunda nota:"))#Pergunta a segunda nota
frequencia = float(input("Digite a frequência (em %):"))#Pergunta a frequência em porcentagem

media = (nota1 + nota2) / 2 #soma as duas notas e dividi por dois
if frequencia < 75:#se frequencia for menor que 75% reprovado por falta
    print("Reprovado por falta")
elif media < 7.0:#se nota for abaixo de 7 reprovado por nota
    print("Reprovado por nota")
else:#se nao aprovado
    print("Aprovado")