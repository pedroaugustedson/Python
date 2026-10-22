preco = float(input("Digite o preço do lanche: "))#Pergunta o valor do lanche
quantidade = int(input("Digite a quantidade comprada: "))#Pergunta a quantidade que foi comprada
pago = float(input("Digite o valor pago: "))#Pergunta o valor que foi pago

total = preco * quantidade # preço do lanche X quantidade comprada = total

troco =  pago - total# valor que foi pagado X o valor total da compra = troco

print ("Total: R$", total)#Diz o valor que foi a compra
print ("Troco: R$", troco)#Diz o troco da compra
