# Escreva um programa que leia um numero real e mostre na tela sua parte inteira. EX: 6.127 tem a parte inteira 6

import math
print('Não Utilize virgula, apenas o Ponto . ')
real = float(input('Digite um Número Real, EX(6.127): '))
inteiro = math.floor(real)
# math.floor() arredonda o numero para baixo
print(f'O Número {real} tem como sua parte inteira o numero {inteiro}')