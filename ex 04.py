algo = input('Digite Algo: ')
print('O Tipo Primitivo do Valor Digitado é: ',type(algo))
print('É Composto somente de espaços: ', algo.isspace()) # algo é uma variavel, o ponto chama uma função em Python, e isspace() é uma função que verifica se a variavel é composta de espaços
print('É Um Número: ', algo.isnumeric()) # algo é uma variavel, o ponto chama uma função em Python, e isnumeric() é uma função que verifica se a variavel é composta de numeros
print('É composto somente por letra: ',algo.isalpha()) # algo é uma variavel, o ponto chama uma função em Python, e isalpha() é uma função que verifica se a variavel é composta de letras
print('É composto por numeros e letras: ', algo.isalnum()) # algo é uma variavel, o ponto chama uma função em Python, e isalnum() é uma função que verifica se a variavel é composta de letras e numeros
