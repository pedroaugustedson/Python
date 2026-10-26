print("CARDÁPIO")#enviando o cardapio
print("1 - Pão de queijo - R$ 4.50")#preço do pao de quijo
print("2 - Coxinha - R$ 6.00")#preço da coxinha
print("3 - Pastel - R$ 7.00")#perço do pastel
print("4 - Suco - R$ 5.00")#preço do suco
print("5 - Café - R$ 3.00")#preço do café

codigo = int(input("Código:"))#pergunta o código
quantidade = int(input("Quantidade: "))#pergunta a quantidade

if codigo == 1:#se ele digitar codigo 1 o valor é 4.50
    preco = 4.50
elif codigo == 2:#se ele digitar codigo 2 o valor é 6.00
    preco = 6.00
elif codigo == 3:#se ele digitar codigo 3 o valor é 7.00
    preco = 7.00
elif codigo == 4:#se ele digitar codigo 4 o valor é 5.00
    preco = 5.00
elif codigo == 5:#se ele digitar codigo 5 o valor é 3.00
    preco = 3.00
else:
    preco =0#qualquer outro nome é invalido
    print("Código inválido")#se for qualquer outro nmero

total = preco * quantidade#calculo preco vezes quantidade

print(f"Total: R$ {total}")#mostra o total
