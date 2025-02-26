# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import math
import random  # Importação da biblioteca correta

vetor_nomes = []

# Solicitar os nomes dos alunos
print('UTILIZE A VIRGULA PARA SEPARAR')
nomes = input('Digite o nome de seus alunos: ')

# Transformar a string de nomes em uma lista, separando pelos espaços
vetor_nomes = nomes.split(',')  # Usando a vírgula como separador

# Sorteando um nome aleatório
escolhido = random.choice(vetor_nomes)

# Exibindo o nome do aluno escolhido
print(f'O aluno escolhido foi: {escolhido.strip()}')  # .strip() remove espaços extras

# Segunda Forma de Fazer
n1 = input('Digite o nome de seu aluno: ')
n2 = input('Digite o nome de seu aluno: ')
n3 = input('Digite o nome de seu aluno: ')
n4 = input('Digite o nome de seu aluno: ')

lista = [n1, n2,n3,n4]
escolhido_novo = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido_novo}')


# Hoje, ao tentar escrever um programa para sortear um aluno de um grupo, encontrei um erro que me impediu de rodar o código corretamente. Eu estava tentando usar a função random.choice() para escolher aleatoriamente um nome de um vetor, mas algo não estava funcionando. O erro aconteceu por dois motivos principais, e aqui está o que eu percebi:
#
# O que eu fiz de errado:
# Confundi o tipo de dados da variável: Ao tentar atribuir o valor digitado pelo usuário à minha lista vetor_nomes, eu cometi o erro de simplesmente fazer:
# vetor_nomes = nomes
# Porém, nomes é uma string (uma sequência de caracteres), não uma lista. O que eu realmente queria fazer era transformar essa string em uma lista, já que a função random.choice() precisa de uma lista como argumento. Quando eu fiz a atribuição, eu não estava criando uma lista, só estava copiando a string para a variável vetor_nomes. Esse foi o erro. Eu precisava separar os nomes em itens individuais dentro de uma lista, para poder fazer o sorteio.
#
# Não fiz a conversão de string para lista: Para corrigir isso, percebi que deveria usar o
# vetor_nomes = nomes.split(',')
# Como eu corrigi: Ao adicionar .split(','), a string nomes foi dividida corretamente em uma lista, onde cada nome passou a ser um elemento da lista vetor_nomes. Agora, eu podia usar random.choice(vetor_nomes) para escolher um nome aleatório da lista.
#
# O aprendizado:
# Eu aprendi que o random.choice() só funciona com listas ou outras sequências (como tuplas). Como eu estava passando uma string (que é uma sequência de caracteres) em vez de uma lista de nomes, o código não funcionou corretamente.
# O importante aqui foi perceber que eu precisava dividir a string em uma lista de nomes antes de passar essa lista para o random.choice().
# Agora, o código está funcionando corretamente, sorteando um nome aleatório da lista de alunos. Eu acho que o maior erro foi não perceber logo que a conversão de string para lista era necessária.