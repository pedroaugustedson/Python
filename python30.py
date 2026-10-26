ano = int(input("Digite um ano: "))  #Pergunta o ano

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:#Divisível por 4 e não por 100 ou divisível por 400
    print("Bissexto")# Se a regra for cumprida, é bissexto
else:
    print("Não é bissexto")#Se não o resultado é não é bissexto
