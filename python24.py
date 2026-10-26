peso = float(input("Peso (kg): "))#perguntando o peso
altura = float(input("Altura (m): "))#perguntando a altura

imc = peso / (altura * altura)#altura vezes altura dividido pelo peso é iagual a imc

if imc < 18.5:#se seu imc for baixo de 18.5 abaixo do peso
    classificacao = "Abaixo do peso"
elif imc < 25:#se seu imc for baixo de 25 peso normal
    classificacao = "Peso normal"
elif imc < 30:#se seu imc for baixo de sobrepeso
    classificacao = "Sobrepeso"
else:#se seu imc esta acima de 30 obesidade
    classificacao = "Obesidade"

print ("IMC:", imc,"Classificação:",classificacao)#mostra o resultado do imc e a classificação