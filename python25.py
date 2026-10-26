limite = float(input("Limite da via (km/h): "))#perguntado o limite da via
velocidade = float(input("Velocidade medida (km/h): "))#perguntando a velocidade

percentual = (velocidade - limite) / limite * 100#limite vezes 100 dividido por limite - velocidade = percentual

if velocidade <= limite:#se velocidade for limite sem infração
    print("Sem infração")
elif percentual <= 20:#se o pencentual for menor que 20 infração media
    print("Infração média")
elif percentual <= 50:#se o percentual for menor ou igual que 50 Infração grave
    print("Infração grave")
else:#se o percentual for maior ou igual que 50 Infração gravíssima
    print("Infração gravíssima")