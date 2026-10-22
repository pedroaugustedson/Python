idade = int(input("Idade: "))#perguntando a idade

if idade < 0:#se idade for menor que zero idade invalida
    print("Idade inválida")
    
elif idade <= 12:#se idade for igual ou menor que doze criança
    print("Criança")

elif idade <= 17:#se idade for igual ou menor que 17 adolecente
    print("Adolescente")

elif idade <= 59:#se idade for igual ou menor que 59 adulto
    print("Adulto")

else:# se idade for acima de 59 idoso
    print("Idoso")