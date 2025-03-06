# Crie um Programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro nome e o ultimo nome separados.
# EX: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

# Solicita o nome completo da pessoa
nome_completo = input("Digite seu nome completo: ")

# Divide o nome completo em uma lista de palavras
nome_dividido = nome_completo.split()

# O primeiro nome será o primeiro item da lista
primeiro_nome = nome_dividido[0]

# O último nome será o último item da lista
ultimo_nome = nome_dividido[-1]

# Exibe o primeiro e o último nome
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
