# print("Hello World!")

# variaveis

# nome = "Pedro"
# idade = 21
# peso = 63.5

# print(nome)
# print(idade)
# print(peso)

# entrada de dados(input)

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# peso = float(input("Digite seu peso: "))

# print(type(idade))
# print(type(peso))

# operadores

# soma = 1 + 1
# multiplicacao = 2 * 2
# divisao = 4 / 2
# sub = 4 - 2

# print(soma)
# print(multiplicacao)
# print(divisao)
# print(sub)

# condicionais

# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Pode entrar!")
# else:
#     print("Nao pode entrar!")

# salario = float(input("Informe seu salario: "))

# if salario <= 1500:
#     print("Programador Junior!")
# elif salario <= 4000:
#     print("Programador Senior!")
# else:
#     print("Gerente de projetos!")

# listas

# lista_numeros = [1, 2, 3]


# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])

# lista_numeros[0] = 5

# print(lista_numeros[0])


# lista_vazia = []
# lista_vazia.append("Ola")
# lista_vazia.append("Mundo")

# print(lista_vazia)

# repeticoes

# notas = []

# for x in range(4):
#     codigo_aluno = input("RM: ")
#     nota = float(input("Nota: "))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

# dicionarios

# funcionario = {
#     "nome": "Pedro",
#     "idade" : 21,
#     "salario" : 1700.5
# }

# print(funcionario['nome'])
# print(funcionario['idade'])
# print(funcionario['salario'])

# import os

# mensagens = []

# nome = input("Nome: ")

# while True:
#     # limpando terminal
#     os.system('cls')

#     if len(mensagens) > 0:
#         for m in mensagens:
#             print(m['nome'], '-', m['texto'])

#     print("---------------------")

#     # obtendo mensagem
#     texto = input("mensagem: ")
#     if texto == "fim":
#         break
#     # adicionando mensagem na lista
#     mensagens.append({
#         "nome": nome,
#         "texto": texto
#     })

# funcoes

# def minha_funcao(valor1, valor2):
    
#     return valor1 + valor2

# resposta = minha_funcao(10, 10)

# print("resposta", resposta)