# Programa que lê 3 números e mostra o maior e o menor

# Solicita a entrada de 3 números
numeros = input("Digite 3 números separados por espaço: ")

# Divide a entrada em uma lista de números
numeros = [float(x) for x in numeros.split()]

# Calcula o maior e o menor número
maior = max(numeros)
menor = min(numeros)

# Exibe os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

print('')
print('2° Forma de se Fazer')
print('')
# 2° Forma de se Fazer

# Programa que lê 3 números e mostra o maior e o menor

# Solicita a entrada de 3 números
n1, n2, n3 = map(float, input("Digite 3 números separados por espaço: ").split())

# Calcula o maior e o menor número
maior = n1
menor = n1

# Comparando diretamente os números
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Exibe os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
