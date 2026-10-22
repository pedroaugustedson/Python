n1 = float(input("Digite sua primeira nota")) #Perguntando a primeira nota e guardando na variavel n1
n2 = float(input("Digite sua segunda nota")) #Perguntando a segunda nota e guardando na variavel n2

media = (n1 + n2) /2 #media igual a n1 + n2 dividido por 2

if media >=7 : 
    print ("Média:", media, "-- Aprovado")# se media for maior que 7 aprovado

else:
    print ("Média:", media, "-- Reprovado")#se media for menor que 7 reprovado

