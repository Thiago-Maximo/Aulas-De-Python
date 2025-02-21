# Faça um Programa que leia um numero e em seguida exiba a sua tabuada


numero = int(input('Digite Um Número: '))  # O número inicial
limite = 9  # O valor até onde queremos ir
tabu = 1
resultado = 1
print('')
print('Tabuada do Número Digitado:')

for _ in range(limite + 1):  # range define até onde o numero irá ir / re repetir
    print(numero, '*', tabu, '=',resultado)
    tabu += 1
    resultado = tabu * numero
