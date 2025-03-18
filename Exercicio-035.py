# Escreva um programa que Pergunte o Salario de um funcionario e calcule o valor do seu aumento.
# Para Salarios superiores a R$1.250,00 calcule um aumento de 10% para os inferiores ou iguais, o aumento é de 15%

print('#' * 100)
print('')
salario_original = float(input('Digite o seu Salário atual R$: '))
print('')

if salario_original > 1250:
    percentual_aumento = 10  # O aumento é de 15%, mas no código estava 10%
    valor_aumento = salario_original * (percentual_aumento / 100)
    salario_novo = salario_original + valor_aumento

    print('#' * 100)
    print('')
    # Corrigido a formatação para R$ com duas casas decimais
    print(f'O Seu Novo Salário é de: R${salario_novo:.2f}')
    print('')
    print('#' * 100)
if salario_original <= 1250:
    percentual_aumento = 15  # O aumento é de 15%, mas no código estava 10%
    valor_aumento = salario_original * (percentual_aumento / 100)
    salario_novo = salario_original + valor_aumento

    print('#' * 100)
    print('')
    # Corrigido a formatação para R$ com duas casas decimais
    print(f'O Seu Novo Salário é de: R${salario_novo:.2f}')
    print('')
    print('#' * 100)

# 2° Forma de se fazer
print('#' * 100)
print('')
salario_original = float(input('Digite o seu Salário atual R$: '))
print('')

if salario_original <= 1250:
    novo = salario_original + (salario_original * 15 / 100)
else:
    novo = salario_original + (salario_original * 10 / 100)
print('Quem Ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario_original,novo))