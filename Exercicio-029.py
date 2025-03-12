# Escreva Um Programa que Faça o Computador "Pensar" em um numero inteiro entre 0 e 5 e peça para o Usuario tentar adivinhar qual foi o nome esolhido pelo computador.
# O Programa deverá escrever na tela se o usuario venceu ou perdeu.

import math
import random

numero_pc = random.randint(0,5) # random.randint() irá "escolher" um numero inteiro aleatório dentre a faixa que foi digitada dentro dos Parenteses ()
print('Tente Advinhar o Numero Escolhido Pelo Computador')
print(numero_pc) # Exibe o Numero que o computador escolheu
numero_usuario = int(input('Digite Aqui: ')) # lê o numero que o usuario digitou

if numero_usuario == numero_pc: # Verifica se o numero digitado pelo usuario foi o mesmo que o computador escolheu e exibe as mensagens ao Usuario se for igual os valores
    print('Parabéns Você Acertou o Numero Escolhido!!')
    print(f'O Número que você escolheu foi {numero_usuario} e o Computador escolheu {numero_pc}')
else: # Se os numeros não forem iguais então ele exibe essas mensagens
    print('Que Pena Você Não Acertou o Número Escolhido Pelo Computador')
    print(f'Seu Numero foi {numero_usuario} e o Computador Escolheu {numero_pc}')