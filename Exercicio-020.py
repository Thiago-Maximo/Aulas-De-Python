# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos, faça um programa que leia o nome dos alunos e mostre a ordem sorteada
import math
import random  # Importando a biblioteca correta

vetor_nomes = []

# Solicitar os nomes dos alunos
print('UTILIZE A VIRGULA PARA SEPARAR')
nomes = input('Digite o nome de seus alunos: ')

# Transformar a string de nomes em uma lista, separando pelos espaços
vetor_nomes = nomes.split(',')  # Usando a vírgula como separador

# Embaralhando a lista de nomes
random.shuffle(vetor_nomes)

# Exibindo os nomes em ordem aleatória
print("Nomes em ordem aleatória:")
for nome in vetor_nomes:
    print(nome.strip())  # .strip() remove espaços extras antes ou depois dos nomes

# Segunda forma de fazer

print('')

n1 = input('Digite o nome de seu aluno: ')
n2 = input('Digite o nome de seu aluno: ')
n3 = input('Digite o nome de seu aluno: ')
n4 = input('Digite o nome de seu aluno: ')

lista = [n1, n2,n3,n4]
random.shuffle(lista)
print(f'O aluno escolhido foi: {lista}')
