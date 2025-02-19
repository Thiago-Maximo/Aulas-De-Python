# Função para somar
def somar(a, b):
    return a + b

# Função para subtrair
def subtrair(a, b):
    return a - b

# Função para multiplicar
def multiplicar(a, b):
    return a * b

# Função para dividir
def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero!"
    return a / b

# Menu de opções
def menu():
    print("Selecione a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
print('')
print('########################################')
# Função principal
def calculadora():
    while True:
        menu()  # Exibe o menu
        escolha = input("Escolha uma operação (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo...")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        # Entrada de números
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        # Execução da operação
        if escolha == '1':
            print(f"O resultado da soma é: {somar(num1, num2)}")
            print('')
            print('########################################')
        elif escolha == '2':
            print(f"O resultado da subtração é: {subtrair(num1, num2)}")
            print('')
            print('########################################')
        elif escolha == '3':
            print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
            print('')
            print('########################################')
        elif escolha == '4':
            print(f"O resultado da divisão é: {dividir(num1, num2)}")
            print('')
            print('########################################')

# Rodando a calculadora
calculadora()