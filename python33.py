idade = int(input("Digite a idade: "))#Pergunta a idade

if idade < 16:#se idade for menor que 16 nao pode votar
    print("Não pode votar")
elif idade < 18 or idade > 70:#se a idade for menor que 18 ou maior que 70 nao e obrigatorio a votar
    print("Voto facultativo")
else:#se nao voto obrigatorio
    print("Voto obrigatório")