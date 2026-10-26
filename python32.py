usuario = input("Digite o usuário:")#Pergunta o usuario
senha = input("Digite a senha:")#Pergunta a senha

if usuario == "aluno":#Primeiro verifica se o usuário está certo
    if senha == "1234":#se a senha for igual a 1234 login realizado com sucesso
        print("Login realizado com sucesso!")
    else:#Usuario certo senha errada
        print("Senha incorreta")
else:
    print("Usuário não encontrado")#Usuario errado