saldo = float(input("Saldo: "))#Perguntando o Saldo 
saque = float(input("Saque: "))#Perguntado o Saque

NovoSaldo = saldo - saque#saldo menos saque vira o novo saldo

if saldo >= saque:#se o saldo for maior ou igual ao saque saque realizado se nao saque insuficiente
    print ("Saque realizado. Novo saldo: R$ ", NovoSaldo)

else:
    print("Saque insuficiente")