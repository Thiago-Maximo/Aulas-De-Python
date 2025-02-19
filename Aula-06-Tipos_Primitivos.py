# PRIMEIRA FORMA DE FAZER



# Tipos Primitivos
from distutils.command.clean import clean

# Começo da Função
def somar(a,b):
    return a + b
# Fim da Função

# Começo da Função
def subtrair(a,b):
    return a - b
# Fim da Função

def menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print('########################################')

# Inteiro (Int)
def calc():
    while True:
        menu()
        operador = input('Escolha o Operação: 1/2/3/4/5: ')

        if operador not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        if operador == '5':
            print('<<<SAINDO>>>')
            break

        # Entrada de números
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue
        if operador == '1':
            print(f'A Soma de {n1} + {n2}, é de: {somar(n1,n2)}')











# SEGUNDA FORMA DE FAZER

# # Função para Somar
# def somar(a, b):
#     return a + b
# # Função para subtrair
# def subtrair(a, b):
#     return a - b
#
# # Função para multiplicar
# def multiplicar(a, b):
#     return a * b
#
# # Função para dividir
# def dividir(a, b):
#     if b == 0:
#         return "Não é possível dividir por zero!"
#     return a / b
#
# def limpar_tela():
#     print("\n" * 100)  # Imprime 100 quebras de linha
#
# # Exemplo de uso
# limpar_tela()
#
# def menu():
#     print('Escolha uma Operação:')
#     print("1 - Somar")
#     print("2 - Subtrair")
#     print("3 - Multiplicar")
#     print("4 - Dividir")
#     print("5 - Sair")
#     print('########################################')
#
# def calculadora():
#     while  True:
#
#         print('')
#         print('#########################################')
#         menu()  #Exibe o Menu
#         escolha = input("Escolha uma operação (1/2/3/4/5): ")
#
#         if escolha == '5':
#             print('')
#             print('<<<<<<Saindo>>>>>>')
#             break
#
#         if escolha not in ['1', '2', '3', '4']:
#             print("Opção inválida! Tente novamente.")
#             continue
#
#         # Entrada de números
#         try:
#             n1 = float(input("Digite o primeiro número: "))
#             n2 = float(input("Digite o segundo número: "))
#         except ValueError:
#             print("Por favor, insira números válidos.")
#             print('')
#             print('#########################################')
#             continue
#
#         # Execução da operação
#         if escolha == '1':
#             limpar_tela()
#             print('')
#             print('########################################')
#             print(f"O resultado da soma é: {somar(n1,n2)}")
#             print('')
#             print('########################################')
#
#         elif escolha == '2':
#
#             print('')
#             print('########################################')
#             print(f"O resultado da subtração é: {subtrair(n1,n2)}")
#             print('')
#             print('########################################')
#         elif escolha == '3':
#             print('')
#             print('########################################')
#             print(f"O resultado da multiplicação é: {multiplicar(n1,n2)}")
#             print('')
#             print('########################################')
#         elif escolha == '4':
#             print('')
#             print('########################################')
#             print(f"O resultado da divisão é: {dividir(n1,n2)}")
#             print('')
#             print('########################################')
# calculadora()