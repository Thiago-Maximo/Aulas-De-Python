# Aula de Condições, tomadas de decisão. if, else, else if, while, do while, for....

# Programa que le o ano de lançamento de um carro e diz quantos anos o carro tem.
import datetime #Biblioteca contendo métodos de data e hora
ano_atual = datetime.datetime.now().year

carro_ano = int(input('Digite o Ano de Lançamento do Carro: '))

ano_atual_formatado = int(ano_atual)
ano_carro = ano_atual_formatado - carro_ano #Calculando a Idade do Carro

print(f'O seu Carro tem {ano_carro} Anos')
if ano_carro > 25:
    print('')
    print('#'*110)
    print(f'Você tem Direito a não pagar mais o IPVA do seu carro pois ele já tem {ano_carro} anos.')
else:
    print('')
    print('#'*110)
    print(f'Você ainda tem que Pagar o IPVA do seu carro pois ele só tem {ano_carro} anos, ele teria que ter 25 anos de lançamento.')


print('')
print('#'*80)
# Utilizando o If ternário
print('Utilizando o If ternário, ou seja o if e else estão na mesma linha que o print')



n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = (n1+n2) / 2
print('A Sua Média foi de {:.1f}'.format(m))
print('')
print('#'*30)
print('APROVADO' if m >=6 else 'REPROVADO')