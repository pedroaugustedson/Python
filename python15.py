valor = float(input("Digite o valor da compra:"))#Pergunta o valor da compra

desconto = valor * 0.10#Valor da compra vezez 10% que é o valor do desconto
final = valor - desconto#valor menos o desconto para saber o valor final

if valor >= 100:#se 100 for maior que tem desconto se nao sem desconto
    print("Valor final: R$", final)

else:
    print("Valor final: R$", valor)