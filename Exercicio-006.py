# Crie um algoritimo que leia um numero e exiba seu dobro, triplo e raiz quadrada

# Primeira Forma de Fazer
print('#'*50)
n1 = int(input('Digite Um Número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1**(1/2)


print('#'*50)
print('1° Forma de se Fazer, usando Variaveis')
print(f' O Dobro de {n1} é {dobro} \n o Triplo é {triplo} \n a Raiz Quadrada é {raiz:.2f}')

print('')
print('#'*50)

# Segunda Forma de Fazer
n2 = int(input('Digite Um Número: '))

print('#'*50)
print('2° Forma de se Fazer, Passando os Parametros no print()')
print(f' O Dobro de {n2} é {n2*2} \n o Triplo é {n2*3} \n a Raiz Quadrada é {n2**(1/2):.2f}')
print('#'*50)