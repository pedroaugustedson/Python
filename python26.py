compra = float(input("Valor da compra (R$): "))#perguntando o valor da compra 

if compra < 50:#se compra for menor que 50 desconto 0%
    percentual = 0
elif compra < 100:#se compra for menor que 100 desconto 5%
    percentual = 5
elif compra < 200:#se compra for menor que 200 desconto 10%
    percentual = 10
else:#se compra for maior ou igual a  200 desconto 15%
    percentual = 15

desconto = compra * percentual / 100#desconto é igual a 100 divido por percentual vezes compra
valor_final = compra - desconto#valor_final é igual a compra menos desconto

print("Desconto: R$", desconto)#mostra o valor do desconto
print ("Valor final: R$", valor_final)#mostra o valor final da compra


