# Operadores Aritméticos
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potenciação
# // Divisão Inteira
# % Resto da Divisão

n1 = 5
n2 = 2
resultado_adicao = n1 + n2
resultado_subtracao = n1 - n2
resultado_multiplicacao = n1 * n2
resultado_divisao = n1 / n2
resultado_potencia = n1 ** n2
resultado_divisao_inteira = n1 // n2
resultado_resto_divisao = n1 % n2
print('#############################################################################')
print(f'O  Resultado da Adição de {n1} + {n2} é de : {resultado_adicao} ')
print(f'O  Resultado da Subtração de {n1} + {n2} é de : {resultado_subtracao}')
print(f'O  Resultado da Multiplicação de {n1} + {n2} é de : {resultado_multiplicacao}')
print(f'O  Resultado da Divisão de {n1} + {n2} é de : {resultado_divisao}')
print(f'O  Resultado da Potenciação de {n1} + {n2} é de : {resultado_potencia}')
print(f'O  Resultado da Divisão Inteira de {n1} + {n2} é de : {resultado_divisao_inteira}')
print(f'O  Resultado do Resto da Divisão de {n1} + {n2} é de : {resultado_resto_divisao}')

print('')
print('#############################################################################')

######################### Ordem De Precedência No Python ###############
# 1 () : Parenteses
# 2 ** :  Potenciação
# 3 *, /, //, % : Multplicação, Divisão, Divisão Inteira, Resto da Divisão
# 4 +, - : Soma e Subtração

print('Ordem de Precedência No Python')
print('')
print('1 - () : Parenteses')
print('2 - ** :  Potenciação')
print('3 - *, /, //, % : Multplicação, Divisão, Divisão Inteira, Resto da Divisão')
print('4 - +, - : Soma e Subtração')

print('')
print('#############################################################################')

# Para Calcular a Raiz Quadrada Basta Fazer o Numero elevado a 1/2. EX: 25**(1/2)
print('')
print('Raiz Quadrada de 25 é: ',25**(1/2) )
print('Para Calcular a Raiz Quadrada Basta Fazer o Numero elevado a 1/2. EX: 25**(1/2)')
print('')
print('#'*80)

# Para Calcular a Raiz Cubica Basta Fazer o Msmo Processo, porém utilizando 1/3. EX: 127**(1/3)
print('')
print('Raiz Cubica de 127 é: ',127**(1/3) )
print('Para Calcular a Raiz Cubica Basta Fazer o Msmo Processo, porém utilizando 1/3. EX: 127**(1/3)')
print('')
print('#############################################################################')

# É Possivel utilizar o * para replicar textos
print('É Possivel utilizar o * para replicar textos')
print('# * 80')
print('Resultado:')
print('#'*80)

#Alinhamento de Texto/String
# É Possivel utilizar os sinais de, < > ^ para alinhar, e colocando um numero depois do sinal indicando quanto de espaço você quer
print('Exemplo de Alinhamento Centralizado')
print('Prazer em te conhecer {:=^20Nome}')
nome = 'Thiago'
print('Prazer Te Conhcer {:=^20}!'.format(nome))
print('')
print('#################################################')

# Alinhamento a Esquerda
print('Exemplo de Alinhamento a Esquerda')
print('Prazer em te conhecer {:=<20Nome}')
nome = 'Thiago'
print('Prazer Te Conhcer {:=<20}!'.format(nome))
print('')
print('#############################################')

# Alinhamento a Direita
print('Exemplo de Alinhamento a Direita')
print('Prazer em te conhecer {:=>20Nome}')
nome = 'Thiago'
print('Prazer Te Conhcer {:=>20}!'.format(nome))

# Formatação de Casa Decimal

# Para Formatar um Numero e deixa-lo somente com 2 ou mais casas decimais, basta fazer o seguinte. {:2f}, o numero 2 corresponde a quantia de casas decimais que eu quero exibir
print('')
print('#############################################')
print('Formatação de Numeros')
n3 = 4
n4 = 3
print('Usando os Numero 4 e 3 como Exemplo, 4 na variavel n3 e 3 na varival n4 ')
print('')

soma = n3 + n4
mult = n3 * n4
div = n3 / n4
div_i = n3 // n4
expo = n3 ** n4

print('A Soma é {}, A Multiplicação é {} e a Divisão é {:.2f}'.format(soma, mult, div), '.O Resultado da Divisão foi Formatado, o resultado era 1.33333333')
print('A Divisão Inteira é {} e a Potência é {}'.format(div_i, expo))
print('')
print('#'*80)

# Para Quebrar a Linha e o texto ir para a linha debaixo use o comando zn, para não quebrar e continuar na mesma linha utilize end ='', se der um espaço dentro do '', ele cria um espaço entre os print e não deixa o texto junto
print('Exemplo de QUebra de Linha com o \n')
print('Teste da \n quebra de linha')
print('#'*120)
print('Exemplo da Não quebra de Linha, usando dois print() e juntando na mesma linha')
print('Texto do print(1)', end=',')
print('Texto do print(2)')
print('#'*120)