algo = input('Digite Algo: ')
print('O Tipo Primitivo do Valor Digitado é: ',type(algo))
print('É Composto somente de espaços: ', algo.isspace()) # algo é uma variavel, o ponto chama uma função em Python, e isspace() é uma função que verifica se a variavel é composta de espaços
print('É Um Número: ', algo.isnumeric()) # algo é uma variavel, o ponto chama uma função em Python, e isnumeric() é uma função que verifica se a variavel é composta de numeros
print('É alfabetico: ',algo.isalpha()) # algo é uma variavel, o ponto chama uma função em Python, e isalpha() é uma função que verifica se a variavel é composta de letras
print('É alfanumerico: ', algo.isalnum()) # algo é uma variavel, o ponto chama uma função em Python, e isalnum() é uma função que verifica se a variavel é composta de letras e numeros
print('Está em Maiúsculas: ', algo.isupper()) #O Comando isupper() serve para verificar se oque foi digitado ou se a variavel está em Maiúsculas
print('Está em Minúscula: ',algo.islower()) # O Comando islower server para verificar se oque foi digitado ou se a variavel está em Minúsculas
print('Está Captalizada: ',algo.istitle())# O comando istitle() server para verificar se o A Primeira letra digitada ou da variavel está em Maiúscula
