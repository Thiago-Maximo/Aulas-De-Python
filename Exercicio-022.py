# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1°: O nome com todas as letras Maiusculas.
# 2°: O nome com todas as letras Minusculas.
# 3°: Quantas letras tem ao total (Sem Considerar espaços)
# 4°: Quantas letras tem o primerio nome
# 5°: Deixe Somente a Primeira letra do primerio nome em maiuscula

# 1° Etapa:
print('1°: O nome com todas as letras Maiusculas.')
print('')
nome_maiucula = input('Digite Seu Nome Completo: ')
print(nome_maiucula.upper())

print('')

# 2° Etapa:
print('')
print('2°: O nome com todas as letras Minusculas.')
print('')
nome_minuscula = input('Digite Seu Nome Completo: ')
print(nome_minuscula.lower())

print('')

# 3° Etapa:
print('')
print('3°: Quantas letras tem ao total (Sem Considerar espaços).')
print('')
nome_letras = input('Digite Seu Nome Completo: ')
nome_sem_espacos = nome_letras.replace(" ","")
print(len(nome_sem_espacos))

# print('')

# 4° Etapa:
print('')
print('4°: Quantas letras tem o primerio nome.')
print('')
nome = input('Digite Seu Nome Completo: ')
lista = nome.split() #o split cria uma lista, dessa forma posso verificar melhor a quantia de caracteres.
print(lista)
print(len(lista[0])) # Fiz desse jeito pois como o primeiro nome vai para a posição zero ent eu faço um len() que irá verificar o tamanho do texto que tem na posição/indice 0 da lista

print('')

# 5° Etapa:
print('')
print('5°: Deixe Somente a Primeira letra do primerio nome em maiuscula.')
print('')
nome = input('Digite Seu Nome Completo: ')
print(nome.capitalize())