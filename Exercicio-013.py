# Crie um algoritmo que leia o Salário de um funcionario e mostre o seu novo salário, com 15% de aumento.
print('#'*100)
print('')
salario_original = float(input('Digite o seu Salário atual R$: '))
print('')

percentual_aumento = 15  # O aumento é de 15%, mas no código estava 10%
valor_aumento = salario_original * (percentual_aumento / 100)
salario_novo = salario_original + valor_aumento

print('#'*100)
print('')
# Corrigido a formatação para R$ com duas casas decimais
print(f'O Seu Novo Salário é de: R${salario_novo:.2f}')
print('')
print('#'*100)
