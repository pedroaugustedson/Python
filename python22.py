temp = float(input("Temperatura (°C): "))#perguntado a temperatura

if temp < 0:#se a temperatura for abaixo de 0 o resultado é Abaixo de zero - risco de geada!
    print("Abaixo de zero - risco de geada!")

elif temp < 10:#se a temperatura for abaixo de 10 o resultado é Muito frio - capriche no agasalho
    print("Muito frio - capriche no agasalho")

elif temp < 18:#se a temperatura for abaixo de 18 o resultado é Frio
    print("Frio")

elif temp < 25:#se a temperatura for abaixo de 25 o resultado é Agradável
    print("Agradável")

else:#se a temperatura for acima de 25 o resultado é Calor
    print("Calor")