# Relatório :

# SISTEMA DE LOGIN E CADASTRO 

# 1 - O Sistema de Login deve Permitir que novos usuarios sejam Cadastrados.
# 2 - O Sistema NÃO deve permitir que usuarios duplicados sejam Cadastrados.
# 3 - Permitir que usuarios existentes possam fazer o Login.
# 4 - O Sistema deve alertar caso a senha e login não estejam corretos.

'''
Metodo do 5 Q's Para cada uma das Aplicações.

Quais são os Dados de entrada necessarios? 
    - Usuario, Senha.

O Que devo fazer com estes Dados?
    - Registrar o Usuario e Senha que foi Digitado.

Quais são as Restrições deste Problema?
    - Não Permitir Cadastro de Usuarios já Existentes.

Qual é o Resultado Esperado?
    - Um Novo Usuario e Senha Cadastrado.

Qual é a sequencia de passos necessarias para chegar ao resultado final?
    - Receber o Usuario.
    - Receber a Senha.
    - Verificar se o Usuario já Existe. 
    - Caso não exista, Cadastrar aquele Usuario e Senha.
         '''


# Passos Descritivos :

# Pedir Usuario. Receber um Usuario.
# Pedir Senha. Receber uma Senha.
# Armazenar os Usuários e Senhas Existentes.
# Permitir que Usuarios existentes possam fazer o Login.
# Verificar se a Senha Providenciada para aquele Usuário é a mesma Senha que está na nossa lista de senhas.
# Caso não exista, Cadastrar aquele Usuário e Senha.
# O Sistema deve alertar caso a Senha e Login não estejam corretos.


# <<< CODDING!!! >>>


usuarios = ['carol','amanda','jeferson']
senhas = ['123456','abcdef','123abcd']
resposta = input("[1] - Cadastrar novo Usuário [2] - Fazer Login: ")

if resposta == '1':
    
    usuario_digitado = input("Digite seu Usuário: ")
    
    if usuario_digitado in usuarios:
        print("Usuário Existente")
    else:
        senha_digitada = input("Digite sua Senha: ")
        usuarios.append(usuario_digitado)
        senhas.append(senha_digitada)
        
elif resposta == '2':
    
    usuario_digitado = input("Digite seu Usuário: ")
    senha_digitada = input("Digite sua Senha: ")
    encontrado = False 
    
    for indice, usuario in enumerate(usuarios):
        
        if usuario_digitado == usuario and senha_digitada == senhas[indice]:
            print("Login feito com Sucesso")
            encontrado = True
            
        elif encontrado == False:
            print("Usuário ou Senha Incorreto!")           
else:
    print("Digite Apenas '1' ou '2'")