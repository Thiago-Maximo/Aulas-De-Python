# faça um programa que leia um numero inteiro e mostre seu sucessor e seu antecessor.

# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Exibe o antecessor e o sucessor
print(f"O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.")
